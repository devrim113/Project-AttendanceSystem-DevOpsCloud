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
    create_event = {
        'operation': 'put',
        **object
    }
    response = student_lambda(create_event, {})
    assert response['statusCode'] == 200

    # Get created record
    get_event = {
        'operation': 'get',
        'ItemId': '1',
        'ItemType': 'Student'
    }
    response = student_lambda(get_event, {})
    assert response['statusCode'] == 200
    retrieved_object = json.loads(response['body'])
    assert len(retrieved_object) == 1
    assert object == retrieved_object[0]

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
        'operation': 'put',
        **attendance_object
    }

    response = student_lambda(enlist_event, {})
    assert response['statusCode'] == 200

    # Update student attendence to get correct attendance
    update_event = {
        'operation': 'update',
        **attendance_object
    }

    response = student_lambda(update_event, {})
    assert response['statusCode'] == 200

    # Get updated record
    get_attendance_event = {
        'operation': 'get',
        'UserId': '1',
        'CourseId': '101'
    }

    response = student_lambda(get_attendance_event, {})
    assert response['statusCode'] == 200
    retrieved_object = json.loads(response['body'])

    for key in attendance_object:
        assert attendance_object[key] == retrieved_object[
            key], f"Value mismatch for {key}: expected {attendance_object[key]}, got {retrieved_object[key]}"

    # Add another record
    attendance_object = {
        'ItemId': '3',
        'CourseId': '102',
        'UserId': '1',
        'ItemType': 'Attendance',
        'Attendance': {}
    }

    create_event = {
        'operation': 'put',
        **attendance_object
    }

    response = student_lambda(create_event, {})
    assert response['statusCode'] == 200

    # Get all student records
    get_courses = {
        'operation': 'get',
        'UserId': '1'
    }

    response = student_lambda(get_courses, {})
    assert response['statusCode'] == 200
    retrieved_courses = json.loads(response['body'])
    assert len(retrieved_courses) == 2

    # Delete created records
    delete_event = {
        'operation': 'delete',
        'ItemId': '2',
        'ItemType': 'Attendance'
    }
    response = student_lambda(delete_event, {})
    assert response['statusCode'] == 200

    delete_event = {
        'operation': 'delete',
        'ItemId': '3',
        'ItemType': 'Attendance'
    }
    response = student_lambda(delete_event, {})
    assert response['statusCode'] == 200

    # Verify deletion
    response = student_lambda(get_courses, {})
    assert response['statusCode'] == 404

    # delete student record
    delete_event = {
        'operation': 'delete',
        'ItemId': '1',
        'ItemType': 'Student'
    }

    response = student_lambda(delete_event, {})
    assert response['statusCode'] == 200

    # Verify deletion
    response = student_lambda(get_event, {})
    assert response['statusCode'] == 404
