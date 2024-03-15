/* API Gateway
* This is the terraform file for the API Gateway, the workflow is as follows:
* 1. Defining the locals to store the paths and methods for the API Gateway
* 2. Creating the API Gateway, resources, methods, integrations, method responses, and integration responses
* 3. Creating the stage and deployment for the API Gateway
* 4. Creating the log group for API Gateway and an IAM role for API Gateway to write to CloudWatch logs
*/

# ----------------- Defining the locals -----------------

# Defining the paths and methods for the API Gateway.
# Combine the path and methods with flatten to create a list of objects that can be accessed by the for_each method.
# Changing the to_define_paths or to_define_methods will automatically create the resources and methods for the API Gateway.
locals {
  to_define_paths   = ["admin", "teacher", "course", "department", "student", "cognito"]
  to_define_methods = ["GET", "OPTIONS", "PUT", "POST", "DELETE", "HEAD"]

  paths_and_methods = flatten([
    for path in local.to_define_paths : [
      for method in local.to_define_methods : {
        path   = path
        method = method
      }
    ]
  ])
}

# ----------------- Creating the API Gateway -----------------

# Creating the API Gateway.
resource "aws_api_gateway_rest_api" "AttendanceAPI" {
  name        = "AttendanceAPI"
  description = "This is the API for the attendance system."

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

# Creating the resources for the API Gateway, one for each path.
resource "aws_api_gateway_resource" "paths" {
  for_each    = toset(local.to_define_paths)
  rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
  parent_id   = aws_api_gateway_rest_api.AttendanceAPI.root_resource_id
  path_part   = each.value
}

# Creating the methods for the API Gateway, one for each path and method.
resource "aws_api_gateway_method" "methods" {
  for_each    = { for pm in local.paths_and_methods : "${pm.path}-${pm.method}" => pm }
  resource_id = aws_api_gateway_resource.paths[each.value.path].id
  rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
  http_method = each.value.method

  request_parameters = {
    "method.request.path.proxy" = true
  }
  authorization = "NONE"
  # authorization = "COGNITO_USER_POOLS"
  # authorizer_id = aws_api_gateway_authorizer.student_authorizer.id
}

# Creating the integration for non-OPTIONS methods.
resource "aws_api_gateway_integration" "integrations_non_options" {
  for_each                = { for pm in local.paths_and_methods : "${pm.path}-${pm.method}" => pm if pm.method != "OPTIONS" }
  rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
  resource_id             = aws_api_gateway_resource.paths[each.value.path].id
  http_method             = aws_api_gateway_method.methods[each.key].http_method
  type                    = "AWS_PROXY"
  integration_http_method = "POST"
  uri                     = aws_lambda_function.lambda[each.value.path].invoke_arn
}

# Creating the Mock Integration for OPTIONS methods.
resource "aws_api_gateway_integration" "integrations_options" {
  for_each    = { for pm in local.paths_and_methods : "${pm.path}-${pm.method}" => pm if pm.method == "OPTIONS" }
  rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
  resource_id = aws_api_gateway_resource.paths[each.value.path].id
  http_method = aws_api_gateway_method.methods[each.key].http_method
  type        = "MOCK"
  request_templates = {
    "application/json" = "{\"statusCode\": 200}"
  }
}

# Creating the method responses for the API Gateway, one for each path and method.
resource "aws_api_gateway_method_response" "responses" {
  for_each    = { for pm in local.paths_and_methods : "${pm.path}-${pm.method}" => pm }
  rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
  resource_id = aws_api_gateway_resource.paths[each.value.path].id
  http_method = aws_api_gateway_method.methods[each.key].http_method
  status_code = 200

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = true,
    "method.response.header.Access-Control-Allow-Methods" = true,
    "method.response.header.Access-Control-Allow-Origin"  = true
  }
}

# Creating the integration responses for the API Gateway, one for each path and method.
resource "aws_api_gateway_integration_response" "integration_responses" {
  for_each    = { for pm in local.paths_and_methods : "${pm.path}-${pm.method}" => pm }
  rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
  resource_id = aws_api_gateway_resource.paths[each.value.path].id
  http_method = aws_api_gateway_method.methods[each.key].http_method
  status_code = aws_api_gateway_method_response.responses[each.key].status_code

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,Access-Control-Allow-Origin'",
    "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
    "method.response.header.Access-Control-Allow-Origin"  = "'*'"
  }

  # As depends_on does not allow dynamic references, we give it the complete list of integrations for every integration response.
  depends_on = [aws_api_gateway_integration.integrations_non_options, aws_api_gateway_integration.integrations_options]
}

# ----------------- Deployment for the API Gateway -----------------

# Creating the production stage for the API Gateway.
resource "aws_api_gateway_stage" "production_stage" {
  stage_name    = "prod"
  rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
  deployment_id = aws_api_gateway_deployment.deployment_production.id

  xray_tracing_enabled = true

  # Specifying some common access logs settings which can help with monitoring and debugging.
  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.api_gateway_access_logs.arn
    format = jsonencode({
      requestId      = "$context.requestId",
      ip             = "$context.identity.sourceIp",
      caller         = "$context.identity.caller",
      user           = "$context.identity.user",
      requestTime    = "$context.requestTime",
      httpMethod     = "$context.httpMethod",
      resourcePath   = "$context.resourcePath",
      status         = "$context.status",
      protocol       = "$context.protocol",
      responseLength = "$context.responseLength"
    })
  }
}

# Creating the method settings for the API Gateway.
resource "aws_api_gateway_method_settings" "method_settings" {
  rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
  stage_name  = aws_api_gateway_stage.production_stage.stage_name
  method_path = "/*/*" # Specifies all methods for all resources

  settings {
    logging_level      = "INFO"
    metrics_enabled    = true
    data_trace_enabled = true # Detailed request/response logs
  }
}

# Creating the deployment for the API Gateway.
resource "aws_api_gateway_deployment" "deployment_production" {
  # The deployment depends on correct configuration of all the resources and methods.
  depends_on = [
    aws_api_gateway_integration.integrations_non_options,
    aws_api_gateway_integration.integrations_options,
    aws_api_gateway_method.methods,
    aws_api_gateway_resource.paths,
    aws_api_gateway_method_response.responses,
    aws_api_gateway_integration_response.integration_responses
  ]

  rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id

  # Redeploy the API Gateway when the timestamp changes, so everytime we run terraform apply, the API Gateway is redeployed.
  triggers = {
    redeployment = "${timestamp()}"
  }

  # We want to create the deployment before destroying the previous one, to avoid downtime.
  lifecycle {
    create_before_destroy = true
  }
}

# ----------------- CloudWatch Logs -----------------

# # Creating the log group for API gateway
resource "aws_cloudwatch_log_group" "api_gateway_access_logs" {
  name = "/aws/api-gateway/AttendanceAPI-access-logs"
}

# Creating an IAM role for API Gateway to write to CloudWatch logs
resource "aws_iam_role" "api_gateway_cloudwatch_role" {
  name = "api_gateway_cloudwatch_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "apigateway.amazonaws.com"
        }
      },
    ]
  })
}

# Creating the IAM policy for API Gateway to write to CloudWatch logs
resource "aws_iam_role_policy" "api_gateway_cloudwatch_policy" {
  name = "api_gateway_cloudwatch_policy"
  role = aws_iam_role.api_gateway_cloudwatch_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:DescribeLogGroups",
          "logs:DescribeLogStreams",
          "logs:PutLogEvents",
          "logs:GetLogEvents",
          "logs:FilterLogEvents"
        ],
        Effect   = "Allow",
        Resource = "*"
      },
    ]
  })
}


# # Attaching the standard policy to the IAM role
# resource "aws_iam_role_policy_attachment" "api_gateway_cloudwatch_logs_attachment" {
#   role       = aws_iam_role.api_gateway_cloudwatch_logs_role.name
#   policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs"
# }

# # Creating the API Gateway account
resource "aws_api_gateway_account" "api_gateway_account" {
  cloudwatch_role_arn = aws_iam_role.api_gateway_cloudwatch_role.arn

  #   depends_on = [
  #     aws_iam_role_policy_attachment.api_gateway_cloudwatch_logs_attachment
  #   ]
}
