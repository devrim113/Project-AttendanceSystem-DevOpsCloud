variable "region" {
  description = "AWS region"
  type        = string
  default     = "eu-central-1"
}

variable "account_id" {
  description = "AWS account ID"
  type        = string
  default     = "590183910477"
}

variable "cognito_identity_client_provider" {
  description = "Cognito identity provider client"
  type        = string
  default     = "cognito-idp.${var.region}.amazonaws.com/${aws_cognito_user_pool.student_pool.id}"
}
