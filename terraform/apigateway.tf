# provider "aws" {
#     region = "eu-west-3"
# }

# // API Gateway
# resource "aws_api_gateway_rest_api" "AttendanceAPI" {
#     name        = "AttendanceAPI"
#     description = "This is the API for the attendance system."

#     endpoint_configuration {
#         types = ["REGIONAL"]
#     }
# }

# # resource "aws_api_gateway_authorizer" "demo" {
# #     name          = "AttendanceAPIg_authorizer2"
# #     rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
# #     type          = "COGNITO_USER_POOLS"
# #     provider_arns = [aws_cognito_user_pool.pool.arn]
# # }

# resource "aws_api_gateway_resource" "root" {
#     rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
#     parent_id   = aws_api_gateway_rest_api.AttendanceAPI.root_resource_id
#     path_part   = "mypath"
# }

# resource "aws_api_gateway_method" "proxy" {
#     rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id = aws_api_gateway_resource.root.id
#     http_method = "POST"

#     authorization = "NONE" // comment this out in cognito section
#     # authorization = "COGNITO_USER_POOLS"
#     # authorizer_id = aws_api_gateway_authorizer.demo.id
# }

# resource "aws_api_gateway_integration" "lambda_integration" {
#     rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id             = aws_api_gateway_resource.root.id
#     http_method             = aws_api_gateway_method.proxy.http_method
#     integration_http_method = "POST"
#     # type                    = "MOCK"
#     type                    = "AWS"
#     uri                     = aws_lambda_function.html_lambda.invoke_arn
# }

# resource "aws_api_gateway_method_response" "proxy" {
#     rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id = aws_api_gateway_resource.root.id
#     http_method = aws_api_gateway_method.proxy.http_method
#     status_code = "200"

#     //cors section
#     response_parameters = {
#         "method.response.header.Access-Control-Allow-Headers" = true,
#         "method.response.header.Access-Control-Allow-Methods" = true,
#         "method.response.header.Access-Control-Allow-Origin"  = true
#     }
# }

# resource "aws_api_gateway_integration_response" "proxy" {
#     rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id = aws_api_gateway_resource.root.id
#     http_method = aws_api_gateway_method.proxy.http_method
#     status_code = aws_api_gateway_method_response.proxy.status_code


#     //cors
#     response_parameters = {
#         "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
#         "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
#         "method.response.header.Access-Control-Allow-Origin"  = "'*'"
#     }

#     depends_on = [
#         aws_api_gateway_method.proxy,
#         aws_api_gateway_integration.lambda_integration
#     ]
# }

# //options
# resource "aws_api_gateway_method" "options" {
#     rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id = aws_api_gateway_resource.root.id
#     http_method = "OPTIONS"
#     authorization = "NONE"

#     # authorization = "COGNITO_USER_POOLS"
#     # authorizer_id = aws_api_gateway_authorizer.demo.id
# }

# resource "aws_api_gateway_integration" "options_integration" {
#     rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id             = aws_api_gateway_resource.root.id
#     http_method             = aws_api_gateway_method.options.http_method
#     integration_http_method = "OPTIONS"
#     type                    = "MOCK"
#     request_templates = {
#         "application/json" = "{\"statusCode\": 200}"
#     }
# }

# resource "aws_api_gateway_method_response" "options_response" {
#     rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id = aws_api_gateway_resource.root.id
#     http_method = aws_api_gateway_method.options.http_method
#     status_code = "200"

#     response_parameters = {
#         "method.response.header.Access-Control-Allow-Headers" = true,
#         "method.response.header.Access-Control-Allow-Methods" = true,
#         "method.response.header.Access-Control-Allow-Origin"  = true
#     }
# }

# resource "aws_api_gateway_integration_response" "options_integration_response" {
#     rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id = aws_api_gateway_resource.root.id
#     http_method = aws_api_gateway_method.options.http_method
#     status_code = aws_api_gateway_method_response.options_response.status_code

#     response_parameters = {
#         "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
#         "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
#         "method.response.header.Access-Control-Allow-Origin"  = "'*'"
#     }

#     depends_on = [
#         aws_api_gateway_method.options,
#         aws_api_gateway_integration.options_integration,
#     ]
# }

# resource "aws_api_gateway_method" "get_mypath" {
#     rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id   = aws_api_gateway_resource.root.id
#     http_method   = "GET"
#     authorization = "NONE"

#     request_parameters = {
#         "method.request.path.proxy" = true
#     }
# }

# resource "aws_api_gateway_integration" "get_mypath_integration" {
#     rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id             = aws_api_gateway_resource.root.id
#     http_method             = aws_api_gateway_method.get_mypath.http_method
#     integration_http_method = "GET"
#     type                    = "MOCK"
#     request_templates = {
#         "application/json" = "{\"statusCode\": 200}"
#     }
# }

# resource "aws_api_gateway_method_response" "get_mypath_response" {
#     rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id = aws_api_gateway_resource.root.id
#     http_method = aws_api_gateway_method.get_mypath.http_method
#     status_code = "200"

#     response_parameters = {
#         "method.response.header.Access-Control-Allow-Headers" = true,
#         "method.response.header.Access-Control-Allow-Methods" = true,
#         "method.response.header.Access-Control-Allow-Origin"  = true
#     }
# }

# resource "aws_api_gateway_integration_response" "get_mypath_integration_response" {
#     rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id = aws_api_gateway_resource.root.id
#     http_method = aws_api_gateway_method.get_mypath.http_method
#     status_code = aws_api_gateway_method_response.get_mypath_response.status_code

#     response_parameters = {
#         "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
#         "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
#         "method.response.header.Access-Control-Allow-Origin"  = "'*'"
#     }

#     depends_on = [
#         aws_api_gateway_method.get_mypath,
#         aws_api_gateway_integration.get_mypath_integration,
#     ]
# }

# resource "aws_api_gateway_method" "put_mypath" {
#     rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id   = aws_api_gateway_resource.root.id
#     http_method   = "PUT"
#     authorization = "NONE"

#     request_parameters = {
#         "method.request.path.proxy" = true
#     }
# }

# resource "aws_api_gateway_integration" "put_mypath_integration" {
#     rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id             = aws_api_gateway_resource.root.id
#     http_method             = aws_api_gateway_method.put_mypath.http_method
#     integration_http_method = "PUT"
#     type                    = "MOCK"
#     request_templates = {
#         "application/json" = "{\"statusCode\": 200}"
#     }
# }

# resource "aws_api_gateway_method_response" "put_mypath_response" {
#     rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id = aws_api_gateway_resource.root.id
#     http_method = aws_api_gateway_method.put_mypath.http_method
#     status_code = "200"

#     response_parameters = {
#         "method.response.header.Access-Control-Allow-Headers" = true,
#         "method.response.header.Access-Control-Allow-Methods" = true,
#         "method.response.header.Access-Control-Allow-Origin"  = true
#     }
# }

# resource "aws_api_gateway_integration_response" "put_mypath_integration_response" {
#     rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
#     resource_id = aws_api_gateway_resource.root.id
#     http_method = aws_api_gateway_method.put_mypath.http_method
#     status_code = aws_api_gateway_method_response.put_mypath_response.status_code

#     response_parameters = {
#         "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
#         "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
#         "method.response.header.Access-Control-Allow-Origin"  = "'*'"
#     }

#     depends_on = [
#         aws_api_gateway_method.put_mypath,
#         aws_api_gateway_integration.put_mypath_integration,
#     ]
# }



# resource "aws_api_gateway_deployment" "deployment" {
#     depends_on = [
#         aws_api_gateway_integration.lambda_integration,
#         aws_api_gateway_integration.options_integration,
#     ]

#     rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
#     stage_name  = "dev"
# }


