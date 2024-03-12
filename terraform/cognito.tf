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
  supported_identity_providers         = ["COGNITO"]
  callback_urls                        = ["https://d5j4m0w9schy1.cloudfront.net/", "https://d5j4m0w9schy1.cloudfront.net"]
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

# ----------------- Creating the Cognito Identity Pool -----------------

resource "aws_cognito_identity_pool" "main" {
  identity_pool_name               = "Attendance users identity pool"
  allow_unauthenticated_identities = false
  allow_classic_flow               = false

  cognito_identity_providers {
    client_id               = "6pnhs85ctml9b9f353b14ui6b4"
    provider_name           = "cognito-idp.${var.region}.amazonaws.com/eu-central-1_jiDMNCeuM"
    server_side_token_check = false
  }
}

# ----------------- Creating the IAM roles -----------------

resource "aws_iam_role" "student_role" {
  name = "studentRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "cognito-idp.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role" "teacher_role" {
  name = "teacherRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "cognito-idp.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role" "admin_role" {
  name = "adminRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "cognito-idp.amazonaws.com"
        }
      }
    ]
  })
}

# ----------------- Creating the IAM policies -----------------

resource "aws_iam_policy" "student_policy" {
  name        = "studentPolicy"
  description = "Policy for student IAM role"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action   = "execute-api:Invoke",
        Effect   = "Allow",
        Resource = "arn:aws:execute-api:${var.region}:${var.account_id}:${var.api_id}/*/*/student"
      }
    ]
  })
}

resource "aws_iam_policy" "teacher_policy" {
  name        = "teacherPolicy"
  description = "Policy for teacher IAM role"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action   = "execute-api:Invoke",
        Effect   = "Allow",
        Resource = "arn:aws:execute-api:${var.region}:${var.account_id}:${var.api_id}/*/*/teacher"
      }
    ]
  })
}

resource "aws_iam_policy" "admin_policy" {
  name        = "adminPolicy"
  description = "Policy for admin IAM role"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "execute-api:Invoke",
        Effect = "Allow",
        Resource = [
          "arn:aws:execute-api:${var.region}:${var.account_id}:${var.api_id}/*/*/admin",
          "arn:aws:execute-api:${var.region}:${var.account_id}:${var.api_id}/*/*/course",
          "arn:aws:execute-api:${var.region}:${var.account_id}:${var.api_id}/*/*/department"
        ]
      }
    ]
  })
}

# ----------------- Attaching the IAM policies to the appropriate roles -----------------

resource "aws_iam_role_policy_attachment" "student_policy_attachment" {
  role       = aws_iam_role.student_role.name
  policy_arn = "arn:aws:iam::${account_id}:policy/studentPolicy"
}

resource "aws_iam_role_policy_attachment" "teacher_policy_attachment" {
  role       = aws_iam_role.teacher_role.name
  policy_arn = "arn:aws:iam::${account_id}:policy/teacherPolicy"
}

resource "aws_iam_role_policy_attachment" "student_to_teacher_policy_attachment" {
  role       = aws_iam_role.admin_role.name
  policy_arn = "arn:aws:iam::${account_id}:policy/studentPolicy"
}

resource "aws_iam_role_policy_attachment" "admin_policy_attachment" {
  role       = aws_iam_role.admin_role.name
  policy_arn = "arn:aws:iam::${account_id}:policy/adminPolicy"
}

resource "aws_iam_role_policy_attachment" "student_to_admin_policy_attachment" {
  role       = aws_iam_role.admin_role.name
  policy_arn = "arn:aws:iam::${account_id}:policy/studentPolicy"
}

resource "aws_iam_role_policy_attachment" "teacher_to_admin_policy_attachment" {
  role       = aws_iam_role.admin_role.name
  policy_arn = "arn:aws:iam::${account_id}:policy/teacherPolicy"
}

# ----------------- Attaching the IAM policies to the appropriate roles -----------------

# resource "aws_cognito_identity_pool_roles_attachment" "student_role_attachment" {
#   identity_pool_id = aws_cognito_identity_pool.main.id

#   role_mapping {
#     identity_provider         = "graph.facebook.com"
#     ambiguous_role_resolution = "AuthenticatedRole"
#     type                      = "Rules"

#     mapping_rule {
#       claim      = "isAdmin"
#       match_type = "Equals"
#       role_arn   = aws_iam_role.authenticated.arn
#       value      = "paid"
#     }
#   }

#   roles = {
#     "authenticated" = aws_iam_role.authenticated.arn
#   }
# }



# # Cognito User Pool Authorizer
# resource "aws_api_gateway_authorizer" "student_authorizer" {
#   name                            = "CognitoStudentAuthorizer"
#   rest_api_id                     = aws_api_gateway_rest_api.AttendanceAPI.id
#   type                            = "COGNITO_USER_POOLS"
#   identity_source                 = "method.request.header.Authorization"
#   provider_arns                   = [aws_cognito_user_group.students.arn]
# }
