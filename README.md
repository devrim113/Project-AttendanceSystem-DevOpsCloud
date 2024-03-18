# Project Documentation

# Terraform Documentation

## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_archive"></a> [archive](#requirement\_archive) | ~> 2.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | ~> 5.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_archive"></a> [archive](#provider\_archive) | 2.4.2 |
| <a name="provider_aws"></a> [aws](#provider\_aws) | 5.37.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_api_gateway_account.api_gateway_account](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_account) | resource |
| [aws_api_gateway_deployment.deployment_production](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_deployment) | resource |
| [aws_api_gateway_integration.integrations_non_options](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_integration) | resource |
| [aws_api_gateway_integration.integrations_options](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_integration) | resource |
| [aws_api_gateway_integration_response.integration_responses](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_integration_response) | resource |
| [aws_api_gateway_method.methods](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_method) | resource |
| [aws_api_gateway_method_response.responses](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_method_response) | resource |
| [aws_api_gateway_method_settings.method_settings](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_method_settings) | resource |
| [aws_api_gateway_resource.paths](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_resource) | resource |
| [aws_api_gateway_rest_api.AttendanceAPI](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_rest_api) | resource |
| [aws_api_gateway_stage.production_stage](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_stage) | resource |
| [aws_cloudfront_distribution.s3_distribution](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudfront_distribution) | resource |
| [aws_cloudfront_origin_access_identity.origin_access_identity_s3](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudfront_origin_access_identity) | resource |
| [aws_cloudwatch_dashboard.my_dashboard](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_dashboard) | resource |
| [aws_cloudwatch_log_group.api_gateway_access_logs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_group) | resource |
| [aws_cloudwatch_metric_alarm.cloudfront_5xx_errors](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_metric_alarm) | resource |
| [aws_cloudwatch_metric_alarm.cloudfront_5xx_errors_15m](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_metric_alarm) | resource |
| [aws_cognito_user_group.admins](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_user_group) | resource |
| [aws_cognito_user_group.students](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_user_group) | resource |
| [aws_cognito_user_group.teacher](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_user_group) | resource |
| [aws_cognito_user_pool.student_pool](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_user_pool) | resource |
| [aws_cognito_user_pool_client.student_pool_client](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_user_pool_client) | resource |
| [aws_cognito_user_pool_domain.main](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_user_pool_domain) | resource |
| [aws_dynamodb_table.attendance_table](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dynamodb_table) | resource |
| [aws_dynamodb_table.table](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dynamodb_table) | resource |
| [aws_iam_policy.artillery_permissions](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_policy.cognito_signup_lambda_permissions](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_policy.lambda_permissions](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_role.api_gateway_cloudwatch_role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role.artillery_role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role.cognito_signup_lambda_role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role.lambda_role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role_policy.api_gateway_cloudwatch_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy) | resource |
| [aws_iam_role_policy_attachment.artillery_permissions_attach](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_iam_role_policy_attachment.cognitoFullAccess](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_iam_role_policy_attachment.cognito_permissions_attach](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_iam_role_policy_attachment.dynamodb_full_access](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_iam_role_policy_attachment.lambda_basic](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_iam_role_policy_attachment.lambda_permissions_attach](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_lambda_function.cognito_signup](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function) | resource |
| [aws_lambda_function.lambda](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function) | resource |
| [aws_lambda_permission.api_gateway_invoke](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_permission) | resource |
| [aws_lambda_permission.cognito_trigger_permission](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_permission) | resource |
| [aws_s3_bucket.S3_Bucket](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket) | resource |
| [aws_s3_bucket.S3_Bucket_Logs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket) | resource |
| [aws_s3_bucket.bucket](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket) | resource |
| [aws_s3_bucket_acl.b_acl](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_acl) | resource |
| [aws_s3_bucket_logging.b_logging](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_logging) | resource |
| [aws_s3_bucket_logging.b_logging_logs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_logging) | resource |
| [aws_s3_bucket_ownership_controls.S3_Bucket](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_ownership_controls) | resource |
| [aws_s3_bucket_ownership_controls.S3_Bucket_Logs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_ownership_controls) | resource |
| [aws_s3_bucket_policy.bucket_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_policy) | resource |
| [aws_s3_bucket_public_access_block.S3_Bucket](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_public_access_block) | resource |
| [aws_s3_bucket_versioning.bucket](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_versioning) | resource |
| [archive_file.cognito_signup_lambda](https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file) | data source |
| [archive_file.lambda_package](https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_account_id"></a> [account\_id](#input\_account\_id) | AWS account ID | `string` | `"590183910477"` | no |
| <a name="input_attendance_frontend_logs"></a> [attendance\_frontend\_logs](#input\_attendance\_frontend\_logs) | n/a | `string` | `"attendance-frontend-logs"` | no |
| <a name="input_lambda_functions"></a> [lambda\_functions](#input\_lambda\_functions) | Defining the lambda functions and their handlers. | `map(string)` | <pre>{<br>  "admin": "admin.lambda_handler",<br>  "cognito": "cognito.lambda_handler",<br>  "course": "course.lambda_handler",<br>  "department": "department.lambda_handler",<br>  "student": "student.lambda_handler",<br>  "teacher": "teacher.lambda_handler"<br>}</pre> | no |
| <a name="input_region"></a> [region](#input\_region) | AWS region | `string` | `"eu-central-1"` | no |
| <a name="input_s3_name_frontend"></a> [s3\_name\_frontend](#input\_s3\_name\_frontend) | name for S3 bucket front-end | `string` | `"attendance-frontend-bucket"` | no |
| <a name="input_s3_origin_id"></a> [s3\_origin\_id](#input\_s3\_origin\_id) | Defining the s3 origin id for the CloudFront distribution. | `string` | `"s3CodeBucketOrigin"` | no |
| <a name="input_student_pool_name"></a> [student\_pool\_name](#input\_student\_pool\_name) | Name of the student\_pool\_id. | `string` | `"student-attendance-system"` | no |
| <a name="input_to_define_methods"></a> [to\_define\_methods](#input\_to\_define\_methods) | Defining the methods that have to be created for the API Gateway. | `list(string)` | <pre>[<br>  "GET",<br>  "OPTIONS",<br>  "PUT",<br>  "POST",<br>  "DELETE",<br>  "HEAD"<br>]</pre> | no |
| <a name="input_to_define_paths"></a> [to\_define\_paths](#input\_to\_define\_paths) | Defining the paths that have to be created for the API Gateway. | `list(string)` | <pre>[<br>  "admin",<br>  "teacher",<br>  "course",<br>  "department",<br>  "student",<br>  "cognito"<br>]</pre> | no |

## Outputs

No outputs.

# Python Documentation

# tests

* [tests package](tests.md)
  * [Submodules](tests.md#submodules)
  * [tests.conftest module](tests.md#tests-conftest-module)
  * [tests.test_admin module](tests.md#tests-test-admin-module)
  * [tests.test_course module](tests.md#tests-test-course-module)
  * [tests.test_department module](tests.md#tests-test-department-module)
  * [tests.test_student module](tests.md#tests-test-student-module)
  * [tests.test_teacher module](tests.md#tests-test-teacher-module)
  * [Module contents](tests.md#module-tests)
<!-- Attendance System documentation master file, created by
sphinx-quickstart on Wed Feb 28 20:04:13 2024.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->

---

 Contents:

* [tests](modules.md)
  * [tests package](tests.md)
* [lambda_functions package](lambda_functions.md)
  * [Submodules](lambda_functions.md#submodules)
  * [lambda_functions.admin module](lambda_functions.md#module-lambda_functions.admin)
  * [lambda_functions.cognito module](lambda_functions.md#module-lambda_functions.cognito)
  * [lambda_functions.cognito_signup module](lambda_functions.md#module-lambda_functions.cognito_signup)
  * [lambda_functions.course module](lambda_functions.md#module-lambda_functions.course)
  * [lambda_functions.department module](lambda_functions.md#module-lambda_functions.department)
  * [lambda_functions.student module](lambda_functions.md#module-lambda_functions.student)
  * [lambda_functions.teacher module](lambda_functions.md#module-lambda_functions.teacher)
  * [Module contents](lambda_functions.md#module-lambda_functions)
* [tests package](tests.md)
  * [Submodules](tests.md#submodules)
  * [tests.conftest module](tests.md#tests-conftest-module)
  * [tests.test_admin module](tests.md#tests-test-admin-module)
  * [tests.test_course module](tests.md#tests-test-course-module)
  * [tests.test_department module](tests.md#tests-test-department-module)
  * [tests.test_student module](tests.md#tests-test-student-module)
  * [tests.test_teacher module](tests.md#tests-test-teacher-module)
  * [Module contents](tests.md#module-tests)

# Indices and tables

* [Index](genindex.md)
* [Module Index](py-modindex.md)
* [Search Page](search.md)
# lambda_functions package

## Submodules

## lambda_functions.admin module

### lambda_functions.admin.check_permission(token)

### lambda_functions.admin.create_admin_record(item_id, user_name)

Create object for an admin record.

* **Parameters:**
  * **item_id** (*str*) – The ID of the admin record.
  * **user_name** (*str*) – The name of the admin.
* **Returns:**
  The response from the table.put_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while putting the item.

### lambda_functions.admin.decode_jwt(token)

### lambda_functions.admin.delete_admin_record(item_id)

Delete an admin record.

* **Parameters:**
  **item_id** (*str*) – The ID of the admin record.
* **Returns:**
  The response from the table.delete_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while deleting the item.

### lambda_functions.admin.get_admin_record(item_id)

Get an admin record.

* **Parameters:**
  **item_id** (*str*) – The ID of the admin record.
* **Returns:**
  The response from the table.get_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while getting the item.

### lambda_functions.admin.lambda_handler(event, context)

Lambda handler for the admin.
The ‘operation’ field in the event data determines the action to be performed.
The following operations are supported:
- ‘put’: Creates a new record for an admin.
- ‘update’: Updates an admin record.
- ‘delete’: Deletes an admin record.
- ‘get’: Retrieves an admin record.

The corresponding functions called for each operation are:
- ‘put’: create_admin_record()
- ‘update’: update_admin_record()
- ‘delete’: delete_admin_record()
- ‘get’: get_admin_record()

* **Parameters:**
  * **event** (*dict*) – The event object.
  * **context** (*object*) – The context object.
* **Returns:**
  The response object.
* **Return type:**
  dict

### lambda_functions.admin.make_response(status_code, body)

Create a response object for the API Gateway.

* **Parameters:**
  * **status_code** (*int*) – The status code for the response.
  * **body** (*str*) – The body of the response.
* **Returns:**
  The response object.
* **Return type:**
  dict

### lambda_functions.admin.update_admin_record(item_id, user_name)

Update an admin record.

* **Parameters:**
  * **item_id** (*str*) – The ID of the admin record.
  * **user_name** (*str*) – The name of the admin.
* **Returns:**
  The response from the table.update_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while updating the item.

## lambda_functions.cognito module

### lambda_functions.cognito.check_permission(token)

### lambda_functions.cognito.create_admin_record(email, user_name)

Create object for a teacher.

* **Parameters:**
  * **user_id** (*str*) – The ID of the user.
  * **user_name** (*str*) – The name of the user.
* **Returns:**
  The response from the table.put_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while putting the item.

### lambda_functions.cognito.create_student_record(email, user_name)

Create object for a teacher.

* **Parameters:**
  * **email** (*str*) – The email of the user.
  * **user_name** (*str*) – The name of the user.
* **Returns:**
  The response from the table.put_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while putting the item.

### lambda_functions.cognito.create_teacher_record(email, user_name)

Create object for a teacher.

* **Parameters:**
  * **user_id** (*str*) – The ID of the user.
  * **user_name** (*str*) – The name of the user.
* **Returns:**
  The response from the table.put_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while putting the item.

### lambda_functions.cognito.create_user_record(email, user_name, title)

### lambda_functions.cognito.decode_jwt(token)

### lambda_functions.cognito.lambda_handler(event, context)

### lambda_functions.cognito.make_response(status_code, body)

Create a response object for the API Gateway.

* **Parameters:**
  * **status_code** (*int*) – The status code for the response.
  * **body** (*str*) – The body of the response.
* **Returns:**
  The response object.
* **Return type:**
  dict

## lambda_functions.cognito_signup module

### lambda_functions.cognito_signup.lambda_handler(event, context)

## lambda_functions.course module

### lambda_functions.course.check_permission(token)

### lambda_functions.course.create_course(item_id, course_name, department_id, classes)

Create object for a course.

* **Parameters:**
  * **item_id** (*str*) – The ID of the course.
  * **course_name** (*str*) – The name of the course.
  * **department_id** (*str*) – The ID of the department.
  * **classes** (*dict*) – The classes for the course.
* **Returns:**
  The response from the table.put_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while putting the item.

### lambda_functions.course.decode_jwt(token)

### lambda_functions.course.delete_course(item_id)

Delete a course.

* **Parameters:**
  **item_id** (*str*) – The ID of the course.
* **Returns:**
  The response from the table.delete_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while deleting the item.

### lambda_functions.course.get_course(item_id)

Get a course.

* **Parameters:**
  **item_id** (*str*) – The ID of the course.
* **Returns:**
  The course object.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while getting the item.

### lambda_functions.course.lambda_handler(event, context)

Lambda handler function to interact with the DynamoDB table.
The function will perform the operation specified in the ‘func’ query parameter.
The following operations are supported:
- create_course: Create a course.
- get_course: Get a course.
- update_course: Update a course.
- delete_course: Delete a course.

* **Parameters:**
  * **event** (*dict*) – The event object from the Lambda function.
  * **context** (*object*) – The context object from the Lambda function.
* **Returns:**
  The response object for the API Gateway.
* **Return type:**
  dict

### lambda_functions.course.make_response(status_code, body)

Create a response object for the API Gateway.

* **Parameters:**
  * **status_code** (*int*) – The status code for the response.
  * **body** (*str*) – The body of the response.
* **Returns:**
  The response object.
* **Return type:**
  dict

### lambda_functions.course.update_course(item_id, course_name, department_id, classes)

Update object for a course.

* **Parameters:**
  * **item_id** (*str*) – The ID of the course.
  * **course_name** (*str*) – The name of the course.
  * **department_id** (*str*) – The ID of the department.
  * **classes** (*dict*) – The classes for the course.
* **Returns:**
  The response from the table.update_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while updating the item.

## lambda_functions.department module

### lambda_functions.department.check_permission(token)

### lambda_functions.department.create_department(dep_id, dep_name)

Create object for a department.

* **Parameters:**
  * **dep_id** (*str*) – The ID of the department.
  * **dep_name** (*str*) – The name of the department.
* **Returns:**
  The response from the table.put_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while putting the item.

### lambda_functions.department.decode_jwt(token)

### lambda_functions.department.delete_department(dep_id)

Delete a department.

* **Parameters:**
  **dep_id** (*str*) – The ID of the department.
* **Returns:**
  The response from the table.delete_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while deleting the item.

### lambda_functions.department.get_department(dep_id)

Get a department.

* **Parameters:**
  **dep_id** (*str*) – The ID of the department.
* **Returns:**
  The department object.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while getting the item.

### lambda_functions.department.get_department_course_names(dep_id)

Get the course names for a department.

* **Parameters:**
  **dep_id** (*str*) – The ID of the department.
* **Returns:**
  The list of course names for the department.
  : [{‘CourseName’: ‘Mathematics’, ‘ItemId’: 101}, {‘CourseName’: ‘Physics’, ‘ItemId’: 102}]
* **Return type:**
  list
* **Raises:**
  **ClientError** – If an error occurs while querying the items.

### lambda_functions.department.get_department_courses(dep_id)

Get the courses for a department.

* **Parameters:**
  **dep_id** (*str*) – The ID of the department.
* **Returns:**
  The list of courses for the department.
* **Return type:**
  list
* **Raises:**
  **ClientError** – If an error occurs while querying the items.

### lambda_functions.department.lambda_handler(event, context)

Lambda handler for the department.
The ‘operation’ field in the event data determines the action to be performed.
The following operations are supported:
- ‘put’: Creates a new record for a department.
- ‘get’: Retrieves a department.
- ‘update’: Updates a record for a department.
- ‘delete’: Deletes a record for a department.

The corresponding functions called for each operation are:
- ‘put’: create_department()
- ‘get’: get_department()
- ‘update’: update_department()
- ‘delete’: delete_department()

* **Parameters:**
  * **event** (*dict*) – The event object.
  * **context** (*object*) – The context object.
* **Returns:**
  The response object.
* **Return type:**
  dict
* **Raises:**
  **ValueError** – If the operation is not supported.

### lambda_functions.department.make_response(status_code, body)

Create a response object for the API Gateway.

* **Parameters:**
  * **status_code** (*int*) – The status code for the response.
  * **body** (*str*) – The body of the response.
* **Returns:**
  The response object.
* **Return type:**
  dict

### lambda_functions.department.update_department(dep_id, dep_name)

Update object for a department.

* **Parameters:**
  * **dep_id** (*str*) – The ID of the department.
  * **dep_name** (*str*) – The name of the department.
* **Returns:**
  The response from the table.put_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while putting the item.

## lambda_functions.student module

This module contains functions for managing attendance records for students in a DynamoDB table.

Functions:
- create_student_record: Create a student record in the database.
- remove_student_course_attendance: Removes the attendance record of a student for a specific course.
- delete_student_record: Deletes a student record from the table.
- update_student_record: Update the student record in the database.
- update_attendance_record: Update the attendance record for a student.
- get_student: Gets the student record.
- get_student_courses: Retrieves all the courses of a student.
- get_student_course_attendance: Retrieves the attendance record of a student for a specific course.
- lambda_handler: Lambda handler function to interact with the DynamoDB table.

### lambda_functions.student.check_permission(token)

### lambda_functions.student.create_student_record(user_id, user_name)

Create a student record in the database.

* **Parameters:**
  * **user_id** (*str*) – The ID of the student.
  * **course_id** ( *#*) – The ID of the course.
  * **course_name** ( *#*) – The name of the course.
  * **user_name** (*str*) – The name of the student.
* **Returns:**
  The response from the database after creating the student record.
  : If an error occurs, None is returned.
* **Return type:**
  dict

### lambda_functions.student.decode_jwt(token)

### lambda_functions.student.delete_record(item_id, item_type)

Deletes a record from the table using its ItemId.

* **Parameters:**
  **ItemId** (*str*) – The ID of the item.
* **Returns:**
  The response from the delete operation, or None if an error occurred.
* **Return type:**
  dict or None

### lambda_functions.student.enlist_student_course(item_id, user_id, course_id, attendance)

Enlist a student to a course.

* **Parameters:**
  * **user_id** (*str*) – The ID of the student.
  * **course_id** (*str*) – The ID of the course.
* **Returns:**
  The response from the put operation, or None if an error occurred.
* **Return type:**
  dict or None

### lambda_functions.student.get_all_courses()

Retrieves all the courses from the database.
Placed in student.py because of the large frequency in which this function is called.

* **Returns:**
  A list of items containing all the courses.
* **Return type:**
  list

### lambda_functions.student.get_student(user_id)

Retrieves all the attendance records for all courses of a student.

* **Parameters:**
  **user_id** (*str*) – The user ID of the student.
* **Returns:**
  A list of items containing the student’s information.
* **Return type:**
  list
* **Raises:**
  **ClientError** – If an error occurs while querying the table.

### lambda_functions.student.get_student_course_attendance(user_id, course_id)

Retrieves the attendance record of a student for a specific course.

* **Parameters:**
  * **user_id** (*str*) – The ID of the student.
  * **course_id** (*str*) – The ID of the course.
* **Returns:**
  The attendance record of the student for the course, or None if an error occurs.
* **Return type:**
  dict

### lambda_functions.student.get_student_course_names(user_id)

Retrieves the names of all the courses of a student.

* **Parameters:**
  **user_id** (*str*) – The user ID of the student.
* **Returns:**
  A dictionary containing the course names of the student.
  : {course_id: course_name}
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while querying the table.

### lambda_functions.student.get_student_courses(user_id)

Retrieves all the courses of a student.

* **Parameters:**
  **user_id** (*str*) – The user ID of the student.
* **Returns:**
  A list of items containing the student’s information.
* **Return type:**
  list
* **Raises:**
  **ClientError** – If an error occurs while querying the table.

### lambda_functions.student.lambda_handler(event, context)

Lambda handler function to interact with the DynamoDB table.
The ‘operation’ field in the body data determines the action to be performed.
The following operations are supported:
- ‘put’: Creates a new record for a student.
- ‘update’: Updates a student record or attendance record.
- ‘get’: Retrieves all courses for a student or all attendance records for a student’s course.
- ‘delete’: Deletes a record for a student.

The corresponding functions called for each operation are:
- ‘put’: create_student_record() or enlist_student_course()
- ‘update’: update_attendance_record() or update_student_record()
- ‘get’: get_student_course_attendance() or get_student() or get_student_courses()
- ‘delete’: delete_student_record() or remove_student_course_attendance()

* **Parameters:**
  * **body** (*dict*) – The body data passed to the Lambda function.
  * **context** (*object*) – The context object provided by AWS Lambda.
* **Returns:**
  The response containing the statusCode, body, and headers.
* **Return type:**
  dict

### lambda_functions.student.make_response(status_code, body)

Create a response object for the API Gateway.

* **Parameters:**
  * **status_code** (*int*) – The status code for the response.
  * **body** (*str*) – The body of the response.
* **Returns:**
  The response object.
* **Return type:**
  dict

### lambda_functions.student.remove_student_course_attendance(user_id, course_id)

Removes the attendance record of a student for a specific course.

* **Parameters:**
  * **user_id** (*str*) – The ID of the student.
  * **course_id** (*str*) – The ID of the course.
* **Returns:**
  The response from the delete operation, or None if an error occurred.
* **Return type:**
  dict or None

### lambda_functions.student.update_attendance_record(item_id, course_id, attendance)

Update the attendance record for a student in a specific course.
Updates one attendance instance (date) at a time

* **Parameters:**
  * **item_id** (*str*) – The ID of the item. In this case the item is the student’s attendance record for the course.
  * **attendance** (*dict*) – 

    The updated attendance value.
    This is a nested object with the following structure:
    > attendance = {
    > : ‘date’: {
    >   : ‘from’: (str),
    >     ‘to’: (str),
    >     ‘status’: (str)
    >   <br/>
    >   }
* **Returns:**
  The response from the update operation if successful, None otherwise.
* **Return type:**
  dict or None

### lambda_functions.student.update_student_record(user_id, user_name)

Update the student record in the database.

* **Parameters:**
  * **user_id** (*str*) – The ID of the student.
  * **user_name** (*str*) – The name of the student.
* **Returns:**
  The response from the update operation if successful, None otherwise.
* **Return type:**
  dict or None

## lambda_functions.teacher module

This module contains functions for managing attendance records for teachers in a DynamoDB table.

Functions:
- put_attendance_record: Put attendance record for a teacher.
- get_all_courses: Get all courses for a teacher.
- get_all_course_attendance: Get all attendance records of students for a teacher’s course.
- delete_attendance_record: Delete attendance record for a teacher.
- lambda_handler: Lambda handler function to interact with the DynamoDB table.

### lambda_functions.teacher.assign_course_to_teacher(item_id, course_id, user_id)

Assign a course to a teacher.

* **Parameters:**
  * **course_id** (*str*) – The ID of the course.
  * **user_id** (*str*) – The ID of the user.
* **Returns:**
  The response from the table.put_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while putting the item.

### lambda_functions.teacher.check_permission(token)

### lambda_functions.teacher.create_teacher_record(item_id, user_name)

Create object for a teacher.

* **Parameters:**
  * **user_id** (*str*) – The ID of the user.
  * **user_name** (*str*) – The name of the user.
* **Returns:**
  The response from the table.put_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while putting the item.

### lambda_functions.teacher.decode_jwt(token)

### lambda_functions.teacher.delete_teacher(user_id)

Delete teacher’s record.

* **Parameters:**
  **user_id** (*str*) – The ID of the user.
* **Returns:**
  The response from the table.delete_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while deleting the item.

### lambda_functions.teacher.get_all_course_attendance(course_id)

Get all attendance records of students for a teacher’s course.
If the attendance record for a class in the course is not found for a student,
the class is added to the list with no status value and key.
Uses the Global Secondary Index CourseIDUserTypeIndex to query the table.

* **Parameters:**
  **course_id** (*str*) – The ID of the course.
* **Returns:**
  The list of attendance records for the teacher’s course.
* **Return type:**
  list
* **Raises:**
  **ClientError** – If an error occurs while getting the items.

### lambda_functions.teacher.get_teacher(user_id)

Get a teacher.

* **Parameters:**
  **user_id** (*str*) – The ID of the user.
* **Returns:**
  The teacher object.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while getting the item.

### lambda_functions.teacher.get_teacher_course_names(user_id)

Get all course names for a teacher.

* **Parameters:**
  **user_id** (*str*) – The ID of the user.
* **Returns:**
  The list of course names for the teacher.
* **Return type:**
  list
* **Raises:**
  **ClientError** – If an error occurs while getting the items.

### lambda_functions.teacher.get_teacher_courses(user_id)

Get all courses for a teacher.

* **Parameters:**
  **user_id** (*str*) – The ID of the user.
* **Returns:**
  The list of courses for the teacher.
* **Return type:**
  list
* **Raises:**
  **ClientError** – If an error occurs while getting the items.

### lambda_functions.teacher.lambda_handler(event, context)

Lambda handler function to interact with the DynamoDB table.
The ‘operation’ field in the event data determines the action to be performed.
The following operations are supported:
- ‘put’: Creates a new record for a teacher.
- ‘get’: Retrieves all courses for a teacher or all attendance records for a teacher’s course.
- ‘update’: Updates a teacher’s record.
- ‘delete’: Deletes a teacher’s record.

The corresponding functions called for each operation are:
- ‘put’: create_teacher_record()
- ‘get’: get_teacher_courses() or get_all_course_attendance()
- ‘update’: update_teacher_record()
- ‘delete’: delete_teacher()

* **Parameters:**
  * **event** (*dict*) – The event data passed to the Lambda function.
  * **context** (*object*) – The context object provided by AWS Lambda.
* **Returns:**
  The response containing the statusCode, body, and headers.
* **Return type:**
  dict

### lambda_functions.teacher.make_response(status_code, body)

Create a response object for the API Gateway.

* **Parameters:**
  * **status_code** (*int*) – The status code for the response.
  * **body** (*str*) – The body of the response.
* **Returns:**
  The response object.
* **Return type:**
  dict

### lambda_functions.teacher.update_teacher_record(item_id, user_name)

Update object for a teacher.

* **Parameters:**
  * **item_id** (*str*) – The ID of the user.
  * **user_name** (*str*) – The name of the user.
* **Returns:**
  The response from the table.update_item() operation.
* **Return type:**
  dict
* **Raises:**
  **ClientError** – If an error occurs while updating the item.

## Module contents
# tests package

## Submodules

## tests.conftest module

## tests.test_admin module

## tests.test_course module

## tests.test_department module

## tests.test_student module

## tests.test_teacher module

## Module contents

# React Documentation

[attendance-app](README.md) / Modules

# attendance-app

## Table of contents

### Modules

- [admin](modules/admin.md)
- [cognito](modules/cognito.md)
- [course](modules/course.md)
- [student](modules/student.md)
- [teacher](modules/teacher.md)
[attendance-app](../README.md) / [Modules](../modules.md) / teacher

# Module: teacher

## Table of contents

### Functions

- [assign\_course\_to\_teacher](teacher.md#assign_course_to_teacher)
- [get\_all\_course\_attendance](teacher.md#get_all_course_attendance)
- [get\_teacher\_course\_names](teacher.md#get_teacher_course_names)

## Functions

### assign\_course\_to\_teacher

▸ **assign_course_to_teacher**(`ItemId`, `CourseId`, `UserId`): () => `Promise`\<`Response`\>

Assigns a course to a teacher.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ItemId` | `string` | The ID of the item. |
| `CourseId` | `string` | The ID of the course. |
| `UserId` | `string` | The ID of the user. |

#### Returns

`fn`

A Promise that resolves to the result of the API call.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[teacher.ts:57](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/teacher.ts#L57)

___

### get\_all\_course\_attendance

▸ **get_all_course_attendance**(`CourseId`): () => `Promise`\<`Response`\>

Retrieves the attendance data for a specific course.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `CourseId` | `string` | The ID of the course to retrieve attendance data for. |

#### Returns

`fn`

A Promise that resolves to the attendance data for the specified course.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[teacher.ts:76](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/teacher.ts#L76)

___

### get\_teacher\_course\_names

▸ **get_teacher_course_names**(`ItemId`): () => `Promise`\<`Response`\>

Retrieves the course names associated with a teacher.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ItemId` | `string` | The ID of the teacher. |

#### Returns

`fn`

A Promise that resolves to the course names.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[teacher.ts:38](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/teacher.ts#L38)
[attendance-app](../README.md) / [Modules](../modules.md) / course

# Module: course

## Table of contents

### Functions

- [create\_course](course.md#create_course)
- [get\_course](course.md#get_course)
- [update\_course](course.md#update_course)

## Functions

### create\_course

▸ **create_course**(`ItemId`, `CourseName`, `DepartmentId`): () => `Promise`\<`Response`\>

Creates a new course.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ItemId` | `string` | The ID of the course item. |
| `CourseName` | `string` | The name of the course. |
| `DepartmentId` | `string` | The ID of the department the course belongs to. |

#### Returns

`fn`

A promise that resolves to the result of the API call.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[course.ts:38](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/course.ts#L38)

___

### get\_course

▸ **get_course**(`ItemId`): () => `Promise`\<`Response`\>

Retrieves a course based on the provided ItemId.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ItemId` | `string` | The unique identifier of the course. |

#### Returns

`fn`

A Promise that resolves to the course data.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[course.ts:58](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/course.ts#L58)

___

### update\_course

▸ **update_course**(`ItemId`, `CourseName`, `DepartmentId`, `Classes`): () => `Promise`\<`Response`\>

Updates a course with the specified details.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ItemId` | `string` | The ID of the course to update. |
| `CourseName` | `string` | The new name of the course. |
| `DepartmentId` | `string` | The ID of the department the course belongs to. |
| `Classes` | `Object` | An object containing the classes associated with the course. |

#### Returns

`fn`

A Promise that resolves to the updated course.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[course.ts:77](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/course.ts#L77)
[attendance-app](../README.md) / [Modules](../modules.md) / student

# Module: student

## Table of contents

### Functions

- [create\_student](student.md#create_student)
- [enlist\_student\_course](student.md#enlist_student_course)
- [get\_all\_courses](student.md#get_all_courses)
- [get\_student\_course\_attendance](student.md#get_student_course_attendance)
- [get\_student\_course\_names](student.md#get_student_course_names)
- [get\_student\_courses](student.md#get_student_courses)
- [get\_student\_list](student.md#get_student_list)
- [update\_attendance](student.md#update_attendance)

## Functions

### create\_student

▸ **create_student**(`ItemId`, `UserName`, `ItemType`): () => `Promise`\<`Response`\>

Creates a new student.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ItemId` | `string` | The ID of the student item. |
| `UserName` | `string` | The username of the student. |
| `ItemType` | `string` | The type of the student item. |

#### Returns

`fn`

A function that performs a fetch request to create a new student.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[student.ts:40](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/student.ts#L40)

___

### enlist\_student\_course

▸ **enlist_student_course**(`ItemId`, `UserId`, `CourseId`): () => `Promise`\<`Response`\>

Enlists a student in a course.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ItemId` | `string` | The ID of the item. |
| `UserId` | `string` | The ID of the user. |
| `CourseId` | `string` | The ID of the course. |

#### Returns

`fn`

A function that performs a fetch request to enlist a student in a course.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[student.ts:123](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/student.ts#L123)

___

### get\_all\_courses

▸ **get_all_courses**(): () => `Promise`\<`Response`\>

Retrieves all courses.

#### Returns

`fn`

A function that performs a fetch request to get all courses.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[student.ts:106](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/student.ts#L106)

___

### get\_student\_course\_attendance

▸ **get_student_course_attendance**(`UserId`, `CourseId`): () => `Promise`\<`Response`\>

Retrieves the attendance of a student in a specific course.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `UserId` | `string` | The ID of the user. |
| `CourseId` | `string` | The ID of the course. |

#### Returns

`fn`

A function that performs a fetch request to get the student's course attendance.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[student.ts:144](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/student.ts#L144)

___

### get\_student\_course\_names

▸ **get_student_course_names**(`ItemId`): () => `Promise`\<`Response`\>

Retrieves the course names of a specific student.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ItemId` | `string` | The ID of the student. |

#### Returns

`fn`

A function that performs a fetch request to get the student's course names.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[student.ts:91](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/student.ts#L91)

___

### get\_student\_courses

▸ **get_student_courses**(`ItemId`): () => `Promise`\<`Response`\>

Retrieves the courses of a specific student.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ItemId` | `string` | The ID of the student. |

#### Returns

`fn`

A function that performs a fetch request to get the student's courses.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[student.ts:75](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/student.ts#L75)

___

### get\_student\_list

▸ **get_student_list**(`ItemId`): () => `Promise`\<`Response`\>

Retrieves the list of students for a specific item.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ItemId` | `string` | The ID of the item. |

#### Returns

`fn`

A function that performs a fetch request to get the student list.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[student.ts:59](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/student.ts#L59)

___

### update\_attendance

▸ **update_attendance**(`ItemId`, `Attendance`, `courseId`): () => `Promise`\<`Response`\>

Updates the attendance of a student for a specific course.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ItemId` | `string` | The ID of the item. |
| `Attendance` | `AttendanceDateRecord` | The attendance record. |
| `courseId` | `string` | The ID of the course. |

#### Returns

`fn`

A function that performs a fetch request to update the student's attendance.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[student.ts:179](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/student.ts#L179)
[attendance-app](../README.md) / [Modules](../modules.md) / admin

# Module: admin
[attendance-app](../README.md) / [Modules](../modules.md) / cognito

# Module: cognito

## Table of contents

### Functions

- [create\_teacher](cognito.md#create_teacher)

## Functions

### create\_teacher

▸ **create_teacher**(`username`, `email`): () => `Promise`\<`Response`\>

Creates a teacher record in the system.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `username` | `string` | The username of the teacher. |
| `email` | `string` | The email of the teacher. |

#### Returns

`fn`

A Promise that resolves to the result of the API call.

▸ (): `Promise`\<`Response`\>

##### Returns

`Promise`\<`Response`\>

#### Defined in

[cognito.ts:39](https://github.com/devrim113/Project-AttendanceSystem-DevOpsCloud/blob/7af7634/frontend/attendance-app/src/API/cognito.ts#L39)
attendance-app / [Modules](modules.md)

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).
