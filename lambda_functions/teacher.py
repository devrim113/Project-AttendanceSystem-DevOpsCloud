"""
This module contains functions for managing attendance records for teachers in a DynamoDB table.

Functions:
- put_attendance_record: Put attendance record for a teacher.
- get_all_courses: Get all courses for a teacher.
- get_all_course_attendance: Get all attendance records of students for a teacher's course.
- delete_attendance_record: Delete attendance record for a teacher.
- lambda_handler: Lambda handler function to interact with the DynamoDB table.
"""

import logging
import json
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('AllData')

UserPoolId = "eu-central-1_jiDMNCeuM"

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


def create_teacher_record(email, user_name):
    """
    Create object for a teacher.

    Args:
        user_id (str): The ID of the user.
        user_name (str): The name of the user.

    Returns:
        dict: The response from the table.put_item() operation.

    Raises:
        ClientError: If an error occurs while putting the item.
    """
    client = boto3.client('cognito-idp')
    try:
        response = client.admin_create_user(
            UserPoolId=UserPoolId,
            Username=email,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': email
                },
                {
                    'Name': 'email_verified',
                    'Value': 'false'
                },
                {
                    'Name': 'name',
                    'Value': user_name
                }
            ],
            clientMetadata={
                'isAdmin': 'false',
                'isTeacher': 'true'
            }
        )
        user_id = response['User']['Username']

        response = table.put_item(
            Item={
                'ItemId': user_id,
                'UserName': user_name,
                'ItemType': 'Teacher'
            },
            ConditionExpression='attribute_not_exists(ItemId) AND attribute_not_exists(ItemType)'
        )
        if response:
            return make_response(200, 'Record created successfully.')
        return make_response(400, 'Record not created.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Record not created.' + e.response['Error']['Message'])


def update_teacher_record(item_id, user_name):
    """
    Update object for a teacher.

    Args:
        item_id (str): The ID of the user.
        user_name (str): The name of the user.

    Returns:
        dict: The response from the table.update_item() operation.

    Raises:
        ClientError: If an error occurs while updating the item.
    """
    try:
        response = table.update_item(
            Key={
                'ItemId': item_id,
                'ItemType': 'Teacher'
            },
            UpdateExpression="set UserName = :n",
            ExpressionAttributeValues={
                ':n': user_name
            },
            ReturnValues="UPDATED_NEW"
        )
        if response:
            return make_response(200, 'Record updated successfully.')
        return make_response(400, 'Record not updated.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def assign_course_to_teacher(item_id, course_id, user_id):
    """
    Assign a course to a teacher.

    Args:
        course_id (str): The ID of the course.
        user_id (str): The ID of the user.

    Returns:
        dict: The response from the table.put_item() operation.

    Raises:
        ClientError: If an error occurs while putting the item.
    """
    try:
        response = table.put_item(
            Item={
                'ItemId': item_id,
                'UserId': user_id,
                'CourseId': course_id,
                'ItemType': 'TeachesCourse'
            },
            ConditionExpression='attribute_not_exists(ItemId) AND attribute_not_exists(ItemType)'
        )
        if response:
            return make_response(200, 'Record created successfully.')
        return make_response(400, 'Record not created.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def get_teacher(user_id):
    """
    Get a teacher.

    Args:
        user_id (str): The ID of the user.

    Returns:
        dict: The teacher object.

    Raises:
        ClientError: If an error occurs while getting the item.
    """
    try:
        response = table.get_item(
            Key={
                'ItemId': user_id,
                'ItemType': 'Teacher'
            }
        )
        if 'Item' in response:
            return make_response(200, response['Item'])
        return make_response(404, 'No records found.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def get_teacher_courses(user_id):
    """
    Get all courses for a teacher.

    Args:
        user_id (str): The ID of the user.

    Returns:
        list: The list of courses for the teacher.

    Raises:
        ClientError: If an error occurs while getting the items.
    """
    try:
        response = table.query(
            IndexName='UserIdCourseIdIndex',
            KeyConditionExpression=Key('UserId').eq(user_id)
        )
        if 'Items' in response:
            return make_response(200, response['Items'])
        return make_response(404, 'No records found.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def get_teacher_course_names(user_id):
    """
    Get all course names for a teacher.

    Args:
        user_id (str): The ID of the user.

    Returns:
        list: The list of course names for the teacher.

    Raises:
        ClientError: If an error occurs while getting the items.
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
        if len(course_names) > 0:
            return make_response(200, course_names)
        return make_response(404, 'No records found.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def get_all_course_attendance(course_id):
    """
    Get all attendance records of students for a teacher's course.
    If the attendance record for a class in the course is not found for a student,
    the class is added to the list with no status value and key.
    Uses the Global Secondary Index CourseIDUserTypeIndex to query the table.

    Args:
        course_id (str): The ID of the course.

    Returns:
        list: The list of attendance records for the teacher's course.

    Raises:
        ClientError: If an error occurs while getting the items.
    """
    try:
        # Get all classes for the course
        response = table.get_item(
            Key={
                'ItemId': course_id,
                'ItemType': 'Course'
            }
        )
        classes = response.get('Item')['Classes']

        # Get all attendance records for the course
        response = table.query(
            IndexName='CourseIdItemTypeIndex',
            KeyConditionExpression=Key('CourseId').eq(
                course_id) & Key('ItemType').eq('Attendance')
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
                    'Item').get('UserName'), id_attendance[i][1])
            except:
                pass

        if len(id_attendance) > 0:
            return make_response(200, id_attendance)
        return make_response(404, 'No records found.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def delete_teacher(user_id):
    """
    Delete teacher's record.

    Args:
        user_id (str): The ID of the user.

    Returns:
        dict: The response from the table.delete_item() operation.

    Raises:
        ClientError: If an error occurs while deleting the item.
    """
    client = boto3.client('cognito-idp')

    try:
        client.admin_delete_user(
            UserPoolId=UserPoolId,
            Username=user_id
        )
        response = table.delete_item(
            Key={
                'ItemId': user_id,
                'ItemType': 'Teacher'
            }
        )
        if response:
            return make_response(200, 'Record deleted successfully.')
        return make_response(404, 'Record not deleted.')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def lambda_handler(event, context):
    """
    Lambda handler function to interact with the DynamoDB table.
    The 'operation' field in the event data determines the action to be performed.
    The following operations are supported:
    - 'put': Creates a new record for a teacher.
    - 'get': Retrieves all courses for a teacher or all attendance records for a teacher's course.
    - 'update': Updates a teacher's record.
    - 'delete': Deletes a teacher's record.

    The corresponding functions called for each operation are:
    - 'put': create_teacher_record()
    - 'get': get_teacher_courses() or get_all_course_attendance()
    - 'update': update_teacher_record()
    - 'delete': delete_teacher()

    Args:
        event (dict): The event data passed to the Lambda function.
        context (object): The context object provided by AWS Lambda.

    Returns:
        dict: The response containing the statusCode, body, and headers.
    """
    try:
        logger.info(f'AWS request ID: {context.aws_request_id}')
        logger.info(f'Lambda function ARN: {context.invoked_function_arn}')
        logger.info(f'CloudWatch log stream name: {context.log_stream_name}')
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
        case 'create_teacher':
            return create_teacher_record(body['ItemId'], body['UserName'])

        case 'assign_course':
            return assign_course_to_teacher(
                body['ItemId'], body['CourseId'], body['UserId'])

        case 'get_teacher':
            return get_teacher(query_params['ItemId'])

        case 'get_teacher_courses':
            return get_teacher_courses(query_params['UserId'])

        case 'get_teacher_course_names':
            return get_teacher_course_names(query_params['UserId'])

        case 'get_course_attendance':
            return get_all_course_attendance(query_params['CourseId'])

        case 'update_teacher':
            return update_teacher_record(body['ItemId'], body['UserName'])

        case 'delete_teacher':
            return delete_teacher(query_params['ItemId'])

        case _:
            return make_response(400, 'Invalid operation')
