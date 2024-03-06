import pytest
import json
import student


@pytest.fixture(scope='function')
def student_lambda(dynamodb):
    return student.lambda_handler


def test_student_record_lifecycle(create_dynamodb_table, student_lambda):
    # Create student record
    object = {
        'ItemId': '1',
        'UserName': 'John Doe',
        'ItemType': 'Student'
    }
    create_event = json.dumps({
        'path': '/student',
        'httpMethod': 'PUT',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': json.dumps({'func': 'create_student'}),
        'body': json.dumps({
            **object
        }),
        'isBase64Encoded': False
    })

    response = student_lambda(create_event, {})
    assert response['statusCode'] == 200

    # Get created record
    get_event = json.dumps({
        'path': '/student',
        'httpMethod': 'GET',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': json.dumps({'func': 'get_student', 'ItemId': '1'}),
        'body': None,
        'isBase64Encoded': False
    })
    response = student_lambda(get_event, {})
    assert response['statusCode'] == 200
    retrieved_object = json.loads(response['body'])
    assert object == retrieved_object

    # Create student attendance record
    attendance_object = {
        'ItemId': '2',
        'CourseId': '101',
        'UserId': '1',
        'ItemType': 'Attendance',
        'Attendance': {
            '2022-01-01': {
                'from': '09:00',
                'to': '12:00',
                'status': 'present'
            }
        }
    }

    enlist_event = json.dumps({
        'path': '/student',
        'httpMethod': 'PUT',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': json.dumps({'func': 'enlist_student'}),
        'body': json.dumps({
            **attendance_object
        }),
        'isBase64Encoded': False
    })

    response = student_lambda(enlist_event, {})
    assert response['statusCode'] == 200

    # Update student attendence to get correct attendance
    updated_attendance_object = {
        'ItemId': '2',
        'CourseId': '101',
        'UserId': '1',
        'ItemType': 'Attendance',
        'Attendance': {
            '2022-01-01': {
                'from': '09:00',
                'to': '12:00',
                'status': 'absent'
            }
        }
    }

    update_event = json.dumps({
        'path': '/student',
        'httpMethod': 'PUT',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': json.dumps({'func': 'update_attendance'}),
        'body': json.dumps({
            **updated_attendance_object
        }),
        'isBase64Encoded': False
    })

    response = student_lambda(update_event, {})
    assert response['statusCode'] == 200

    # Get updated record
    get_attendance_event = json.dumps({
        'path': '/student/',
        'httpMethod': 'GET',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': json.dumps({'func': 'get_student_course_attendance', 'UserId': '1', 'CourseId': '101'}),
        'body': None,
        'isBase64Encoded': False
    })

    response = student_lambda(get_attendance_event, {})
    assert response['statusCode'] == 200
    retrieved_object = json.loads(response['body'])

    for key in updated_attendance_object:
        assert updated_attendance_object[key] == retrieved_object[
            key], f"Value mismatch for {key}: expected {attendance_object[key]}, got {retrieved_object[key]}"

    # Add another record
    attendance_object = {
        'ItemId': '3',
        'CourseId': '102',
        'UserId': '1',
        'ItemType': 'Attendance',
        'Attendance': {}
    }

    enlist_event2 = json.dumps({
        'path': '/student',
        'httpMethod': 'PUT',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': json.dumps({'func': 'enlist_student'}),
        'body': json.dumps({
            **attendance_object
        }),
        'isBase64Encoded': False
    })

    response = student_lambda(enlist_event2, {})
    assert response['statusCode'] == 200

    # Get all student records
    get_courses = json.dumps({
        'path': '/student',
        'httpMethod': 'GET',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': json.dumps({'func': 'get_student_courses', 'UserId': '1'}),
        'body': None,
        'isBase64Encoded': False
    })

    response = student_lambda(get_courses, {})
    assert response['statusCode'] == 200
    retrieved_courses = json.loads(response['body'])
    assert len(retrieved_courses) == 2

    # Delete created records, either student or attendance
    delete_event = json.dumps({
        'path': '/student',
        'httpMethod': 'DELETE',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': json.dumps({'func': 'delete_student'}),
        'body': json.dumps({
            'ItemId': '2',
            'ItemType': 'Attendance'
        }),
        'isBase64Encoded': False
    })

    response = student_lambda(delete_event, {})
    assert response['statusCode'] == 200

    delete_event = json.dumps({
        'path': '/student',
        'httpMethod': 'DELETE',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': json.dumps({'func': 'delete_student'}),
        'body': json.dumps({
            'ItemId': '3',
            'ItemType': 'Attendance'
        }),
        'isBase64Encoded': False
    })

    response = student_lambda(delete_event, {})
    assert response['statusCode'] == 200

    # Verify deletion
    response = student_lambda(get_courses, {})
    assert response['statusCode'] == 404

    # delete student record
    delete_event = json.dumps({
        'path': '/student',
        'httpMethod': 'DELETE',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': json.dumps({'func': 'delete_student'}),
        'body': json.dumps({
            'ItemId': '1',
            'ItemType': 'Student'
        }),
        'isBase64Encoded': False
    })

    response = student_lambda(delete_event, {})
    assert response['statusCode'] == 200

    # Verify deletion
    response = student_lambda(get_event, {})
    print(response)
    assert response['statusCode'] == 404
