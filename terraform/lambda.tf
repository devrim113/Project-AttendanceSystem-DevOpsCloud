/* Lambda
 * This is the terraform file for the Lambda functions, the workflow is as follows:
 * 1. Archiving the python files and creating the lambda functions
 * 2. Creating the IAM role for execution of the lambda functions
*/

# ----------------- Preparing the python file and creating the lambda functions -----------------

# Archiving the python files and creating the lambda functions.
data "archive_file" "lambda_package" {
  for_each    = var.lambda_functions
  type        = "zip"
  source_file = "../lambda_functions/${each.key}.py"
  output_path = "../lambda_functions/${each.key}.zip"
}

# Creating the lambda functions with the respective handlers and names.
resource "aws_lambda_function" "lambda" {
  for_each = var.lambda_functions

  function_name = each.key
  filename      = data.archive_file.lambda_package[each.key].output_path
  handler       = each.value
  runtime       = "python3.12"
  role          = aws_iam_role.lambda_role.arn
}

# ----------------- Creating the IAM role for execution of the lambda functions -----------------

# Creating the IAM role for the lambda functions so that they can be invoked by the API Gateway.
resource "aws_iam_role" "lambda_role" {
  name = "lambdaRole"
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

# Creating the IAM policy for the lambda functions to write to Cognito.
resource "aws_iam_policy" "lambda_permissions" {
  name        = "lambda_permissions"
  description = "Permissions for Lambda to interact with Cognito and other services"

  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Action" : [
          "cognito-idp:AdminCreateUser",
          "cognito-idp:AdminAddUserToGroup",
          "cognito-idp:AdminDeleteUser"
        ],
        "Resource" : "*"
      }
    ]
  })
}

# Add the 'cognito_signup' Lambda function
data "archive_file" "cognito_signup_lambda" {
  type        = "zip"
  source_file = "../lambda_functions/cognito_signup.py"
  output_path = "../lambda_functions/cognito_signup.zip"
}

resource "aws_lambda_function" "cognito_signup" {
  function_name = "cognito_signup"
  filename      = data.archive_file.cognito_signup_lambda.output_path
  handler       = "cognito_signup.lambda_handler"
  runtime       = "python3.12"
  role          = aws_iam_role.lambda_role.arn
}

# Create an IAM role specifically for the Cognito pre-signup Lambda
resource "aws_iam_role" "cognito_signup_lambda_role" {
  name = "cognitoSignupLambdaRole"
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

# IAM policy for Lambda (DynamoDB access and Cognito access)
resource "aws_iam_policy" "cognito_signup_lambda_permissions" {
  name        = "cognitoSignupLambdaPermissions"
  description = "Permissions for the pre-signup Lambda"

  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Action" : [
          "cognito-idp:AdminCreateUser",
          "cognito-idp:AdminAddUserToGroup",
          "cognito-idp:AdminDeleteUser"
        ],
        "Resource" : "*"
      },

    ]
  })
}

# Attach the policy to the Lambda role
resource "aws_iam_role_policy_attachment" "cognito_permissions_attach" {
  policy_arn = aws_iam_policy.cognito_signup_lambda_permissions.arn
  role       = aws_iam_role.cognito_signup_lambda_role.name
}

# Attaching the lambda permissions policy to the lambda role.
resource "aws_iam_role_policy_attachment" "lambda_permissions_attach" {
  policy_arn = aws_iam_policy.lambda_permissions.arn
  role       = aws_iam_role.lambda_role.name
}

# Attaching the AWSLambdaBasicExecutionRole policy to the lambda role.
resource "aws_iam_role_policy_attachment" "lambda_basic" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = aws_iam_role.lambda_role.name
}

# Add adding to cognito to the group.
resource "aws_iam_role_policy_attachment" "cognitoFullAccess" {
  policy_arn = aws_iam_policy.cognito_signup_lambda_permissions.arn
  role       = aws_iam_role.lambda_role.name
}

# Attatching the AmazonDynamoDBFullAccess policy to the lambda role.
resource "aws_iam_role_policy_attachment" "dynamodb_full_access" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess"
  role       = aws_iam_role.lambda_role.name
}

# Creating the lambda permissions so that the API Gateway can invoke the lambda functions.
resource "aws_lambda_permission" "api_gateway_invoke" {
  for_each = var.lambda_functions

  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda[each.key].function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.AttendanceAPI.execution_arn}/*/*/*"
}
