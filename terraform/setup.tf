provider "aws" {
    region = "eu-central-1"
}

resource "aws_s3_bucket" "bucket" {
    bucket = "terraform-developmentuva"
}

resource "aws_s3_bucket_versioning" "bucket" {
    bucket = aws_s3_bucket.bucket.bucket
    versioning_configuration {
        status = "Enabled"
    }
}

resource "aws_dynamodb_table" "table" {
    name           = "terraform-developmentuva"
    billing_mode   = "PAY_PER_REQUEST"
    hash_key       = "LockID"
    attribute {
        name = "LockID"
        type = "S"
    }
}

terraform {
    backend "s3" {
        bucket         = "terraform-developmentuva"
        key            = "terraform.tfstate"
        region         = "eu-central-1"
        dynamodb_table = "terraform-developmentuva"
    }
}

