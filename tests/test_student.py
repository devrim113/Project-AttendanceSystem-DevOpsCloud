import pytest
import json
import student
import course


@pytest.fixture(scope='function')
def student_lambda(dynamodb):
    return student.lambda_handler


@pytest.fixture(scope='function')
def course_lambda(dynamodb):
    return course.lambda_handler


def test_student_record_lifecycle(create_dynamodb_table, student_lambda, course_lambda):
    # Create student record
    object = {
        'ItemId': '1',
        'UserName': 'John Doe',
        'ItemType': 'Student'
    }
    create_event = {
        'path': '/student',
        'httpMethod': 'PUT',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': {'func': 'create_student'},
        'body': {
            **object
        },
        'isBase64Encoded': False
    }

    response = student_lambda(create_event, {})
    assert response['statusCode'] == 200

    # Get created record
    get_event = {
        'path': '/student',
        'httpMethod': 'GET',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': {'func': 'get_student', 'ItemId': '1'},
        'body': None,
        'isBase64Encoded': False
    }
    response = student_lambda(get_event, {})
    assert response['statusCode'] == 200
    retrieved_object = json.loads(response['body'])
    assert object == retrieved_object

    # Create course records
    course_object1 = {
        'ItemId': '101',
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

    course_object2 = {
        'ItemId': '102',
        'CourseName': 'Calc',
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

    for course_object in [course_object1, course_object2]:
        create_event = {
            'path': '/course',
            'httpMethod': 'PUT',
            'headers': {},
            'pathParameters': {},
            'queryStringParameters': {'func': 'create_course'},
            'body': {
                **course_object
            },
            'isBase64Encoded': False
        }

        response = course_lambda(create_event, {})
        assert response['statusCode'] == 200

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

    enlist_event = {
        'path': '/student',
        'httpMethod': 'PUT',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': {'func': 'enlist_student'},
        'body': {
            **attendance_object
        },
        'isBase64Encoded': False
    }

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

    update_event = {
        'path': '/student',
        'httpMethod': 'PUT',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': {'func': 'update_attendance'},
        'body': {
            **updated_attendance_object
        },
        'isBase64Encoded': False
    }

    response = student_lambda(update_event, {})
    assert response['statusCode'] == 200

    # Get updated record
    get_attendance_event = {
        'path': '/student/',
        'httpMethod': 'GET',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': {'func': 'get_student_course_attendance', 'UserId': '1', 'CourseId': '101'},
        'body': None,
        'isBase64Encoded': False
    }

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

    enlist_event2 = {
        'path': '/student',
        'httpMethod': 'PUT',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': {'func': 'enlist_student'},
        'body': {
            **attendance_object
        },
        'isBase64Encoded': False
    }

    response = student_lambda(enlist_event2, {})
    assert response['statusCode'] == 200

    # Get all student records
    get_courses = {
        'path': '/student',
        'httpMethod': 'GET',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': {'func': 'get_student_courses', 'UserId': '1'},
        'body': None,
        'isBase64Encoded': False
    }

    response = student_lambda(get_courses, {})
    assert response['statusCode'] == 200
    retrieved_courses = json.loads(response['body'])
    assert len(retrieved_courses) == 2

    # Get all student course names
    get_course_names = {
        'path': '/student',
        'httpMethod': 'GET',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': {'func': 'get_student_course_names', 'UserId': '1'},
        'body': None,
        'isBase64Encoded': False
    }

    response = student_lambda(get_course_names, {})
    retrieved_courses = json.loads(response['body'])
    assert response['statusCode'] == 200

    # Delete created records, either student or attendance
    delete_event = {
        'path': '/student',
        'httpMethod': 'DELETE',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': {'func': 'delete_student'},
        'body': {
            'ItemId': '2',
            'ItemType': 'Attendance'
        },
        'isBase64Encoded': False
    }

    response = student_lambda(delete_event, {})
    assert response['statusCode'] == 200

    delete_event = {
        'path': '/student',
        'httpMethod': 'DELETE',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': {'func': 'delete_student'},
        'body': {
            'ItemId': '3',
            'ItemType': 'Attendance'
        },
        'isBase64Encoded': False
    }

    response = student_lambda(delete_event, {})
    assert response['statusCode'] == 200

    # Verify deletion
    response = student_lambda(get_courses, {})
    assert response['statusCode'] == 404

    # delete student record
    delete_event = {
        'path': '/student',
        'httpMethod': 'DELETE',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': {'func': 'delete_student'},
        'body': {
            'ItemId': '1',
            'ItemType': 'Student'
        },
        'isBase64Encoded': False
    }

    response = student_lambda(delete_event, {})
    assert response['statusCode'] == 200

    # Verify deletion
    response = student_lambda(get_event, {})
    assert response['statusCode'] == 404

    # Get all courses
    get_courses_event = {
        'path': '/student',
        'httpMethod': 'GET',
        'headers': {},
        'pathParameters': {},
        'queryStringParameters': {'func': 'get_all_courses'},
        'body': None,
        'isBase64Encoded': False
    }

    response = student_lambda(get_courses_event, {})
    assert response['statusCode'] == 200
    retrieved_courses = json.loads(response['body'])
    assert len(retrieved_courses) == 2
