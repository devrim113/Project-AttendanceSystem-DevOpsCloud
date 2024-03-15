/* DynamoDB Table
 * This is the terraform file for the DynamoDB table, the workflow is as follows:
 * 1. Creating the DynamoDB table and the global secondary indexes
*/

# ----------------- Creating the DynamoDB table and the global secondary indexes -----------------

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
