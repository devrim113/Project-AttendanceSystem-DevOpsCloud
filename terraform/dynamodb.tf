resource "aws_dynamodb_table" "attendance_table" {
  name         = "AllData"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "ItemId"
  range_key    = "ItemType"

  global_secondary_index {
    name            = "CourseIdItemTypeIndex"
    hash_key        = "CourseId"
    range_key       = "ItemType"
    projection_type = "ALL"
  }

  global_secondary_index {
    name            = "DepartmentIdItemTypeIndex"
    hash_key        = "DepartmentId"
    range_key       = "ItemType"
    projection_type = "ALL"
  }

  global_secondary_index {
    name            = "UserIdCourseIdIndex"
    hash_key        = "UserId"
    range_key       = "CourseId"
    projection_type = "ALL"
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
    name = "UserId"
    type = "S"
  }

  attribute {
    name = "DepartmentId"
    type = "S"
  }

  attribute {
    name = "CourseId"
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
