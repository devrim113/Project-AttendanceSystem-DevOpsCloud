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