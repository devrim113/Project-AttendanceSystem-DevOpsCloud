"""
This module contains functions for managing attendance records for students in a DynamoDB table.

Functions:
- create_student_record: Create a student record in the database.
- update_attendance_record: Update the attendance record for a student.
- get_student: Retrieves all the attendance records for all courses of a student.
- get_student_course_attendance: Retrieves the attendance record of a student for a specific course.
- delete_student_record: Deletes a student record from the table.
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
table = dynamodb.Table('UserData')


def create_student_record(user_id, course_id, course_name, attendance, user_name):
    """
    Create a student record in the database.

    Args:
        user_id (str): The ID of the student.
        course_id (str): The ID of the course.
        course_name (str): The name of the course.
        attendance (dictionary): The attendance of the student.
            This is a nested object with the following structure:
                attendance = {
                    'date': {
                        'from': (str),
                        'to': (str),
                        'status': (str)
                    }
        user_name (str): The name of the student.

    Returns:
        dict: The response from the database after creating the student record.
            If an error occurs, None is returned.
    """
    try:
        response = table.put_item(
            Item={
                'UserId': user_id,
                'CourseId': course_id,
                'CourseName': course_name,
                'Attendance': attendance,
                'UserName': user_name,
                'UserType': "Student"
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None

# Functions to add or remove one or more attendance records,
# Deemed not necessary for now, just update with entirely new attendance record instead

# def add_attendance_record(user_id, course_id, attendance):
#     update_expression = "SET "
#     expression_attribute_values = {}
#     expression_attribute_names = {}
#     condition_expression = []

#     for i, a in enumerate(attendance):
#         attendance_id = f"{a['date']}_{a['date']['from']}_to_{a['date']['to']}"
#         value_key = f":val{i}"

#         update_expression += f"Attendance.{attendance_id} = {value_key}, "
#         expression_attribute_values[value_key] = a
#         expression_attribute_names[f"#Attendance{i}"] = attendance_id
#         condition_expression.append(
#             f"attribute_not_exists(Attendance.{attendance_id})")

#     # Remove the last comma and space
#     update_expression = update_expression[:-2]

#     try:
#         response = table.update_item(
#             Key={
#                 'UserId': user_id,
#                 'CourseId': course_id
#             },
#             UpdateExpression=update_expression,
#             ExpressionAttributeValues=expression_attribute_values,
#             ExpressionAttributeNames=expression_attribute_names,
#             ConditionExpression=" and ".join(condition_expression),
#             ReturnValues="UPDATED_NEW"
#         )

#         return response

#     except ClientError as e:
#         print(e.response['Error']['Message'])
#         if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
#             print(e.response['Error']['Message'])
#         return None


# def remove_attendance_record(user_id, course_id, attendance):
#     update_expression = "REMOVE "
#     expression_attribute_names = {}

#     for i, a in enumerate(attendance):
#         attendance_id = f"{a['date']}_{a['date']['from']}_to_{a['date']['to']}"
#         expression_attribute_names[f"#Attendance{i}"] = attendance_id
#         update_expression += f"Attendance.{attendance_id}, "

#     # Remove the last comma and space
#     update_expression = update_expression[:-2]

#     try:
#         response = table.update_item(
#             Key={
#                 'UserId': user_id,
#                 'CourseId': course_id
#             },
#             UpdateExpression=update_expression,
#             ExpressionAttributeNames=expression_attribute_names,
#             ReturnValues="UPDATED_NEW"
#         )

#         return response

#     except ClientError as e:
#         print(e.response['Error']['Message'])
#         return None


def update_attendance_record(user_id, course_id, attendance):
    """
    Update the attendance record for a student in a specific course.

    Args:
        user_id (str): The ID of the student.
        course_id (str): The ID of the course.
        attendance (dict): The updated attendance value.

    Returns:
        dict or None: The response from the update operation if successful, None otherwise.
    """
    try:
        response = table.update_item(
            Key={
                'UserId': user_id,
                'CourseId': course_id
            },
            UpdateExpression="SET Attendance = :attendance",
            ExpressionAttributeValues={
                ':attendance': attendance
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


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
        response = table.query(
            KeyConditionExpression=Key('UserId').eq(user_id)
        )
        return response.get('Items')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


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
                'UserId': user_id,
                'CourseId': course_id
            }
        )
        return response.get('Item')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def delete_student_record(user_id, course_id):
    """
    Deletes a student record from the table.

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
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def lambda_handler(event, context):
    """
    Lambda handler function to interact with the DynamoDB table.
    The 'operation' field in the event data determines the action to be performed.
    The following operations are supported:
    - 'put': Creates or updates a student record.
    - 'update': Updates the attendance record for a student.
    - 'get': Retrieves the student record or course attendance record.
    - 'delete': Deletes a student record.

    The corresponding functions called for each operation are:
    - 'put': create_student_record()
    - 'update': update_attendance_record()
    - 'get': get_student_course_attendance() or get_student()
    - 'delete': delete_student_record()

    Args:
        event (dict): The event data passed to the Lambda function.
        context (object): The context object provided by AWS Lambda.

    Returns:
        dict: The response containing the statusCode, body, and headers.
    """

    # Add logging of context information
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

    operation = event.get('operation')

    match operation:
        case 'put':
            response = create_student_record(
                event['UserId'], event['CourseId'], event['CourseName'], event['Attendance'], event['UserName']
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

        case 'update':
            response = update_attendance_record(
                event['UserId'], event['CourseId'], event['Attendance'])
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

        case 'get':
            if 'CourseId' in event:
                item = get_student_course_attendance(
                    event['UserId'], event['CourseId'])
            else:
                item = get_student(event['UserId'])
            if item:
                return {
                    'statusCode': 200,
                    'body': json.dumps(item),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps('Record not found.'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }

        case 'delete':
            response = delete_student_record(
                event['UserId'], event['CourseId'])
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
