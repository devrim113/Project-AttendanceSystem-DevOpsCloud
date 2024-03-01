resource "aws_dynamodb_table" "attendance_table" {
  name           = "AllData"
  billing_mode   = "PAY_PER_REQUEST"
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


# resource "aws_dynamodb_table_item" "course1" {
#   table_name = aws_dynamodb_table.table_attendance.name
#   hash_key   = aws_dynamodb_table.table_attendance.hash_key

#   item = <<ITEM
#     {
#       "ItemID": {"S": "C1"},
#       "CourseName": {"S": "DevOps"}
#     }
#   ITEM
# }

# resource "aws_dynamodb_table_item" "course2" {
#   table_name = aws_dynamodb_table.table_attendance.name
#   hash_key   = aws_dynamodb_table.table_attendance.hash_key

#   item = <<ITEM
#     {
#       "ItemID": {"S": "C2"},
#       "CourseName": {"S": "Software Process"}
#     }
#   ITEM
# }

# resource "aws_dynamodb_table_item" "teacher1" {
#   table_name = aws_dynamodb_table.table_attendance.name
#   hash_key   = aws_dynamodb_table.table_attendance.hash_key

#   item = <<ITEM
#     {
#       "ItemID": {"S": "T1"},
#       "UserType": {"S": "Teacher"},
#       "UserName": {"S": "Zhiming Zhao"}
#     }
#   ITEM
# }

# resource "aws_dynamodb_table_item" "teacher2" {
#   table_name = aws_dynamodb_table.table_attendance.name
#   hash_key   = aws_dynamodb_table.table_attendance.hash_key

#   item = <<ITEM
#     {
#       "ItemID": {"S": "T2"},
#       "UserType": {"S": "Teacher"},
#       "UserName": {"S": "Yuri Demchenko"}
#     }
#   ITEM
# }

# resource "aws_dynamodb_table_item" "student1" {
#   table_name = aws_dynamodb_table.table_attendance.name
#   hash_key   = aws_dynamodb_table.table_attendance.hash_key

#   item = <<ITEM
#     {
#       "ItemID": {"S": "S1"},
#       "UserType": {"S": "Student"},
#       "UserName": {"S": "John Doe"}
#     }
#   ITEM
# }

# resource "aws_dynamodb_table_item" "teachercourse1" {
#   table_name = aws_dynamodb_table.table_attendance.name
#   hash_key   = aws_dynamodb_table.table_attendance.hash_key

#   item = <<ITEM
#     {
#       "ItemID": {"S": "E1"},
#       "UserID": {"S": "T1"},
#       "UserType": {"S": "Teacher"},
#       "CourseID": {"S": "C1"}
#     }
#   ITEM
# }

# resource "aws_dynamodb_table_item" "teachercourse2" {
#   table_name = aws_dynamodb_table.table_attendance.name
#   hash_key   = aws_dynamodb_table.table_attendance.hash_key

#   item = <<ITEM
#     {
#       "ItemID": {"S": "E2"},
#       "UserID": {"S": "T2"},
#       "UserType": {"S": "Teacher"},
#       "CourseID": {"S": "C1"}
#     }
#   ITEM
# }

# resource "aws_dynamodb_table_item" "attendance1" {
#   table_name = aws_dynamodb_table.table_attendance.name
#   hash_key   = aws_dynamodb_table.table_attendance.hash_key

#   item = <<ITEM
#     {
#       "ItemID": {"S": "E3"},
#       "UserID": {"S": "S1"},
#       "UserType": {"S": "Student"},
#       "CourseID": {"S": "C1"}
#     }
#   ITEM
# }

# resource "aws_dynamodb_table_item" "attendance2" {
#   table_name = aws_dynamodb_table.table_attendance.name
#   hash_key   = aws_dynamodb_table.table_attendance.hash_key

#   item = <<ITEM
#     {
#       "ItemID": {"S": "E4"},
#       "UserID": {"S": "S1"},
#       "UserType": {"S": "Student"},
#       "CourseID": {"S": "C2"}
#     }
#   ITEM
# }
