resource "aws_iam_policy" "artillery_permissions" {
  name        = "Artillery_permissions"
  description = "Permissions for Artillery to interact with services"

  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid" : "CreateOrGetLambdaRole",
        "Effect" : "Allow",
        "Action" : ["iam:CreateRole", "iam:GetRole", "iam:PassRole"],
        "Resource" : "arn:aws:iam::${var.account_id}:role/artilleryio-default-lambda-role-*"
      },
      {
        "Sid" : "CreateLambdaPolicy",
        "Effect" : "Allow",
        "Action" : ["iam:CreatePolicy", "iam:AttachRolePolicy"],
        "Resource" : "arn:aws:iam::${var.account_id}:policy/artilleryio-lambda-policy"
      },
      {
        "Sid" : "SQSPermissions",
        "Effect" : "Allow",
        "Action" : ["sqs:*"],
        "Resource" : "arn:aws:sqs:*:${var.account_id}:artilleryio*"
      },
      {
        "Sid" : "SQSListQueues",
        "Effect" : "Allow",
        "Action" : ["sqs:ListQueues"],
        "Resource" : "*"
      },
      {
        "Sid" : "LambdaPermissions",
        "Effect" : "Allow",
        "Action" : [
          "lambda:InvokeFunction",
          "lambda:CreateFunction",
          "lambda:DeleteFunction",
          "lambda:GetFunctionConfiguration"
        ],
        "Resource" : "arn:aws:lambda:*:${var.account_id}:function:artilleryio-*"
      },
      {
        "Sid" : "S3Permissions",
        "Effect" : "Allow",
        "Action" : [
          "s3:CreateBucket",
          "s3:DeleteObject",
          "s3:GetObject",
          "s3:PutObject",
          "s3:ListBucket",
          "s3:GetLifecycleConfiguration",
          "s3:PutLifecycleConfiguration"
        ],
        "Resource" : [
          "arn:aws:s3:::artilleryio-test-data-*",
          "arn:aws:s3:::artilleryio-test-data-*/*"
        ]
      }
    ]
  })
}

resource "aws_iam_role" "artillery_role" {
  name = "artilleryRole"
  assume_role_policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid" : "Statement1",
        "Effect" : "Allow",
        "Principal" : {},
        "Action" : "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "artillery_permissions_attach" {
  policy_arn = aws_iam_policy.artillery_permissions.arn
  role       = aws_iam_role.artillery_role.name
}
