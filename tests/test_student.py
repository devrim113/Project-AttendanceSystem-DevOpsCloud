import pytest
import json
from moto import mock_aws
import student
from student import table

@pytest.fixture(scope='function')
def student_lambda(dynamodb):
    return student.lambda_handler

def test_student_record_lifecycle(create_dynamodb_table, student_lambda):
    # Create record
    object = {
        'UserId': '1',
        'CourseId': '101',
        'CourseName': 'Math',
        'Date': '2022-01-01',
        'Present': True,
        'UserName': 'John Doe'
    }
    create_event = {
        'operation': 'put',
        **object
    }
    response = student_lambda(create_event, {})
    assert response['statusCode'] == 200

    # Get created record
    get_event = {
        'operation': 'get',
        'UserId': '1',
        'CourseId': '101',
        'Date': '2022-01-01'
    }
    response = student_lambda(get_event, {})
    assert response['statusCode'] == 200
    retrieved_object = json.loads(response['body'])

    for key in object:
        assert object[key] == retrieved_object[key], f"Value mismatch for {key}: expected {object[key]}, got {object[key]}"

    # Delete created record
    delete_event = {
        'operation': 'delete',
        'UserId': '1',
        'CourseId': '101',
        'Date': '2022-01-01'
    }
    response = student_lambda(delete_event, {})
    assert response['statusCode'] == 200

    # Verify deletion
    response = student_lambda(get_event, {})
    assert response['statusCode'] == 404
