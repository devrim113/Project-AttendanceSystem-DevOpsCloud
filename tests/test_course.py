import json
import pytest
import course


@pytest.fixture(scope='function')
def course_lambda(dynamodb):
    return course.lambda_handler


def test_admin_lambda_handler(create_dynamodb_table, course_lambda):
    """
    Test course lambda handler
    """
    # Create a course record
    course_object = {
        'ItemId': '1',
        'CourseName': 'Math',
        'ItemType': 'Course',
        'DepartmentId': '1',
        'Classes': {
            '2022-01-01': {
                'from': '09:00',
                'to': '12:00'
            },
            '2022-01-02': {
                'from': '09:00',
                'to': '12:00'
            }
        }
    }

    create_event = {
        'path': '/course',
        'httpMethod': 'PUT',
        'headers': {
            "Authorization": "PYTEST_CODE"
        },
        'pathParameters': {},
        'queryStringParameters': {'func': 'create_course'},
        'body': {
            **course_object
        },
        'isBase64Encoded': False
    }

    response = course_lambda(create_event, {})
    assert response['statusCode'] == 200

    # Get created record
    get_event = {
        'path': '/course',
        'httpMethod': 'GET',
        'headers': {
            "Authorization": "PYTEST_CODE"
        },
        'pathParameters': {},
        'queryStringParameters': {'func': 'get_course', 'ItemId': '1'},
        'body': None,
        'isBase64Encoded': False
    }
    response = course_lambda(get_event, {})
    assert response['statusCode'] == 200

    retrieved_object = json.loads(response['body'])
    assert course_object == retrieved_object

    # Update course record
    updated_course_object = {
        'ItemId': '1',
        'ItemType': 'Course',
        'CourseName': 'Mathematics',
        'DepartmentId': '1',
        'Classes': {
            '2022-01-01': {
                'from': '09:00',
                'to': '12:00'
            }
        }
    }

    update_event = {
        'path': '/course',
        'httpMethod': 'PUT',
        'headers': {
            "Authorization": "PYTEST_CODE"
        },
        'pathParameters': {},
        'queryStringParameters': {'func': 'update_course'},
        'body': {
            **updated_course_object
        },
        'isBase64Encoded': False
    }

    response = course_lambda(update_event, {})
    assert response['statusCode'] == 200

    # Get updated record
    response = course_lambda(get_event, {})
    assert response['statusCode'] == 200
    assert updated_course_object == json.loads(response['body'])

    # Delete course record
    delete_event = {
        'path': '/course',
        'httpMethod': 'DELETE',
        'headers': {
            "Authorization": "PYTEST_CODE"
        },
        'pathParameters': {},
        'queryStringParameters': {'func': 'delete_course', 'ItemId': '1'},
        'body': None,
        'isBase64Encoded': False
    }

    response = course_lambda(delete_event, {})
    assert response['statusCode'] == 200

    # Get deleted record
    response = course_lambda(get_event, {})
    assert response['statusCode'] == 404
