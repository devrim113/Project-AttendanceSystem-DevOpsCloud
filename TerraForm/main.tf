# terraform {
#   required_providers {
#     aws = {
#       source  = "hashicorp/aws"
#       version = "~> 5.0"
#     }
#   }

#   required_version = ">= 1.2.0"
# }

# provider "aws" {
#   region  = ""
#   access_key = "my-access-key"
#   secret_key = "my-secret-key"

# }

# resource "aws_instance" "app_server" {
#   ami           = "ami-830c94e3"
#   instance_type = "t2.micro"

#   tags = {
#     Name = "ExampleAppServerInstance"
#   }
# }

# resource "aws_dynamodb_table" "basic-dynamodb-table" {
#   name           = "GameScores"
#   billing_mode   = "PROVISIONED"
#   read_capacity  = 20
#   write_capacity = 20
#   hash_key       = "UserId"
#   range_key      = "GameTitle"

#   attribute {
#     name = "UserId"
#     type = "S"
#   }

#   attribute {
#     name = "GameTitle"
#     type = "S"
#   }

#   attribute {
#     name = "TopScore"
#     type = "N"
#   }

#   ttl {
#     attribute_name = "TimeToExist"
#     enabled        = false
#   }

#   global_secondary_index {
#     name               = "GameTitleIndex"
#     hash_key           = "GameTitle"
#     range_key          = "TopScore"
#     write_capacity     = 10
#     read_capacity      = 10
#     projection_type    = "INCLUDE"
#     non_key_attributes = ["UserId"]
#   }

#   tags = {
#     Name        = "dynamodb-table-1"
#     Environment = "production"
#   }
# }


terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.37.0"
    }
  }
}


provider "aws" {
  # Dit gebruiken om te testen, maar in productie .env met de namen die nu in "..." staan. 
  # dan vervangen door. Source: https://registry.terraform.io/providers/hashicorp/aws/latest/docs#example-usage
  # provider "aws" {} 
  region  = "AWS_REGION" #eu-west-2
  access_key = "AWS_ACCESS_KEY_ID" 
  secret_key = "asecretkey"
}

resource "aws_dynamodb_table" "students-list" {
    name = "students"
    hash_key = "id"

    attribute {
        name = "id"
        type = "N"
    }
    attribute {
        name = "first-name"
        type = "S"
    }
    attribute {
        name = "last-name"
        type = "S"
    }
}
resource "aws_dynamodb_table" "teachers-list" {
    name = "teachers"
    hash_key = "id"

    attribute {
        name = "id"
        type = "N"
    }
    attribute {
        name = "first-name"
        type = "S"
    }
    attribute {
        name = "last-name"
        type = "S"
    }
}
resource "aws_dynamodb_table" "teachers-list" {
    name = "teachers"
    hash_key = "id"

    attribute {
        name = "id"
        type = "N"
    }
    attribute {
        name = "first-name"
        type = "S"
    }
    attribute {
        name = "last-name"
        type = "S"
    }
}