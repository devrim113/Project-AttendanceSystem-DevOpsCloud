resource "aws_dynamodb_table" "attendance_table" {
  name           = "AllData"
  billing_mode   = "PROVISIONED"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "CourseUserDate"
  range_key      = "CourseID"

  attribute {
    name = "CourseUserDate"
    type = "S"
  }

  attribute {
    name = "UserID"
    type = "S"
  }

  attribute {
    name = "UserType"
    type = "S"
  }

  attribute {
    name = "CourseID"
    type = "S"
  }

  attribute {
    name = "Date"
    type = "S"
  }

  local_secondary_index {
    name            = "UserData"
    projection_type = "ALL"
    range_key       = "UserID"
  }

  # Attendance on specific date for all courses
  local_secondary_index {
    name            = "Attendance"
    projection_type = "ALL"
    range_key       = "Date"
  }

  local_secondary_index {
    name            = "UserData"
    projection_type = "ALL"
    range_key       = "UserType"
  }


  # Course's attendance on specific date for all students
  global_secondary_index {
    name            = "CourseDate"
    hash_key        = "CourseID"
    range_key       = "Date"
    write_capacity  = 5
    read_capacity   = 5
    projection_type = "ALL"
  }

  # To sort teachers from students in course
  global_secondary_index {
    name               = "CourseUsers"
    hash_key           = "CourseID"
    range_key          = "UserType"
    write_capacity     = 5
    read_capacity      = 5
    projection_type    = "INCLUDE"
    non_key_attributes = ["UserID"]
  }

  # User's attendance for specific course
  global_secondary_index {
    name            = "UserCourse"
    hash_key        = "UserID"
    range_key       = "CourseID"
    write_capacity  = 5
    read_capacity   = 5
    projection_type = "ALL"
  }

  tags = {
    Name = "dynamodb_table_attendance"
  }
}
