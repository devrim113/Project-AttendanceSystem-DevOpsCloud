"""
This module contains functions for managing attendance records for students in a DynamoDB table.

Functions:
- create_student_record: Create a student record in the database.
- remove_student_course_attendance: Removes the attendance record of a student for a specific course.
- delete_student_record: Deletes a student record from the table.
- update_student_record: Update the student record in the database.
- update_attendance_record: Update the attendance record for a student.
- get_student: Gets the student record.
- get_student_courses: Retrieves all the courses of a student.
- get_student_course_attendance: Retrieves the attendance record of a student for a specific course.
- lambda_handler: Lambda handler function to interact with the DynamoDB table.
"""

import logging
import json
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Attr
from boto3.dynamodb.conditions import Key

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('AllData')


def make_response(status_code, body):
    """
    Create a response object for the API Gateway.

    Args:
        status_code (int): The status code for the response.
        body (str): The body of the response.

    Returns:
        dict: The response object.
    """
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS, GET, POST, PUT, DELETE',
            'Access-Control-Allow-Headers': 'Content-Type, X-Amz-Date, Authorization, X-Api-Key, X-Amz-Security-Token, Access-Control-Allow-Origin',
        },
        'body': json.dumps(body)
    }


def get_all_courses():
    """
    Retrieves all the courses from the database.
    Placed in student.py because of the large frequency in which this function is called.

    Returns:
        list: A list of items containing all the courses.
    """
    try:
        response = table.scan(
            FilterExpression=Attr('ItemType').eq('Course')
        )
        if len(response.get('Items')) > 0:
            return make_response(200, response.get('Items'))
        return make_response(404, 'No courses found.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def create_student_record(user_id, user_name):
    """
    Create a student record in the database.

    Args:
        user_id (str): The ID of the student.
        # course_id (str): The ID of the course.
        # course_name (str): The name of the course.
        user_name (str): The name of the student.

    Returns:
        dict: The response from the database after creating the student record.
            If an error occurs, None is returned.
    """
    try:
        response = table.put_item(
            Item={
                'ItemId': user_id,
                'UserName': user_name,
                'ItemType': 'Student'
            },
            ConditionExpression='attribute_not_exists(ItemId) AND attribute_not_exists(ItemType)'
        )
        if response:
            return make_response(200, 'Record created successfully.')
        return make_response(400, 'Record not created.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def delete_record(item_id, item_type):
    """
    Deletes a record from the table using its ItemId.

    Args:
        ItemId (str): The ID of the item.

    Returns:
        dict or None: The response from the delete operation, or None if an error occurred.
    """
    try:
        response = table.delete_item(
            Key={
                'ItemId': item_id,
                'ItemType': item_type
            }
        )
        if response:
            return make_response(200, 'Record deleted successfully.')
        return make_response(400, 'Record not deleted.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def remove_student_course_attendance(user_id, course_id):
    # TODO: If necessary add functionality to remove student course attendance based on user_id and course_id
    # This can be done by first querying the table to get the item_id of the attendance record.
    """
    Removes the attendance record of a student for a specific course.

    Args:
        user_id (str): The ID of the student.
        course_id (str): The ID of the course.

    Returns:
        dict or None: The response from the delete operation, or None if an error occurred.
    """
    try:
        response = table.delete_item(
            Key={
                'UserId': user_id,
                'CourseId': course_id
            }
        )
        if response:
            return make_response(200, 'Record deleted successfully.')
        return make_response(400, 'Record not deleted.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def update_student_record(user_id, user_name):
    """
    Update the student record in the database.

    Args:
        user_id (str): The ID of the student.
        user_name (str): The name of the student.

    Returns:
        dict or None: The response from the update operation if successful, None otherwise.
    """
    try:
        response = table.update_item(
            Key={
                'ItemId': user_id,
                'ItemType': 'Student'
            },
            UpdateExpression="SET UserName = :user_name",
            ExpressionAttributeValues={
                ':user_name': user_name
            },
            ReturnValues="UPDATED_NEW"
        )
        if response:
            return make_response(200, 'Record updated successfully.')
        return make_response(400, 'Record not updated.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def update_attendance_record(item_id, course_id, attendance):
    """
    Update the attendance record for a student in a specific course.
    Updates one attendance instance (date) at a time

    Args:
        item_id (str): The ID of the item. In this case the item is the student's attendance record for the course.
        attendance (dict): The updated attendance value.
            This is a nested object with the following structure:
                attendance = {
                    'date': {
                        'from': (str),
                        'to': (str),
                        'status': (str)
                    }

    Returns:
        dict or None: The response from the update operation if successful, None otherwise.
    """
    try:
        attendance_record = table.get_item(
            Key={
                'ItemId': item_id,
                'ItemType': 'Attendance'
            }
        )
        if attendance_record.get('Item'):
            attendance = attendance_record.get('Item')[
                'Attendance'] | attendance

        print(attendance)
        response = table.update_item(
            Key={
                'ItemId': item_id,
                'ItemType': 'Attendance'
            },
            UpdateExpression="SET Attendance = :attendance",
            ExpressionAttributeValues={
                ':attendance': attendance
            },
            ReturnValues="UPDATED_NEW"
        )
        if response:
            return make_response(200, 'Record updated successfully.')
        return make_response(400, 'Record not updated.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def get_student(user_id):
    """
    Retrieves all the attendance records for all courses of a student.

    Args:
        user_id (str): The user ID of the student.

    Returns:
        list: A list of items containing the student's information.

    Raises:
        ClientError: If an error occurs while querying the table.
    """
    try:
        response = table.get_item(
            Key={
                'ItemId': user_id,
                'ItemType': 'Student'
            }
        )
        if response.get('Item') is not None:
            return make_response(200, response.get('Item'))
        return make_response(404, 'Record not found.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def get_student_courses(user_id):
    """
    Retrieves all the courses of a student.

    Args:
        user_id (str): The user ID of the student.

    Returns:
        list: A list of items containing the student's information.

    Raises:
        ClientError: If an error occurs while querying the table.
    """
    try:
        response = table.query(
            IndexName='UserIdCourseIdIndex',
            KeyConditionExpression=Key('UserId').eq(user_id)
        )
        if len(response.get('Items')) > 0:
            return make_response(200, response.get('Items'))
        return make_response(404, 'Record not found.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def get_student_course_names(user_id):
    """
    Retrieves the names of all the courses of a student.

    Args:
        user_id (str): The user ID of the student.

    Returns:
        dict: A dictionary containing the course names of the student.
            {course_id: course_name}

    Raises:
        ClientError: If an error occurs while querying the table.
    """
    try:
        response = table.query(
            IndexName='UserIdCourseIdIndex',
            KeyConditionExpression=Key('UserId').eq(user_id)
        )

        course_names = {item.get('CourseId'): '404-noNameFound'
                        for item in response.get('Items')}
        for course_id in course_names.keys():
            response = table.get_item(
                Key={
                    'ItemId': course_id,
                    'ItemType': 'Course'
                }
            )
            try:
                course_names[course_id] = response.get(
                    'Item').get('CourseName')
            except:
                pass
        if len(course_names.keys()) > 0:
            return make_response(200, course_names)
        return make_response(404, 'Record not found.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def get_student_course_attendance(user_id, course_id):
    """
    Retrieves the attendance record of a student for a specific course.

    Args:
        user_id (str): The ID of the student.
        course_id (str): The ID of the course.

    Returns:
        dict: The attendance record of the student for the course, or None if an error occurs.
    """
    try:
        response = table.get_item(
            Key={
                'ItemId': course_id,
                'ItemType': 'Course'
            }
        )
        classes = response.get('Item')['Classes']

        response = table.query(
            IndexName='UserIdCourseIdIndex',
            KeyConditionExpression=Key('UserId').eq(
                user_id) & Key('CourseId').eq(course_id)
        )

        id_attendance = []
        try:
            id_attendance = [(item.get('UserId'), classes | item.get('Attendance'))
                             if type(item.get('Attendance')) == dict else (item.get('UserId'), classes)
                             for item in response.get('Items')]
        except:
            pass

        for i, (user_id, _) in enumerate(id_attendance):
            response = table.get_item(
                Key={
                    'ItemId': user_id,
                    'ItemType': 'Student'
                }
            )
            try:
                id_attendance[i] = (id_attendance[i][0], response.get(
                    'Item').get('UserName'), (id_attendance[i][1]))
            except:
                pass

        if len(id_attendance) > 0:
            return make_response(200, id_attendance)
        return make_response(404, 'Attendance not found.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def enlist_student_course(item_id, user_id, course_id, attendance):
    """
    Enlist a student to a course.

    Args:
        user_id (str): The ID of the student.
        course_id (str): The ID of the course.

    Returns:
        dict or None: The response from the put operation, or None if an error occurred.
    """
    try:
        response = table.put_item(
            Item={
                'ItemId': item_id,
                'UserId': user_id,
                'CourseId': course_id,
                'ItemType': 'Attendance',
                'Attendance': attendance
            },
            ConditionExpression='attribute_not_exists(ItemId) AND attribute_not_exists(ItemType)'
        )
        if response:
            return make_response(200, 'Record created successfully.')
        return make_response(400, 'Record not created.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def lambda_handler(event, context):
    """
    Lambda handler function to interact with the DynamoDB table.
    The 'operation' field in the body data determines the action to be performed.
    The following operations are supported:
    - 'put': Creates a new record for a student.
    - 'update': Updates a student record or attendance record.
    - 'get': Retrieves all courses for a student or all attendance records for a student's course.
    - 'delete': Deletes a record for a student.

    The corresponding functions called for each operation are:
    - 'put': create_student_record() or enlist_student_course()
    - 'update': update_attendance_record() or update_student_record()
    - 'get': get_student_course_attendance() or get_student() or get_student_courses()
    - 'delete': delete_student_record() or remove_student_course_attendance()

    Args:
        body (dict): The body data passed to the Lambda function.
        context (object): The context object provided by AWS Lambda.

    Returns:
        dict: The response containing the statusCode, body, and headers.
    """

    if context:
        try:
            logger.info(f'AWS request ID: {context.aws_request_id}')
            logger.info(f'Lambda function ARN: {context.invoked_function_arn}')
            logger.info(
                f'CloudWatch log stream name: {context.log_stream_name}')
            logger.info(
                f'Remaining execution time: {context.get_remaining_time_in_millis()} ms')
        except:
            pass

    try:
        query_params = event['queryStringParameters']
        function = query_params['func']
    except:
        return make_response(400, f"{event['queryStringParameters']['func']}Invalid operation. Make sure to include the 'func' parameter in the query string.")
    if type(event['body']) == str:
        body = json.loads(event['body'])
    else:
        body = event['body']
    match function:
        case 'create_student':
            return create_student_record(body['ItemId'], body['UserName'])

        case 'enlist_student':
            return enlist_student_course(
                body['ItemId'], body['UserId'], body['CourseId'], body['Attendance'])

        case 'update_attendance':
            return update_attendance_record(
                body['ItemId'], body['CourseId'], body['Attendance'])

        case 'update_student':
            return update_student_record(
                body['UserId'], body['UserName'])

        case 'get_all_courses':
            return get_all_courses()

        case 'get_student':
            return get_student(query_params['ItemId'])

        case 'get_student_courses':
            return get_student_courses(query_params['UserId'])

        case 'get_student_course_names':
            return get_student_course_names(query_params['UserId'])

        case 'get_student_course_attendance':
            return get_student_course_attendance(
                query_params['UserId'], query_params['CourseId'])

        case 'delete_student':
            return delete_record(
                body['ItemId'], body['ItemType'])

        case _:
            return make_response(400, 'Invalid operation.')
