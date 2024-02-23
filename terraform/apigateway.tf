// API Gateway
resource "aws_api_gateway_rest_api" "AttendanceAPI" {
    name        = "AttendanceAPI"
    description = "This is the API for the attendance system."

    endpoint_configuration {
        types = ["REGIONAL"]
    }
}

resource "aws_api_gateway_resource" "student" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    parent_id   = aws_api_gateway_rest_api.AttendanceAPI.root_resource_id
    path_part   = "student"
}

resource "aws_api_gateway_method" "get_student" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.student.id
    http_method   = "GET"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "options_student" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.student.id
    http_method   = "OPTIONS"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "put_student" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.student.id
    http_method   = "PUT"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "post_student" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.student.id
    http_method   = "POST"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_integration" "student_get_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.student.id
    http_method             = aws_api_gateway_method.get_student.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["student"].invoke_arn
}

resource "aws_api_gateway_integration" "student_options_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.student.id
    http_method             = aws_api_gateway_method.options_student.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["student"].invoke_arn
}

resource "aws_api_gateway_integration" "student_put_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.student.id
    http_method             = aws_api_gateway_method.put_student.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["student"].invoke_arn
}

resource "aws_api_gateway_integration" "student_post_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.student.id
    http_method             = aws_api_gateway_method.post_student.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["student"].invoke_arn
}

resource "aws_api_gateway_method_response" "student_get_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.student.id
    http_method = aws_api_gateway_method.get_student.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "student_options_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.student.id
    http_method = aws_api_gateway_method.options_student.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "student_put_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.student.id
    http_method = aws_api_gateway_method.put_student.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "student_post_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.student.id
    http_method = aws_api_gateway_method.post_student.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_integration_response" "student_get_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.student.id
    http_method = aws_api_gateway_method.get_student.http_method
    status_code = aws_api_gateway_method_response.student_get_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.get_student,
        aws_api_gateway_integration.student_get_integration,
    ]
}

resource "aws_api_gateway_integration_response" "student_options_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.student.id
    http_method = aws_api_gateway_method.options_student.http_method
    status_code = aws_api_gateway_method_response.student_options_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.options_student,
        aws_api_gateway_integration.student_options_integration,
    ]
}

resource "aws_api_gateway_integration_response" "student_put_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.student.id
    http_method = aws_api_gateway_method.put_student.http_method
    status_code = aws_api_gateway_method_response.student_put_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.put_student,
        aws_api_gateway_integration.student_put_integration,
    ]
}

resource "aws_api_gateway_integration_response" "student_post_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.student.id
    http_method = aws_api_gateway_method.post_student.http_method
    status_code = aws_api_gateway_method_response.student_post_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.post_student,
        aws_api_gateway_integration.student_post_integration,
    ]
}

resource "aws_api_gateway_resource" "course" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    parent_id   = aws_api_gateway_rest_api.AttendanceAPI.root_resource_id
    path_part   = "course"
}

resource "aws_api_gateway_method" "get_course" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.course.id
    http_method   = "GET"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "options_course" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.course.id
    http_method   = "OPTIONS"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "put_course" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.course.id
    http_method   = "PUT"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "post_course" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.course.id
    http_method   = "POST"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_integration" "course_get_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.course.id
    http_method             = aws_api_gateway_method.get_course.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["course"].invoke_arn
}

resource "aws_api_gateway_integration" "course_options_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.course.id
    http_method             = aws_api_gateway_method.options_course.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["course"].invoke_arn
}

resource "aws_api_gateway_integration" "course_put_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.course.id
    http_method             = aws_api_gateway_method.put_course.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["course"].invoke_arn
}

resource "aws_api_gateway_integration" "course_post_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.course.id
    http_method             = aws_api_gateway_method.post_course.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["course"].invoke_arn
}

resource "aws_api_gateway_method_response" "course_get_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.course.id
    http_method = aws_api_gateway_method.get_course.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "course_options_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.course.id
    http_method = aws_api_gateway_method.options_course.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "course_put_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.course.id
    http_method = aws_api_gateway_method.put_course.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "course_post_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.course.id
    http_method = aws_api_gateway_method.post_course.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_integration_response" "course_get_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.course.id
    http_method = aws_api_gateway_method.get_course.http_method
    status_code = aws_api_gateway_method_response.course_get_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.get_course,
        aws_api_gateway_integration.course_get_integration,
    ]
}

resource "aws_api_gateway_integration_response" "course_options_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.course.id
    http_method = aws_api_gateway_method.options_course.http_method
    status_code = aws_api_gateway_method_response.course_options_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.options_course,
        aws_api_gateway_integration.course_options_integration,
    ]
}

resource "aws_api_gateway_integration_response" "course_put_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.course.id
    http_method = aws_api_gateway_method.put_course.http_method
    status_code = aws_api_gateway_method_response.course_put_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.put_course,
        aws_api_gateway_integration.course_put_integration,
    ]
}

resource "aws_api_gateway_integration_response" "course_post_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.course.id
    http_method = aws_api_gateway_method.post_course.http_method
    status_code = aws_api_gateway_method_response.course_post_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.post_course,
        aws_api_gateway_integration.course_post_integration,
    ]
}

resource "aws_api_gateway_resource" "admin" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    parent_id   = aws_api_gateway_rest_api.AttendanceAPI.root_resource_id
    path_part   = "admin"
}

resource "aws_api_gateway_method" "get_admin" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.admin.id
    http_method   = "GET"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "options_admin" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.admin.id
    http_method   = "OPTIONS"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "put_admin" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.admin.id
    http_method   = "PUT"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "post_admin" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.admin.id
    http_method   = "POST"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_integration" "admin_get_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.admin.id
    http_method             = aws_api_gateway_method.get_admin.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["admin"].invoke_arn
}

resource "aws_api_gateway_integration" "admin_options_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.admin.id
    http_method             = aws_api_gateway_method.options_admin.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["admin"].invoke_arn
}

resource "aws_api_gateway_integration" "admin_put_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.admin.id
    http_method             = aws_api_gateway_method.put_admin.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["admin"].invoke_arn
}

resource "aws_api_gateway_integration" "admin_post_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.admin.id
    http_method             = aws_api_gateway_method.post_admin.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["admin"].invoke_arn
}

resource "aws_api_gateway_method_response" "admin_get_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.admin.id
    http_method = aws_api_gateway_method.get_admin.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "admin_options_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.admin.id
    http_method = aws_api_gateway_method.options_admin.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "admin_put_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.admin.id
    http_method = aws_api_gateway_method.put_admin.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "admin_post_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.admin.id
    http_method = aws_api_gateway_method.post_admin.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_integration_response" "admin_get_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.admin.id
    http_method = aws_api_gateway_method.get_admin.http_method
    status_code = aws_api_gateway_method_response.admin_get_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.get_admin,
        aws_api_gateway_integration.admin_get_integration,
    ]
}

resource "aws_api_gateway_integration_response" "admin_options_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.admin.id
    http_method = aws_api_gateway_method.options_admin.http_method
    status_code = aws_api_gateway_method_response.admin_options_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.options_admin,
        aws_api_gateway_integration.admin_options_integration,
    ]
}

resource "aws_api_gateway_integration_response" "admin_put_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.admin.id
    http_method = aws_api_gateway_method.put_admin.http_method
    status_code = aws_api_gateway_method_response.admin_put_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.put_admin,
        aws_api_gateway_integration.admin_put_integration,
    ]
}

resource "aws_api_gateway_integration_response" "admin_post_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.admin.id
    http_method = aws_api_gateway_method.post_admin.http_method
    status_code = aws_api_gateway_method_response.admin_post_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.post_admin,
        aws_api_gateway_integration.admin_post_integration,
    ]
}

resource "aws_api_gateway_resource" "teacher" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    parent_id   = aws_api_gateway_rest_api.AttendanceAPI.root_resource_id
    path_part   = "teacher"
}

resource "aws_api_gateway_method" "get_teacher" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.teacher.id
    http_method   = "GET"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "options_teacher" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.teacher.id
    http_method   = "OPTIONS"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "put_teacher" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.teacher.id
    http_method   = "PUT"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "post_teacher" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.teacher.id
    http_method   = "POST"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_integration" "teacher_get_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.teacher.id
    http_method             = aws_api_gateway_method.get_teacher.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["teacher"].invoke_arn
}

resource "aws_api_gateway_integration" "teacher_options_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.teacher.id
    http_method             = aws_api_gateway_method.options_teacher.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["teacher"].invoke_arn
}

resource "aws_api_gateway_integration" "teacher_put_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.teacher.id
    http_method             = aws_api_gateway_method.put_teacher.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["teacher"].invoke_arn
}

resource "aws_api_gateway_integration" "teacher_post_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.teacher.id
    http_method             = aws_api_gateway_method.post_teacher.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["teacher"].invoke_arn
}

resource "aws_api_gateway_method_response" "teacher_get_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.teacher.id
    http_method = aws_api_gateway_method.get_teacher.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "teacher_options_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.teacher.id
    http_method = aws_api_gateway_method.options_teacher.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "teacher_put_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.teacher.id
    http_method = aws_api_gateway_method.put_teacher.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "teacher_post_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.teacher.id
    http_method = aws_api_gateway_method.post_teacher.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_integration_response" "teacher_get_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.teacher.id
    http_method = aws_api_gateway_method.get_teacher.http_method
    status_code = aws_api_gateway_method_response.teacher_get_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.get_teacher,
        aws_api_gateway_integration.teacher_get_integration,
    ]
}

resource "aws_api_gateway_integration_response" "teacher_options_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.teacher.id
    http_method = aws_api_gateway_method.options_teacher.http_method
    status_code = aws_api_gateway_method_response.teacher_options_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.options_teacher,
        aws_api_gateway_integration.teacher_options_integration,
    ]
}

resource "aws_api_gateway_integration_response" "teacher_put_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.teacher.id
    http_method = aws_api_gateway_method.put_teacher.http_method
    status_code = aws_api_gateway_method_response.teacher_put_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.put_teacher,
        aws_api_gateway_integration.teacher_put_integration,
    ]
}

resource "aws_api_gateway_integration_response" "teacher_post_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.teacher.id
    http_method = aws_api_gateway_method.post_teacher.http_method
    status_code = aws_api_gateway_method_response.teacher_post_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.post_teacher,
        aws_api_gateway_integration.teacher_post_integration,
    ]
}

resource "aws_api_gateway_resource" "department" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    parent_id   = aws_api_gateway_rest_api.AttendanceAPI.root_resource_id
    path_part   = "department"
}

resource "aws_api_gateway_method" "get_department" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.department.id
    http_method   = "GET"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "options_department" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.department.id
    http_method   = "OPTIONS"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "put_department" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.department.id
    http_method   = "PUT"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_method" "post_department" {
    rest_api_id   = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id   = aws_api_gateway_resource.department.id
    http_method   = "POST"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy" = true
    }
}

resource "aws_api_gateway_integration" "department_get_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.department.id
    http_method             = aws_api_gateway_method.get_department.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["department"].invoke_arn
}

resource "aws_api_gateway_integration" "department_options_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.department.id
    http_method             = aws_api_gateway_method.options_department.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["department"].invoke_arn
}

resource "aws_api_gateway_integration" "department_put_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.department.id
    http_method             = aws_api_gateway_method.put_department.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["department"].invoke_arn
}

resource "aws_api_gateway_integration" "department_post_integration" {
    rest_api_id             = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id             = aws_api_gateway_resource.department.id
    http_method             = aws_api_gateway_method.post_department.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda["department"].invoke_arn
}

resource "aws_api_gateway_method_response" "department_get_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.department.id
    http_method = aws_api_gateway_method.get_department.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "department_options_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.department.id
    http_method = aws_api_gateway_method.options_department.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "department_put_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.department.id
    http_method = aws_api_gateway_method.put_department.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_method_response" "department_post_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.department.id
    http_method = aws_api_gateway_method.post_department.http_method
    status_code = "200"

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin"  = true
    }
}

resource "aws_api_gateway_integration_response" "department_get_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.department.id
    http_method = aws_api_gateway_method.get_department.http_method
    status_code = aws_api_gateway_method_response.department_get_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.get_department,
        aws_api_gateway_integration.department_get_integration,
    ]
}

resource "aws_api_gateway_integration_response" "department_options_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.department.id
    http_method = aws_api_gateway_method.options_department.http_method
    status_code = aws_api_gateway_method_response.department_options_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.options_department,
        aws_api_gateway_integration.department_options_integration,
    ]
}

resource "aws_api_gateway_integration_response" "department_put_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.department.id
    http_method = aws_api_gateway_method.put_department.http_method
    status_code = aws_api_gateway_method_response.department_put_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.put_department,
        aws_api_gateway_integration.department_put_integration,
    ]
}

resource "aws_api_gateway_integration_response" "department_post_integration_response" {
    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    resource_id = aws_api_gateway_resource.department.id
    http_method = aws_api_gateway_method.post_department.http_method
    status_code = aws_api_gateway_method_response.department_post_response.status_code

    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin"  = "'*'"
    }

    depends_on = [
        aws_api_gateway_method.post_department,
        aws_api_gateway_integration.department_post_integration,
    ]
}

resource "aws_api_gateway_deployment" "deployment" {
    depends_on = [
        aws_api_gateway_integration.student_get_integration,
        aws_api_gateway_integration.student_options_integration,
        aws_api_gateway_integration.student_put_integration,
        aws_api_gateway_integration.student_post_integration,
        aws_api_gateway_integration.course_get_integration,
        aws_api_gateway_integration.course_options_integration,
        aws_api_gateway_integration.course_put_integration,
        aws_api_gateway_integration.course_post_integration,
        aws_api_gateway_integration.admin_get_integration,
        aws_api_gateway_integration.admin_options_integration,
        aws_api_gateway_integration.admin_put_integration,
        aws_api_gateway_integration.admin_post_integration,
        aws_api_gateway_integration.teacher_get_integration,
        aws_api_gateway_integration.teacher_options_integration,
        aws_api_gateway_integration.teacher_put_integration,
        aws_api_gateway_integration.teacher_post_integration,
        aws_api_gateway_integration.department_get_integration,
        aws_api_gateway_integration.department_options_integration,
        aws_api_gateway_integration.department_put_integration,
        aws_api_gateway_integration.department_post_integration,
    ]

    rest_api_id = aws_api_gateway_rest_api.AttendanceAPI.id
    stage_name  = "dev"
}

