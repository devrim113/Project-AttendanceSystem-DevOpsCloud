# Defining the locals to store the lambda functions and their handlers
locals {
  lambda_functions = {
    "student"    = "student.lambda_handler",
    "admin"      = "admin.lambda_handler",
    "teacher"    = "teacher.lambda_handler",
    "course"     = "course.lambda_handler",
    "department" = "department.lambda_handler"
  }
}

# Archiving the python files and creating the lambda functions
data "archive_file" "lambda_package" {
  for_each    = local.lambda_functions
  type        = "zip"
  source_file = "../lambda/${each.key}.py"
  output_path = "../lambda/${each.key}.zip"
}

# Creating the lambda functions with the respective handlers and names
resource "aws_lambda_function" "lambda" {
  for_each = local.lambda_functions

  function_name = each.key
  filename      = data.archive_file.lambda_package[each.key].output_path
  handler       = each.value
  runtime       = "python3.12"
  role          = aws_iam_role.lambda_role.arn
}

# Creating the IAM role for the lambda functions so that they can be invoked by the API Gateway
resource "aws_iam_role" "lambda_role" {
  name = "lambda-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# Attaching the AWSLambdaBasicExecutionRole policy to the lambda role
resource "aws_iam_role_policy_attachment" "lambda_basic" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = aws_iam_role.lambda_role.name
}

# Creating the lambda permissions so that the API Gateway can invoke the lambda functions
resource "aws_lambda_permission" "api_gateway_invoke" {
  for_each = local.lambda_functions

  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda[each.key].function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.AttendanceAPI.execution_arn}/*/*/*"
}
