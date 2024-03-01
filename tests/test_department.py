import json
import pytest
import department
import course


@pytest.fixture(scope='function')
def course_lambda(dynamodb):
    return course.lambda_handler


@pytest.fixture(scope='function')
def department_lambda(dynamodb):
    return department.lambda_handler


def test_admin_lambda_handler(create_dynamodb_table, department_lambda, course_lambda):
    # Create a department record
    department_object = {
        'ItemId': '1',
        'ItemType': 'Department',
        'DepartmentName': 'Mathematics'
    }

    create_event = {
        'operation': 'put',
        **department_object
    }

    response = department_lambda(create_event, {})
    assert response['statusCode'] == 200

    # Get created record
    get_event = {
        'operation': 'get',
        'ItemId': '1',
        'ItemType': 'Department'
    }
    response = department_lambda(get_event, {})
    assert response['statusCode'] == 200

    retrieved_object = json.loads(response['body'])
    assert department_object == retrieved_object

    # Update department record
    updated_department_object = {
        'ItemId': '1',
        'ItemType': 'Department',
        'DepartmentName': 'Math'
    }

    update_event = {
        'operation': 'update',
        'ItemId': '1',
        'DepartmentName': 'Math'
    }

    response = department_lambda(update_event, {})
    assert response['statusCode'] == 200

    # Get updated record
    response = department_lambda(get_event, {})
    assert response['statusCode'] == 200
    assert updated_department_object == json.loads(response['body'])

    # Add 2 courses to department
    course_object1 = {
        'ItemId': '2',
        'CourseName': 'LinAlg',
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
        'ItemId': '3',
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
            'operation': 'put',
            **course_object
        }

        response = course_lambda(create_event, {})
        assert response['statusCode'] == 200

    # Get all courses for the department
    get_courses_event = {
        'operation': 'get',
        'DepartmentId': '1',
        'ItemType': 'Course'
    }

    response = department_lambda(get_courses_event, {})
    assert response['statusCode'] == 200
    retrieved_courses = json.loads(response['body'])
    assert len(retrieved_courses) == 2
    assert course_object1 in retrieved_courses
    assert course_object2 in retrieved_courses

    # Delete department
    delete_event = {
        'operation': 'delete',
        'ItemId': '1',
        'ItemType': 'Department'
    }

    response = department_lambda(delete_event, {})
    assert response['statusCode'] == 200

    # Verify deletion
    response = department_lambda(get_event, {})
    assert response['statusCode'] == 404
