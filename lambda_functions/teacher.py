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


def create_teacher_record(item_id, user_name):
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
    try:
        response = table.put_item(
            Item={
                'ItemId': item_id,
                'UserName': user_name,
                'ItemType': 'Teacher'
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


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
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


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
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


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
        if 'Item' not in response:
            return None
        return response['Item']
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


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
            IndexName='UserIDCourseIDIndex',
            KeyConditionExpression=Key('UserId').eq(user_id)
        )
        return response.get('Items')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def get_all_course_attendance(course_id):
    """
    Get all attendance records of students for a teacher's course.
    Uses the Global Secondary Index CourseIDUserTypeIndex to query the table.

    Args:
        course_id (str): The ID of the course.

    Returns:
        list: The list of attendance records for the teacher's course.

    Raises:
        ClientError: If an error occurs while getting the items.
    """
    try:
        response = table.query(
            IndexName='CourseIDItemTypeIndex',
            KeyConditionExpression=Key('CourseId').eq(
                course_id) & Key('ItemType').eq('Attendance')
        )
        return response['Items']
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


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
    try:
        response = table.delete_item(
            Key={
                'ItemId': user_id,
                'ItemType': 'Teacher'
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


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

    operation = event.get('operation')
    match operation:
        case 'put':
            if 'ItemType' in event and event['ItemType'] == 'TeachesCourse':
                response = assign_course_to_teacher(
                    event['ItemId'], event['CourseId'], event['UserId'])
            else:
                response = create_teacher_record(
                    event['ItemId'], event['UserName'])
            if response:
                return {
                    'statusCode': 200,
                    'body': json.dumps('Record created or updated successfully.'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Record not created or updated.'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }

        case 'get':
            if 'ItemType' in event and event['ItemType'] == 'Teacher':
                response = get_teacher(event['ItemId'])
            elif 'CourseId' in event:
                response = get_all_course_attendance(event['CourseId'])
            else:
                response = get_teacher_courses(event['UserId'])
            if response:
                return {
                    'statusCode': 200,
                    'body': json.dumps(response),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('No records found.'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }

        case 'update':
            response = update_teacher_record(
                event['ItemId'], event['UserName'])
            if response:
                return {
                    'statusCode': 200,
                    'body': json.dumps('Record updated successfully.'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Record not updated.'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }

        case 'delete':
            response = delete_teacher(event['ItemId'])
            if response:
                return {
                    'statusCode': 200,
                    'body': json.dumps('Record deleted successfully.'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Record not deleted.'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }

        case _:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid operation.'),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }
