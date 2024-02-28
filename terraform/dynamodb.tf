resource "aws_dynamodb_table" "attendance_table" {
  name           = "AllData"
  billing_mode   = "PROVISIONED"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "UserID"
  range_key      = "CourseID"

  global_secondary_index {
    name               = "CourseIDUserTypeIndex"
    hash_key           = "CourseID"
    range_key = "UserType"
    read_capacity  = 5
    write_capacity = 5
    projection_type    = "ALL"
  }

  attribute {
    name = "UserID"
    type = "S"
  }

  attribute {
    name = "CourseID"
    type = "S"
  }

  attribute {
    name = "UserType"
    type = "S"
  }

  tags = {
    Name = "dynamodb_table_attendance"
  }
}
