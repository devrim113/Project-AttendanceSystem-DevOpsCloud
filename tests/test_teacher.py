# import pytest
# import json
# import teacher
# import student


# @pytest.fixture(scope='function')
# def student_lambda(dynamodb):
#     return student.lambda_handler


# @pytest.fixture(scope='function')
# def teacher_lambda(dynamodb):
#     return teacher.lambda_handler


# def test_admin_lambda_handler(create_dynamodb_table, teacher_lambda, student_lambda):
#     # Create a teacher record
#     teacher_object = {
#         'ItemId': '1',
#         'ItemType': 'Teacher',
#         'UserName': 'John Doe'
#     }

#     create_event = {
#         'operation': 'put',
#         **teacher_object
#     }

#     response = teacher_lambda(create_event, {})
#     assert response['statusCode'] == 200

#     # Get created record
#     get_event = {
#         'operation': 'get',
#         'ItemId': '1',
#         'ItemType': 'Teacher'
#     }
#     response = teacher_lambda(get_event, {})
#     assert response['statusCode'] == 200

#     retrieved_object = json.loads(response['body'])
#     assert teacher_object == retrieved_object

#     # Update teacher record
#     updated_teacher_object = {
#         'ItemId': '1',
#         'ItemType': 'Teacher',
#         'UserName': 'Jane Doe'
#     }

#     update_event = {
#         'operation': 'update',
#         'ItemId': '1',
#         'UserName': 'Jane Doe'
#     }

#     response = teacher_lambda(update_event, {})
#     assert response['statusCode'] == 200

#     # Get updated record
#     response = teacher_lambda(get_event, {})
#     assert response['statusCode'] == 200
#     assert updated_teacher_object == json.loads(response['body'])

#     # Add a course to teacher
#     teaches_object = {
#         'ItemId': '2',
#         'UserId': '1',
#         'CourseId': '101',
#         'ItemType': 'TeachesCourse'
#     }

#     enlist_event_teacher = {
#         'operation': 'put',
#         **teaches_object
#     }

#     response = teacher_lambda(enlist_event_teacher, {})
#     assert response['statusCode'] == 200

#     # Get all courses for the teacher
#     get_courses_event = {
#         'operation': 'get',
#         'UserId': '1'
#     }

#     response = teacher_lambda(get_courses_event, {})
#     assert response['statusCode'] == 200

#     # Add two students to the same course
#     student_object1 = {
#         'ItemId': '3',
#         'ItemType': 'Student',
#         'UserName': 'John Doe'
#     }

#     student_object2 = {
#         'ItemId': '4',
#         'ItemType': 'Student',
#         'UserName': 'Hamid Doe'
#     }

#     for student in [student_object1, student_object2]:
#         create_event = {
#             'operation': 'put',
#             **student
#         }
#         response = student_lambda(create_event, {})
#         assert response['statusCode'] == 200

#     # Enlist students to the course
#     attendance_object_student1 = {
#         'ItemId': '5',
#         'CourseId': '101',
#         'UserId': '3',
#         'ItemType': 'Attendance',
#         'Attendance': {
#             '2022-01-01': {
#                 'from': '09:00',
#                 'to': '12:00',
#                 'status': 'present'
#             }
#         }
#     }

#     attendance_object_student2 = {
#         'ItemId': '6',
#         'CourseId': '101',
#         'UserId': '4',
#         'ItemType': 'Attendance',
#         'Attendance': {
#             '2022-01-01': {
#                 'from': '09:00',
#                 'to': '12:00',
#                 'status': 'present'
#             }
#         }
#     }

#     for attendance in [attendance_object_student1, attendance_object_student2]:
#         enlist_event_student = {
#             'operation': 'put',
#             **attendance
#         }
#         response = student_lambda(enlist_event_student, {})
#         assert response['statusCode'] == 200

#     # Get attendance for the students in the course
#     get_attendance_event = {
#         'operation': 'get',
#         'CourseId': '101'
#     }

#     response = teacher_lambda(get_attendance_event, {})
#     assert response['statusCode'] == 200

#     # Check attendance for the students
#     attendance = json.loads(response['body'])
#     assert len(attendance) == 2
#     assert attendance_object_student1 in attendance
#     assert attendance_object_student2 in attendance

#     # Delete the teacher record
#     delete_event = {
#         'operation': 'delete',
#         'ItemId': '1'
#     }

#     response = teacher_lambda(delete_event, {})
#     assert response['statusCode'] == 200

#     # Verify that the teacher record is deleted
#     response = teacher_lambda(get_event, {})
#     assert response['statusCode'] == 400
