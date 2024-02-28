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
table = dynamodb.Table('UserData')


def put_attendance_record(user_id, course_id, course_name, user_name):
    """
    Put attendance record for a teacher.

    Args:
        user_id (str): The ID of the user.
        course_id (str): The ID of the course.
        course_name (str): The name of the course.
        user_name (str): The name of the user.

    Returns:
        dict: The response from the table.put_item() operation.

    Raises:
        ClientError: If an error occurs while putting the item.
    """
    try:
        response = table.put_item(
            Item={
                'UserId': user_id,
                'CourseId': course_id,
                'CourseName': course_name,
                'UserName': user_name,
                'UserType': 'Teacher'
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def get_all_courses(user_id):
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
            KeyConditionExpression=Key('UserId').eq(user_id)
        )
        return response['Items']
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
            IndexName='CourseIDUserTypeIndex',
            KeyConditionExpression=Key('CourseId').eq(
                course_id) & Key('UserType').eq('Student')
        )
        return response['Items']
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def delete_attendance_record(user_id, course_id):
    """
    Delete attendance record for a teacher.

    Args:
        user_id (str): The ID of the user.
        course_id (str): The ID of the course.

    Returns:
        dict: The response from the table.delete_item() operation.

    Raises:
        ClientError: If an error occurs while deleting the item.
    """
    try:
        response = table.delete_item(
            Key={
                'UserId': user_id,
                'CourseId': course_id
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
    - 'delete': Deletes a record for a teacher.

    The corresponding functions called for each operation are:
    - 'put': put_attendance_record()
    - 'get': get_all_course_attendance() or get_all_courses()
    - 'delete': delete_attendance_record()

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
            response = put_attendance_record(
                event['UserId'], event['CourseId'], event['CourseName'],
                event['UserName']
            )
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
            if 'CourseId' in event:
                response = get_all_course_attendance(event['CourseId'])
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
            else:
                response = get_all_courses(event['UserId'])
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
                        'body': json.dumps('No courses found.'),
                        'headers': {
                            'Content-Type': 'application/json'
                        }
                    }
        case 'delete':
            response = delete_attendance_record(
                event['UserId'], event['CourseId']
            )
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
