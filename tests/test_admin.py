# import pytest
# import json
# import admin
# import student


# @pytest.fixture(scope='function')
# def admin_lambda(dynamodb):
#     return admin.lambda_handler


# @pytest.fixture(scope='function')
# def student_lambda(dynamodb):
#     return student.lambda_handler


# def test_admin_lambda_handler(create_dynamodb_table, admin_lambda, student_lambda):
#     # Create an admin record
#     admin_object = {
#         'ItemId': '1',
#         'ItemType': 'Admin',
#         'UserName': 'John Doe'
#     }

#     create_event = {
#         'operation': 'put',
#         **admin_object
#     }

#     response = admin_lambda(create_event, {})
#     assert response['statusCode'] == 200

#     # Get created record
#     get_event = {
#         'operation': 'get',
#         'ItemId': '1',
#         'ItemType': 'Admin'
#     }
#     response = admin_lambda(get_event, {})
#     assert response['statusCode'] == 200
#     assert json.loads(response['body']) == admin_object

#     # Update admin record
#     updated_admin_object = {
#         'ItemId': '1',
#         'ItemType': 'Admin',
#         'UserName': 'Jane Doe'
#     }

#     update_event = {
#         'operation': 'update',
#         'ItemId': '1',
#         'UserName': 'Jane Doe'
#     }

#     response = admin_lambda(update_event, {})
#     assert response['statusCode'] == 200

#     # Get updated record
#     response = admin_lambda(get_event, {})
#     assert response['statusCode'] == 200
#     assert json.loads(response['body']) == updated_admin_object

#     # Create student record
#     student_object = {
#         'ItemId': '2',
#         'UserName': 'John Doe',
#         'ItemType': 'Student'
#     }
#     create_event = {
#         'operation': 'put',
#         **student_object
#     }
#     response = student_lambda(create_event, {})
#     assert response['statusCode'] == 200

#     # # Change student record to admin record
#     # update_event = {
#     #     'operation': 'update',
#     #     'ItemId': '2',
#     #     'ItemType': 'Admin'
#     # }

#     # response = admin_lambda(update_event, {})
#     # assert response['statusCode'] == 200

#     # # Get created record
#     # response = admin_lambda(get_event, {})
#     # assert response['statusCode'] == 200

#     # student_object['ItemType'] = 'Admin'
#     # assert json.loads(response['body']) == student_object

#     # # Change admin record to teacher record
#     # update_event = {
#     #     'operation': 'update',
#     #     'ItemId': '2',
#     #     'ItemType': 'Teacher'
#     # }

#     # response = admin_lambda(update_event, {})
#     # assert response['statusCode'] == 200
#     # # Get created record
#     # response = admin_lambda(get_event, {})
#     # assert response['statusCode'] == 200
#     # student_object['ItemType'] = 'Teacher'
#     # assert json.loads(response['body']) == student_object

#     # Delete admin record
#     delete_event = {
#         'operation': 'delete',
#         'ItemId': '1',
#         'ItemType': 'Admin'
#     }

#     response = admin_lambda(delete_event, {})
#     assert response['statusCode'] == 200

#     # Verify admin record is deleted
#     response = admin_lambda(get_event, {})
#     assert response['statusCode'] == 400
