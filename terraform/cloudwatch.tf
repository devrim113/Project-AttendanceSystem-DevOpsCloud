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
          ["AWS/APIGateway", "5XXError", "ApiName", "AttendanceAPI", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Invocations", "FunctionName", "student", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Errors", "FunctionName", "student", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Invocations", "FunctionName", "teacher", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Errors", "FunctionName", "teacher", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Invocations", "FunctionName", "admin", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Errors", "FunctionName", "admin", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Invocations", "FunctionName", "course", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Errors", "FunctionName", "course", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Invocations", "FunctionName", "department", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Errors", "FunctionName", "department", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Invocations", "FunctionName", "cognito", { "stat": "Sum", "period": 300 }],
          ["AWS/Lambda", "Errors", "FunctionName", "cognito", { "stat": "Sum", "period": 300 }],
          ["AWS/DynamoDB", "ConsumedReadCapacityUnits", "TableName", "attendance_table", { "stat": "Sum", "period": 300 }],
          ["AWS/DynamoDB", "ConsumedWriteCapacityUnits", "TableName", "attendance_table", { "stat": "Sum", "period": 300 }]
        ],
        "view": "timeSeries",
        "stacked": false,
        "title": "API Gateway Errors and Lambda/DynamoDB Metrics",
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
          ["AWS/CloudFront", "5XXErrorRate", "DistributionId", "s3_distribution", { "stat": "Average", "period": 300 }],
          ["AWS/CloudFront", "5XXErrorRate", "DistributionId", "s3_distribution", { "stat": "Average", "period": 300 }]
        ],
        "view": "timeSeries",
        "stacked": false,
        "title": "CloudFront Error Rates",
        "annotations": {
          "horizontal": [
            {
              "label": "5XX Error Threshold",
              "value": 50
            },
            {
              "label": "5XX Error Threshold",
              "value": 500
            }
          ]
        },
        "region": "eu-central-1"
      }
    }
  ]
}
EOF
}
