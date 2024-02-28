import pytest
import json
import student


@pytest.fixture(scope='function')
def student_lambda(dynamodb):
    return student.lambda_handler


def test_student_record_lifecycle(create_dynamodb_table, student_lambda):
    # Create record
    object = {
        'UserId': '1',
        'CourseId': '101',
        'CourseName': 'Math',
        'Attendance': {
            '2022-01-01': {
                'from': '09:00',
                'to': '12:00',
                'status': 'present'
            },
            '2022-02-01': {
                'from': '09:00',
                'to': '12:00',
                'status': 'present'
            }
        },
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
    }
    response = student_lambda(get_event, {})
    assert response['statusCode'] == 200
    retrieved_object = json.loads(response['body'])

    for key in object:
        assert object[key] == retrieved_object[
            key], f"Value mismatch for {key}: expected {object[key]}, got {retrieved_object[key]}"

    # Update created record's attendance
    updated_object = {
        'UserId': '1',
        'CourseId': '101',
        'CourseName': 'Math',
        'Attendance': {
            '2022-01-01': {
                'from': '09:00',
                'to': '12:00',
                'status': 'present'
            },
            '2022-02-01': {
                'from': '09:00',
                'to': '12:00',
                'status': 'present'
            },
            '2022-03-01': {
                'from': '09:00',
                'to': '12:00',
                'status': 'absent'
            }
        },
        'UserName': 'John Doe'
    }

    update_event = {
        'operation': 'update',
        **updated_object,
        'Present': False
    }

    response = student_lambda(update_event, {})
    assert response['statusCode'] == 200

    # Get updated record
    response = student_lambda(get_event, {})
    assert response['statusCode'] == 200
    retrieved_object = json.loads(response['body'])

    for key in updated_object:
        assert updated_object[key] == retrieved_object[
            key], f"Value mismatch for {key}: expected {updated_object[key]}, got {retrieved_object[key]}"

    # Add another record
    object = {
        'UserId': '1',
        'CourseId': '102',
        'CourseName': 'Science',
        'Attendance': {
            '2022-01-01': {
                'from': '09:00',
                'to': '12:00',
                'status': 'present'
            },
            '2022-02-01': {
                'from': '09:00',
                'to': '12:00',
                'status': 'absent'
            }
        },
        'UserName': 'John Doe'
    }

    create_event = {
        'operation': 'put',
        **object
    }

    response = student_lambda(create_event, {})
    assert response['statusCode'] == 200

    # Get all student records
    get_all_event = {
        'operation': 'get',
        'UserId': '1'
    }

    response = student_lambda(get_all_event, {})
    print(json.loads(response['body']))
    assert response['statusCode'] == 200

    # Delete created records
    delete_event = {
        'operation': 'delete',
        'UserId': '1',
        'CourseId': '101'
    }
    response = student_lambda(delete_event, {})
    assert response['statusCode'] == 200

    delete_event = {
        'operation': 'delete',
        'UserId': '1',
        'CourseId': '102'
    }
    response = student_lambda(delete_event, {})
    assert response['statusCode'] == 200

    # Verify deletion
    response = student_lambda(get_all_event, {})
    assert response['statusCode'] == 404
