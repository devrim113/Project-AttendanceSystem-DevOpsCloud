# This file contains CRUD functions for an AWS Lambda node which interacts with a DynamoDB table
# to store and retrieve teacher data.
# Teachers are also able to change the attendance of students that are in their courses.

#! We need a partition key (PK) of UserId, CourseId, and Date to uniquely identify a record.

import logging
import json
import boto3
from boto3.dynamodb.conditions import Key

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('UserData')

# Create or Update a student record
def put_attendance_record(user_id, course_id, course_name, date, present, user_name, user_type):
    response = table.put_item(
        Item={
            'UserId': user_id,
            'CourseId': course_id,
            'CourseName': course_name,
            'Date': date,
            'Present': present,
            'UserName': user_name,
            'UserType': user_type
        }
    )
    return response

# Read a record
def get_specific_attendance_record(user_id, course_id, date):
    response = table.get_item(
        Key={
            'UserId': user_id,
            'CourseId': course_id,
            'Date': date
        }
    )
    return response.get('Item')

# Read all records for a user
def get_all_student_attendance_records(user_id, course_id):
    response = table.query(
        Key={
            'UserId': user_id,
            'CourseId': course_id
        }
    )
    return response.get('Items')

def get_all_attendance_records(course_id):
    response = table.query(
        Key={
            'CourseId': course_id,
            'UserType': 'Student'
        }
    )
    return response.get('Items')

# Delete a record
def delete_attendance_record(user_id, course_id, date):
    response = table.delete_item(
        Key={
            'UserId': user_id,
            'CourseId': course_id,
            'Date': date
        }
    )
    return response

# Lambda handler example
# Context argument passes in information about the invocation, function, and execution environment.
# This is not necessary for our use case.
def lambda_handler(event, context):
    # Add logging of context information
    try:
        logger.info(f'AWS request ID: {context.aws_request_id}')
        logger.info(f'Lambda function ARN: {context.invoked_function_arn}')
        logger.info(f'CloudWatch log stream name: {context.log_stream_name}')
        logger.info(f'Remaining execution time: {context.get_remaining_time_in_millis()} ms')
    except:
        pass

    operation = event.get('operation')
    
    if operation == 'put':
        response = put_attendance_record(
            event['UserId'], event['CourseId'], event['CourseName'],
            event['Date'], event['Present'], event['UserName'], event['UserType']
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Record created or updated successfully.'),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    elif operation == 'get':
        if event['Date'] == None:
            if event['UserId'] == None:
                item = get_all_attendance_records(event['CourseId'])
            else:
                item = get_all_student_attendance_records(event['UserId'], event['CourseId'])
        else:
            item = get_specific_attendance_record(event['UserId'], event['CourseId'], event['Date'])
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
    elif operation == 'delete':
        delete_attendance_record(event['UserId'], event['CourseId'], event['Date'])
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
            'body': json.dumps('Unsupported operation.'),
            'headers': {
                'Content-Type': 'application/json'
            }
        }