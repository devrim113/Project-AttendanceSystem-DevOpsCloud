import pytest
import json
import teacher
import student


@pytest.fixture(scope='function')
def student_lambda(dynamodb):
    return student.lambda_handler


@pytest.fixture(scope='function')
def teacher_lambda(dynamodb):
    return teacher.lambda_handler


def test_admin_lambda_handler(create_dynamodb_table, teacher_lambda, student_lambda):
    # Create a teacher record
    teacher_object = {
        'UserId': '1',
        'CourseId': '101',
        'CourseName': 'Math',
        'UserName': 'John Doe'
    }

    create_event = {
        'operation': 'put',
        **teacher_object
    }

    response = teacher_lambda(create_event, {})
    assert response['statusCode'] == 200

    # Create two student records with attendance in the teacher's course
    student_object_1 = {
        'UserId': '2',
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
        'UserName': 'Jane Doe',
        'UserType': 'Student'
    }

    student_object_2 = {
        'UserId': '3',
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
                'status': 'absent'
            }
        },
        'UserName': 'Jim Doe',
        'UserType': 'Student'
    }

    for x in [student_object_1, student_object_2]:
        create_event = {
            'operation': 'put',
            **x
        }

        response = student_lambda(create_event, {})
        assert response['statusCode'] == 200

    # Get all courses for the teacher
    get_event = {
        'operation': 'get',
        'UserId': '1'
    }
    response = teacher_lambda(get_event, {})
    assert response['statusCode'] == 200

    retrieved_courses = json.loads(response['body'])
    assert len(retrieved_courses) == 1
    assert retrieved_courses[0]['CourseId'] == teacher_object['CourseId']

    # Get all attendance records for the teacher's course
    get_event = {
        'operation': 'get',
        'UserId': '1',
        'CourseId': '101'
    }

    response = teacher_lambda(get_event, {})
    retrieved_attendance = json.loads(response['body'])
    print(retrieved_attendance)
    assert response['statusCode'] == 200

    assert len(retrieved_attendance) == 2
    assert student_object_1 in retrieved_attendance
    assert student_object_2 in retrieved_attendance

    # Update the attendance record for one of the students
    student_object_1['Attendance']['2022-03-01'] = {
        'from': '09:00',
        'to': '12:00',
        'status': 'absent'
    }

    update_event = {
        'operation': 'put',
        **student_object_1
    }

    response = student_lambda(update_event, {})
    assert response['statusCode'] == 200

    # Get the updated attendance record for the student
    get_event = {
        'operation': 'get',
        'UserId': '1',
        'CourseId': '101'
    }

    response = teacher_lambda(get_event, {})
    assert response['statusCode'] == 200
    retrieved_attendance = json.loads(response['body'])
    print(retrieved_attendance)
    assert len(retrieved_attendance) == 2
    assert retrieved_attendance[0] == student_object_1 or retrieved_attendance[1] == student_object_1
    assert retrieved_attendance[0] == student_object_2 or retrieved_attendance[1] == student_object_2

    # Delete the attendance record for the other student
    delete_event = {
        'operation': 'delete',
        'UserId': '3',
        'CourseId': '101'
    }

    response = student_lambda(delete_event, {})
    assert response['statusCode'] == 200

    # Get all attendance records for the teacher's course
    get_event = {
        'operation': 'get',
        'UserId': '1',
        'CourseId': '101'
    }

    response = teacher_lambda(get_event, {})
    assert response['statusCode'] == 200
    retrieved_attendance = json.loads(response['body'])
    print(retrieved_attendance)
    assert len(retrieved_attendance) == 1
    assert retrieved_attendance[0] == student_object_1
    assert retrieved_attendance[0] != student_object_2

    # Delete the teacher record
    delete_event = {
        'operation': 'delete',
        'UserId': '1',
        'CourseId': '101'
    }

    response = teacher_lambda(delete_event, {})
    assert response['statusCode'] == 200

    # Get all courses for the teacher
    get_event = {
        'operation': 'get',
        'UserId': '1'
    }
    response = teacher_lambda(get_event, {})
    assert response['statusCode'] == 400
