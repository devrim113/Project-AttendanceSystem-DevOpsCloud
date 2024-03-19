
# Specify the region where we want to deploy the infrastructure.
variable "region" {
  description = "AWS region"
  type        = string
  default     = "eu-central-1"
}

# Specify the AWS account ID to access the resources.
variable "account_id" {
  description = "AWS account ID"
  type        = string
  default     = "590183910477"
}

# Defining the paths that have to be created for the API Gateway.
variable "to_define_paths" {
  type    = list(string)
  default = ["admin", "teacher", "course", "department", "student", "cognito"]
}

# Defining the methods that have to be created for the API Gateway.
variable "to_define_methods" {
  type    = list(string)
  default = ["GET", "OPTIONS", "PUT", "POST", "DELETE", "HEAD"]
}

# Defining the lambda functions and their handlers.
variable "lambda_functions" {
  type = map(string)
  default = {
    "student"    = "student.lambda_handler",
    "admin"      = "admin.lambda_handler",
    "teacher"    = "teacher.lambda_handler",
    "course"     = "course.lambda_handler",
    "department" = "department.lambda_handler",
    "cognito"    = "cognito.lambda_handler",
    # "cognito_signup" = "cognito_signup.lambda_handler",
  }
}

# Defining the s3 origin id for the CloudFront distribution.
variable "s3_origin_id" {
  type    = string
  default = "s3CodeBucketOrigin"
}

# Name of the student_pool_id.
variable "student_pool_name" {
  type    = string
  default = "student-attendance-system"
}

# name for S3 bucket front-end
variable "s3_name_frontend" {
  type    = string
  default = "attendance-frontend-bucket"
}

variable "attendance_frontend_logs" {
  type    = string
  default = "attendance-frontend-logs"
}