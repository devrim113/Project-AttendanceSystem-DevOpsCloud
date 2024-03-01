import logging
import json
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('AllData')


def create_course(item_id, course_name, department_id, classes):
    """
    Create object for a course.

    Args:
        item_id (str): The ID of the course.
        course_name (str): The name of the course.
        department_id (str): The ID of the department.
        classes (dict): The classes for the course.

    Returns:
        dict: The response from the table.put_item() operation.

    Raises:
        ClientError: If an error occurs while putting the item.
    """
    try:
        response = table.put_item(
            Item={
                'ItemId': item_id,
                'CourseName': course_name,
                'DepartmentId': department_id,
                'ItemType': 'Course',
                'Classes': classes
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def get_course(item_id):
    """
    Get a course.

    Args:
        item_id (str): The ID of the course.

    Returns:
        dict: The course object.

    Raises:
        ClientError: If an error occurs while getting the item.
    """
    try:
        response = table.get_item(
            Key={
                'ItemId': item_id,
                'ItemType': 'Course'
            }
        )
        return response['Item']
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def update_course(item_id, course_name, department_id, classes):
    """
    Update object for a course.

    Args:
        item_id (str): The ID of the course.
        course_name (str): The name of the course.
        department_id (str): The ID of the department.
        classes (dict): The classes for the course.

    Returns:
        dict: The response from the table.update_item() operation.

    Raises:
        ClientError: If an error occurs while updating the item.
    """
    try:
        response = table.update_item(
            Key={
                'ItemId': item_id,
                'ItemType': 'Course'
            },
            UpdateExpression="set CourseName = :n, DepartmentId = :d, Classes = :c",
            ExpressionAttributeValues={
                ':n': course_name,
                ':d': department_id,
                ':c': classes
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def delete_course(item_id):
    """
    Delete a course.

    Args:
        item_id (str): The ID of the course.

    Returns:
        dict: The response from the table.delete_item() operation.

    Raises:
        ClientError: If an error occurs while deleting the item.
    """
    try:
        response = table.delete_item(
            Key={
                'ItemId': item_id,
                'ItemType': 'Course'
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def lambda_handler(event, context):
    """
    Lambda handler.

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

    operation = event.get('operation')
    match operation:
        case 'put':
            response = create_course(
                event['ItemId'], event['CourseName'], event['DepartmentId'], event['Classes'])
            if response:
                return {
                    'statusCode': 200,
                    'body': json.dumps('Record created or updated successfully.'),
                    'headers': {
                        'Content-Type': 'application/json',
                    }
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Error creating course'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
        case 'get':
            response = get_course(event['ItemId'])
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
                    'statusCode': 404,
                    'body': json.dumps('Course not found'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
        case 'update':
            response = update_course(
                event['ItemId'], event['CourseName'], event['DepartmentId'], event['Classes'])
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
                    'body': json.dumps('Error updating course'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
        case 'delete':
            response = delete_course(event['ItemId'])
            if response:
                return {
                    'statusCode': 200,
                    'body': json.dumps('Record deleted successfully'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Error deleting course'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
        case _:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid operation')
            }
