resource "aws_dynamodb_table" "attendance_table" {
  name           = "SchoolData"
  billing_mode   = "PROVISIONED"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "CourseID"
  # range_key      = "UserID"

  attribute {
    name = "UserID"
    type = "S"
  }

  # attribute {
  #   name = "UserType"
  #   type = "S"
  # }

  # attribute {
  #   name = "UserName"
  #   type = "S"
  # }

  attribute {
    name = "CourseID"
    type = "S"
  }

  # attribute {
  #   name = "CourseName"
  #   type = "S"
  # }

  attribute {
    name = "Date"
    type = "S"
  }

  # attribute {
  #   name = "Present"
  #   type = "B"
  # }

  # View a student's course attendance
  local_secondary_index {
    name               = "CourseUsers"
    range_key          = "UserID"
    projection_type    = "INCLUDE"
    non_key_attributes = ["Date", "Present"]
  }

  # View user information of every user in course
  local_secondary_index {
    name               = "CourseUsers"
    range_key          = "UserType"
    projection_type    = "INCLUDE"
    non_key_attributes = ["UserID", "UserName"]
  }

  # Attendance on specific date for a course
  local_secondary_index {
    name               = "CourseAttendance"
    range_key          = "Date"
    projection_type    = "INCLUDE"
    non_key_attributes = ["UserID", "UserType", "UserName", "Present"]
  }

  # View a student's information
  global_secondary_index {
    name               = "UserData"
    hash_key           = "UserID"
    write_capacity     = 5
    read_capacity      = 5
    projection_type    = "INCLUDE"
    non_key_attributes = ["UserName", "UserType", "CourseID"]
  }

  tags = {
    Name = "dynamodb_table_attendance"
  }
}
