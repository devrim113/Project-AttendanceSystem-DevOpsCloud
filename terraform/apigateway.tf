# Creating the API Gateway
resource "aws_api_gateway_rest_api" "AttendanceAPI" {
  name        = "AttendanceAPI"
  description = "This is the API for the attendance system."

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

# Defining the paths and methods for the API Gateway
# Combine the path and methods with flatten to create a list of objects that can be accessed by the for_each method
locals {
  to_define_paths   = ["admin", "teacher", "course", "department", "student"]
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

# Creating the resources for the API Gateway, one for each path
resource "aws_api_gateway_resource" "paths" {
  for_each    = toset(local.to_define_paths)
  rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
  parent_id   = aws_api_gateway_rest_api.AttendanceAPI.root_resource_id
  path_part   = each.value
}

# Creating the methods for the API Gateway, one for each path and method
resource "aws_api_gateway_method" "methods" {
  for_each      = { for pm in local.paths_and_methods : "${pm.path}-${pm.method}" => pm }
  resource_id   = aws_api_gateway_resource.paths[each.value.path].id
  rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
  authorization = "NONE"
  http_method   = each.value.method

  request_parameters = {
    "method.request.path.proxy" = true
  }
}

# Creating the integrations for the API Gateway, one for each path and method
resource "aws_api_gateway_integration" "integrations" {
  for_each                = { for pm in local.paths_and_methods : "${pm.path}-${pm.method}" => pm }
  rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
  resource_id             = aws_api_gateway_resource.paths[each.value.path].id
  http_method             = aws_api_gateway_method.methods[each.key].http_method
  integration_http_method = "POST"
  type                    = each.value.method == "OPTIONS" ? "MOCK" : "AWS_PROXY"

  # Use a conditional expression for the uri attribute
  uri = each.value.method == "OPTIONS" ? "arn:aws:apigateway:eu-central-1:lambda:path/2015-03-31/functions/placeholder/invocations" : aws_lambda_function.lambda[each.value.path].invoke_arn

  request_templates = each.value.method == "OPTIONS" ? {
    "application/json" = "{\"statusCode\": 200}"
  } : {}
}


# Creating the method responses for the API Gateway, one for each path and method
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

# Creating the integration responses for the API Gateway, one for each path and method
resource "aws_api_gateway_integration_response" "integration_responses" {
  for_each    = { for pm in local.paths_and_methods : "${pm.path}-${pm.method}" => pm }
  rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
  resource_id = aws_api_gateway_resource.paths[each.value.path].id
  http_method = aws_api_gateway_method.methods[each.key].http_method
  status_code = aws_api_gateway_method_response.responses[each.key].status_code

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
    "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
    "method.response.header.Access-Control-Allow-Origin"  = "'*'"
  }

  # As depends_on does not allow dynamic references, we give it the complete list of integrations for every integration response.
  depends_on = [aws_api_gateway_integration.integrations]
}

# Creating the deployment for the API Gateway
resource "aws_api_gateway_deployment" "deployment_production" {
  depends_on = [
    aws_api_gateway_integration.integrations,
    aws_api_gateway_method.methods,
    aws_api_gateway_resource.paths,
  ]

  rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
  stage_name  = "prod"

  triggers = {
    redeployment = "${timestamp()}"
  }

  lifecycle {
    create_before_destroy = true
  }
}

# Creating the CloudWatch role for API Gateway
resource "aws_iam_role" "cloudwatch_role" {
  name               = "api_gateway_cloudwatch_role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "apigateway.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

# Attaching the CloudWatch policy to the role
resource "aws_iam_role_policy_attachment" "cloudwatch_policy_attachment" {
  role       = aws_iam_role.cloudwatch_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs"
}

# Enabling CloudWatch logging for the API Gateway
resource "aws_api_gateway_stage" "stage_logging" {
  rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
  stage_name    = "prodv2"
  deployment_id = aws_api_gateway_deployment.deployment_production.id

  xray_tracing_enabled = true

  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.api_gateway_logs.arn
    format          = "$context.requestId"
  }

  lifecycle {
    ignore_changes = [deployment_id]
  }
}

# Creating the CloudWatch log group for API Gateway
resource "aws_cloudwatch_log_group" "api_gateway_logs" {
  name              = "/aws/api-gateway/${aws_api_gateway_rest_api.AttendanceAPI.id}"
  retention_in_days = 7
}
