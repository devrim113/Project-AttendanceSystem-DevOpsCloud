/* Frontend
 * This is the terraform file for the frontend, the workflow is as follows:
 * 1. Creating the S3 bucket where the frontend code will be stored.
 * 2. Creating the S3 bucket where the logs will be stored.
 * 3. Creating the CloudFront distribution for the frontend.
 * 4. Creating alarms for too many 500 errors in the CloudFront distribution.
*/

# ----------------- Creating the S3 bucket where the frontend code will be stored -----------------

# Creating the S3 bucket where the frontend code will be stored.
resource "aws_s3_bucket" "S3_Bucket" {
  bucket = var.s3_name_frontend

  tags = {
    Name = "The code bucket"
  }
}

# Changing the ownership of the objects in the bucket to the bucket owner.
resource "aws_s3_bucket_ownership_controls" "S3_Bucket" {
  bucket = aws_s3_bucket.S3_Bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

# Enabling the public access block for the bucket.
resource "aws_s3_bucket_public_access_block" "S3_Bucket" {
  bucket = aws_s3_bucket.S3_Bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

# Adding the bucket policy to the bucket to allow the CloudFront to access the objects in the bucket.
resource "aws_s3_bucket_acl" "b_acl" {
  bucket = aws_s3_bucket.S3_Bucket.id
  acl    = "public-read"
}

# Enabling the logging for the bucket.
resource "aws_s3_bucket_logging" "b_logging" {
  bucket        = aws_s3_bucket.S3_Bucket.id
  target_bucket = aws_s3_bucket.S3_Bucket_Logs.id
  target_prefix = "frontend_bucket_logs/"
}

# ----------------- Creating the S3 bucket where the logs will be stored -----------------

# Creating the S3 bucket where the logs will be stored.
resource "aws_s3_bucket" "S3_Bucket_Logs" {
  bucket = var.attendance_frontend_logs
  tags = {
    Name = "The logs bucket"
  }
}

# Changing the ownership of the objects in the bucket to the bucket owner.
resource "aws_s3_bucket_ownership_controls" "S3_Bucket_Logs" {
  bucket = aws_s3_bucket.S3_Bucket_Logs.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

# Enabling the logging for the bucket.
resource "aws_s3_bucket_logging" "b_logging_logs" {
  bucket        = aws_s3_bucket.S3_Bucket_Logs.id
  target_bucket = aws_s3_bucket.S3_Bucket_Logs.id
  target_prefix = "logs_bucket_logs/"
}

# ----------------- Creating the CloudFront distribution for the frontend -----------------

# Creating the origin access identity for the S3 bucket.
resource "aws_cloudfront_origin_access_identity" "origin_access_identity_s3" {
  comment = "Let the cloudfront access the S3"
}

# Adding the bucket policy to the bucket to allow the CloudFront to access the objects in the bucket.
resource "aws_s3_bucket_policy" "bucket_policy" {
  bucket = aws_s3_bucket.S3_Bucket.id
  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCloudFrontAccesstoBucket",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity ${aws_cloudfront_origin_access_identity.origin_access_identity_s3.id}"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::${aws_s3_bucket.S3_Bucket.id}/*"
    }
  ]
}
POLICY
}

# Creating the CloudFront distribution for the frontend.
resource "aws_cloudfront_distribution" "s3_distribution" {
  origin {
    domain_name = aws_s3_bucket.S3_Bucket.bucket_regional_domain_name
    origin_id   = var.s3_origin_id
    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.origin_access_identity_s3.cloudfront_access_identity_path
    }
  }

  enabled             = true
  is_ipv6_enabled     = true
  default_root_object = "index.html"

  # Adding the logging configuration to the CloudFront distribution.
  logging_config {
    include_cookies = false
    bucket          = aws_s3_bucket.S3_Bucket_Logs.bucket_regional_domain_name
    prefix          = "frontend_cloudfront_logs/"
  }

  # Adding the default cache behavior to the CloudFront distribution.
  default_cache_behavior {
    allowed_methods  = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = var.s3_origin_id

    forwarded_values {
      query_string = false
      headers      = ["Authorization", "Origin"]

      cookies {
        forward = "none"
      }
    }

    # Adding the viewer protocol policy to the CloudFront distribution, so that the traffic is redirected to HTTPS.
    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 3600
    max_ttl                = 86400
  }

  # Adding the restrictions to the CloudFront distribution, only accessed from NL.
  restrictions {
    geo_restriction {
      restriction_type = "whitelist"
      locations        = ["NL"]
    }
  }

  # Adding the viewer certificate to the CloudFront distribution, so that the traffic is encrypted.
  viewer_certificate {
    cloudfront_default_certificate = true
  }

  # Added a custom errror response to redirect the 404 errors to the index.html page.
  custom_error_response {
    error_code         = 404
    response_code      = 200
    response_page_path = "/index.html"
  }
}

# ----------------- Creating alarms for too many 500 errors in the CloudFront distribution -----------------

# Creating the alarm for the 5xx error rate for the CloudFront distribution.
# This alarm will be triggered if the 5xx error rate is greater than 50 over 1 minute.
resource "aws_cloudwatch_metric_alarm" "cloudfront_5xx_errors" {
  alarm_name                = "cloudfront-5xx-error-rate-high"
  comparison_operator       = "GreaterThanThreshold"
  evaluation_periods        = "1"
  metric_name               = "5xxErrorRate"
  namespace                 = "AWS/CloudFront"
  period                    = "60" // In seconds
  statistic                 = "Sum"
  threshold                 = "50"
  alarm_description         = "This metric monitors 5xx error rate for CloudFront"
  actions_enabled           = true
  insufficient_data_actions = []

  dimensions = {
    DistributionId = aws_cloudfront_distribution.s3_distribution.id
    Region         = "Global"
  }
}

# Creating the alarm for the 5xx error rate over 15 minutes for the CloudFront distribution.
# This alarm will be triggered if the 5xx error rate is greater than 500 over 15 minutes.
resource "aws_cloudwatch_metric_alarm" "cloudfront_5xx_errors_15m" {
  alarm_name                = "cloudfront-5xx-error-rate-high-15m"
  comparison_operator       = "GreaterThanThreshold"
  evaluation_periods        = "15"
  metric_name               = "5xxErrorRate"
  namespace                 = "AWS/CloudFront"
  period                    = "60" // In seconds
  statistic                 = "Sum"
  threshold                 = "500"
  alarm_description         = "This metric monitors 5xx error rate over 15 minutes for CloudFront"
  actions_enabled           = true
  insufficient_data_actions = []

  dimensions = {
    DistributionId = aws_cloudfront_distribution.s3_distribution.id
    Region         = "Global"
  }
}
