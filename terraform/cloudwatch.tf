/* Cloudwatch
 * This is the terraform file for the cloudwatch dashboard, the workflow is as follows:
 * 1. Creating the cloudwatch dashboard
*/

# ----------------- Creating the cloudwatch dashboard -----------------

resource "aws_cloudwatch_dashboard" "my_dashboard" {
  dashboard_name = "CloudWatch-Default"

  dashboard_body = <<EOF
{
  "widgets": [
    {
      "type": "metric",
      "x": 0,
      "y": 0,
      "width": 12,
      "height": 6,
      "properties": {
        "metrics": [
          ["AWS/APIGateway", "Invocations", "ApiName", "AttendanceAPI", { "stat": "Sum", "period": 300 }],
          ["AWS/APIGateway", "4XXError", "ApiName", "AttendanceAPI", { "stat": "Sum", "period": 300 }],
          ["AWS/APIGateway", "5XXError", "ApiName", "AttendanceAPI", { "stat": "Sum", "period": 300 }]
        ],
        "view": "timeSeries",
        "stacked": false,
        "title": "API Gateway Errors",
        "region": "eu-central-1"
      }
    },
    {
      "type": "metric",
      "x": 12,
      "y": 0,
      "width": 12,
      "height": 6,
      "properties": {
        "metrics": [
          ["AWS/Lambda", "Invocations", "FunctionName", "student", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Errors", "FunctionName", "student", { "stat": "Sum", "period": 300 }]
        ],
        "view": "timeSeries",
        "stacked": false,
        "title": "Lambda Student metrics",
        "region": "eu-central-1"
      }
    },
    {
      "type": "metric",
      "x": 0,
      "y": 6,
      "width": 12,
      "height": 6,
      "properties": {
        "metrics": [
          ["AWS/Lambda", "Invocations", "FunctionName", "teacher", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Errors", "FunctionName", "teacher", { "stat": "Sum", "period": 300 }]
        ],
        "view": "timeSeries",
        "stacked": false,
        "title": "Lambda Teacher metrics",
        "region": "eu-central-1"
      }
    },
    {
      "type": "metric",
      "x": 12,
      "y": 6,
      "width": 12,
      "height": 6,
      "properties": {
        "metrics": [
          ["AWS/Lambda", "Invocations", "FunctionName", "admin", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Errors", "FunctionName", "admin", { "stat": "Sum", "period": 300 }]
        ],
        "view": "timeSeries",
        "stacked": false,
        "title": "Lambda Admin metrics",
        "region": "eu-central-1"
      }
    },
    {
      "type": "metric",
      "x": 0,
      "y": 12,
      "width": 12,
      "height": 6,
      "properties": {
        "metrics": [
          ["AWS/Lambda", "Invocations", "FunctionName", "course", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Errors", "FunctionName", "course", { "stat": "Sum", "period": 300 }]
        ],
        "view": "timeSeries",
        "stacked": false,
        "title": "Lambda Course metrics",
        "region": "eu-central-1"
      }
    },
    {
      "type": "metric",
      "x": 12,
      "y": 12,
      "width": 12,
      "height": 6,
      "properties": {
        "metrics": [
          ["AWS/Lambda", "Invocations", "FunctionName", "department", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Errors", "FunctionName", "department", { "stat": "Sum", "period": 300 }]
        ],
        "view": "timeSeries",
        "stacked": false,
        "title": "Lambda Department metrics",
        "region": "eu-central-1"
      }
    },
    {
      "type": "metric",
      "x": 0,
      "y": 18,
      "width": 12,
      "height": 6,
      "properties": {
        "metrics": [
          ["AWS/Lambda", "Invocations", "FunctionName", "cognito", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Errors", "FunctionName", "cognito", { "stat": "Sum", "period": 300 }]
        ],
        "view": "timeSeries",
        "stacked": false,
        "title": "Lambda Cognito metrics",
        "region": "eu-central-1"
      }
    },
    {
      "type": "metric",
      "x": 12,
      "y": 6,
      "width": 12,
      "height": 6,
      "properties": {
        "metrics": [
          [ "AWS/CloudFront", "Requests", "Region", "Global", "DistributionId", "${aws_cloudfront_distribution.s3_distribution.id}", { "stat": "Sum", "period": 300 } ]
        ],
        "view": "timeSeries",
        "stacked": false,
        "title": "Cloudfront requests",
        "region": "eu-central-1"
      }
    },
    {
      "type": "metric",
      "x": 12,
      "y": 18,
      "width": 12,
      "height": 6,
      "properties": {
        "metrics": [
          ["AWS/DynamoDB", "ConsumedReadCapacityUnits", "TableName", "attendance_table", { "stat": "Sum", "period": 300 }],
          ["AWS/DynamoDB", "ConsumedWriteCapacityUnits", "TableName", "attendance_table", { "stat": "Sum", "period": 300 }]
        ],
        "view": "timeSeries",
        "stacked": false,
        "title": "DynamoDB metrics",
        "region": "eu-central-1"
      }
    }
  ]
}
EOF
}
