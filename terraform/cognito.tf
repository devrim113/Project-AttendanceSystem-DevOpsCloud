# Cognito User Pool
resource "aws_cognito_user_pool" "student_pool" {
  name                     = "student-login"
  username_attributes      = ["email"]
  auto_verified_attributes = ["email"]

  schema {
    name                = "email"
    attribute_data_type = "String"
    mutable             = true
    required            = true
    string_attribute_constraints {
      min_length = 2
      max_length = 254
    }
  }
  schema {
    name                = "name"
    attribute_data_type = "String"
    mutable             = true
    required            = true
    string_attribute_constraints {
      min_length = 0
      max_length = 256
    }
  }

  # admin_create_user_config {
  #     allow_admin_create_user_only = true
  # }

  password_policy {
    minimum_length                   = 8
    require_lowercase                = true
    require_numbers                  = true
    require_symbols                  = true
    require_uppercase                = true
    temporary_password_validity_days = 3
  }

  mfa_configuration = "OFF"
}

# Cognito User Pool Client
resource "aws_cognito_user_pool_client" "student_pool_client" {
  name                                 = "website-static"
  user_pool_id                         = aws_cognito_user_pool.student_pool.id
  generate_secret                      = false
  allowed_oauth_flows                  = ["code", "implicit"] # Modify based on needs
  allowed_oauth_flows_user_pool_client = true
  allowed_oauth_scopes                 = ["email", "profile", "openid"]
  callback_urls                        = ["https://d5j4m0w9schy1.cloudfront.net/"]
}

resource "aws_cognito_user_pool_domain" "main" {
  domain       = "student-attendance-system"
  user_pool_id = aws_cognito_user_pool.student_pool.id
}


# Generate user group
resource "aws_cognito_user_group" "students" {
  name         = "Students"
  user_pool_id = aws_cognito_user_pool.student_pool.id
  description  = "A group for student users"
}

# Generate admin group
resource "aws_cognito_user_group" "admins" {
  name         = "Admins"
  user_pool_id = aws_cognito_user_pool.student_pool.id
  description  = "A group for admin users"
}

# Generate teacher group
resource "aws_cognito_user_group" "teacher" {
  name         = "Teachers"
  user_pool_id = aws_cognito_user_pool.student_pool.id
  description  = "A group for teachers users"
}



# # Cognito User Pool Authorizer
# resource "aws_api_gateway_authorizer" "student_authorizer" {
#   name                            = "CognitoStudentAuthorizer"
#   rest_api_id                     = aws_api_gateway_rest_api.AttendanceAPI.id
#   type                            = "COGNITO_USER_POOLS"
#   identity_source                 = "method.request.header.Authorization"
#   provider_arns                   = [aws_cognito_user_group.students.arn]
# }
