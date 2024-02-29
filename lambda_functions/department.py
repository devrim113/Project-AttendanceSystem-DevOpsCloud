import logging
import json
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('UserData')


def create_department(dep_id, dep_name):
    """
    Create object for a department.

    Args:
        dep_id (str): The ID of the department.
        dep_name (str): The name of the department.

    Returns:
        dict: The response from the table.put_item() operation.

    Raises:
        ClientError: If an error occurs while putting the item.
    """
    try:
        response = table.put_item(
            Item={
                'ItemId': dep_id,
                'DepartmentName': dep_name,
                'ItemType': 'Department'
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def get_department(dep_id):
    """
    Get a department.

    Args:
        dep_id (str): The ID of the department.

    Returns:
        dict: The department object.

    Raises:
        ClientError: If an error occurs while getting the item.
    """
    try:
        response = table.get_item(
            Key={
                'ItemId': dep_id,
                'ItemType': 'Department'
            }
        )
        return response['Item']
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def update_department(dep_id, dep_name):
    """
    Update object for a department.

    Args:
        dep_id (str): The ID of the department.
        dep_name (str): The name of the department.

    Returns:
        dict: The response from the table.put_item() operation.

    Raises:
        ClientError: If an error occurs while putting the item.
    """
    try:
        response = table.update_item(
            Key={
                'ItemId': dep_id,
                'ItemType': 'Department'
            },
            UpdateExpression='SET DepartmentName = :val1',
            ExpressionAttributeValues={
                ':val1': dep_name
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def delete_department(dep_id):
    """
    Delete a department.

    Args:
        dep_id (str): The ID of the department.

    Returns:
        dict: The response from the table.delete_item() operation.

    Raises:
        ClientError: If an error occurs while deleting the item.
    """
    try:
        response = table.delete_item(
            Key={
                'ItemId': dep_id,
                'ItemType': 'Department'
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def lambda_handler(event, context):
    """
    Lambda handler for the department.
    The 'operation' field in the event data determines the action to be performed.
    The following operations are supported:
    - 'put': Creates a new record for a department.
    - 'get': Retrieves a department.
    - 'update': Updates a record for a department.
    - 'delete': Deletes a record for a department.

    The corresponding functions called for each operation are:
    - 'put': create_department()
    - 'get': get_department()
    - 'update': update_department()
    - 'delete': delete_department()

    Args:
        event (dict): The event object.
        context (object): The context object.

    Returns:
        dict: The response object.

    Raises:
        ValueError: If the operation is not supported.
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
            response = create_department(
                event['DepartmentId'], event['DepartmentName'])
            if response:
                return {
                    'statusCode': 200,
                    'body': json.dumps('Department created successfully'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Department creation failed'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }

        case 'get':
            response = get_department(event['DepartmentId'])
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
                    'body': json.dumps('Department not found'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }

        case 'update':
            response = update_department(
                event['DepartmentId'], event['DepartmentName'])
            if response:
                return {
                    'statusCode': 200,
                    'body': json.dumps('Department updated successfully'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Department update failed'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }

        case 'delete':
            response = delete_department(event['DepartmentId'])
            if response:
                return {
                    'statusCode': 200,
                    'body': json.dumps('Department deleted successfully'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Department deletion failed'),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }

        case _:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid operation'),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }
