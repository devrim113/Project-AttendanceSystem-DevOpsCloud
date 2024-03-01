resource "aws_dynamodb_table" "attendance_table" {
  name           = "AllData"
  billing_mode   = "PROVISIONED"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "ItemId"
  range_key      = "ItemType"

  global_secondary_index {
    name               = "CourseIDITemTypeIndex"
    hash_key           = "CourseID"
    range_key = "ItemType"
    read_capacity  = 5
    write_capacity = 5
    projection_type    = "ALL"
  }

  global_secondary_index {
    name              = "DepartmentIdItemTypeIndex"
    hash_key          = "DepartmentID"
    range_key = "ItemType"
    read_capacity  = 5
    write_capacity = 5
    projection_type   = "ALL"
  }

  global_secondary_index {
    name              = "UserIdCourseIdIndex"
    hash_key          = "UserID"
    range_key = "CourseID"
    read_capacity  = 5
    write_capacity = 5
    projection_type   = "ALL"
  }

  attribute {
    name = "ItemId"
    type = "S"
  }

  attribute {
    name = "ItemType"
    type = "S"
  }

  attribute {
    name = "UserID"
    type = "S"
  }

  attribute {
    name = "DepartmentID"
    type = "S"
  }

  attribute {
    name = "CourseID"
    type = "S"
  }

  tags = {
    Name = "dynamodb_table_attendance"
  }
}
