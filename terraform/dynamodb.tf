resource "aws_dynamodb_table" "attendance_table" {
  name           = "UserData"
  billing_mode   = "PROVISIONED"
  read_capacity  = 50
  write_capacity = 50
  hash_key       = "UserID"
  range_key      = "CourseID"

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

  # User's attendance on specific date for all courses
  local_secondary_index {
    name            = "UserAttendance"
    projection_type = "ALL"
    range_key       = "Date"
  }

  # Course's attendance on specific date for all students
  global_secondary_index {
    name            = "CourseAttendance"
    hash_key        = "CourseID"
    range_key       = "Date"
    write_capacity  = 50
    read_capacity   = 50
    projection_type = "ALL"
  }

  # To sort teachers from students in course
  global_secondary_index {
    name            = "CourseUsers"
    hash_key        = "CourseID"
    range_key       = "UserType"
    write_capacity  = 50
    read_capacity   = 50
    projection_type = "ALL"
  }

  tags = {
    Name = "dynamodb_table_attendance"
  }
}
