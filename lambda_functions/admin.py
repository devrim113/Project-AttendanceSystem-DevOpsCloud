# This file contains CRUD functions for an AWS Lambda node which interacts with a DynamoDB table
# to store and retrieve student data.

#! We need a partition key (PK) of UserId, CourseId, and Date to uniquely identify a record.

import logging
import json
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('AllData')


def create_admin_record(item_id, user_name):
    """
    Create object for an admin record.

    Args:
        item_id (str): The ID of the admin record.
        user_name (str): The name of the admin.

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
                'ItemType': 'Admin'
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def update_admin_record(item_id, user_name):
    """
    Update an admin record.

    Args:
        item_id (str): The ID of the admin record.
        user_name (str): The name of the admin.

    Returns:
        dict: The response from the table.update_item() operation.

    Raises:
        ClientError: If an error occurs while updating the item.
    """
    try:
        response = table.update_item(
            Key={
                'ItemId': item_id,
                'ItemType': 'Admin'
            },
            UpdateExpression="set UserName=:n",
            ExpressionAttributeValues={
                ':n': user_name
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None

# This is not possible as the ItemType is part of the primary key and cannot be updated.
# To do this, we would need to delete the record and create a new one.
# def update_user_type(item_id, item_type):
#     """
#     Update the user type for a user record.

#     Args:
#         item_id (str): The ID of the admin record.
#         item_type (str): The type of the admin.

#     Returns:
#         dict: The response from the table.update_item() operation.

#     Raises:
#         ClientError: If an error occurs while updating the item.
#     """
#     try:
#         response = table.update_item(
#             Key={
#                 'ItemId': item_id
#             },
#             UpdateExpression="set ItemType=:t",
#             ExpressionAttributeValues={
#                 ':t': item_type
#             },
#             ReturnValues="UPDATED_NEW"
#         )
#         return response
#     except ClientError as e:
#         print(e.response['Error']['Message'])
#         return None


def delete_admin_record(item_id):
    """
    Delete an admin record.

    Args:
        item_id (str): The ID of the admin record.

    Returns:
        dict: The response from the table.delete_item() operation.

    Raises:
        ClientError: If an error occurs while deleting the item.
    """
    try:
        response = table.delete_item(
            Key={
                'ItemId': item_id,
                'ItemType': 'Admin'
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def get_admin_record(item_id):
    """
    Get an admin record.

    Args:
        item_id (str): The ID of the admin record.

    Returns:
        dict: The response from the table.get_item() operation.

    Raises:
        ClientError: If an error occurs while getting the item.
    """
    try:
        response = table.get_item(
            Key={
                'ItemId': item_id,
                'ItemType': 'Admin'
            }
        )
        return response.get('Item')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


# Lambda handler example
# Context argument passes in information about the invocation, function, and execution environment.
# This is not necessary for our use case.


def lambda_handler(event, context):
    """
    Lambda handler for the admin.
    The 'operation' field in the event data determines the action to be performed.
    The following operations are supported:
    - 'put': Creates a new record for an admin.
    - 'update': Updates an admin record.
    - 'delete': Deletes an admin record.
    - 'get': Retrieves an admin record.

    The corresponding functions called for each operation are:
    - 'put': create_admin_record()
    - 'update': update_admin_record()
    - 'delete': delete_admin_record()
    - 'get': get_admin_record()

    Args:
        event (dict): The event object.
        context (object): The context object.

    Returns:
        dict: The response object.
    """

    # Add logging of context information
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
            response = create_admin_record(
                event['ItemId'], event['UserName'])
            if response:
                return {
                    'statusCode': 200,
                    'body': json.dumps('Admin record created successfully'),
                    'headers': {
                        'Content-Type': 'application/json',
                    }
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Error creating admin record'),
                    'headers': {
                        'Content-Type': 'application/json',
                    }
                }
        case 'update':
            # if 'UserName' in event:
            response = update_admin_record(
                event['ItemId'], event['UserName'])
            # else:
            #     response = update_user_type(
            #         event['ItemId'], event['ItemType'])
            if response:
                return {
                    'statusCode': 200,
                    'body': json.dumps('Admin record updated successfully'),
                    'headers': {
                        'Content-Type': 'application/json',
                    }
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Error updating admin record'),
                    'headers': {
                        'Content-Type': 'application/json',
                    }
                }

        case 'delete':
            response = delete_admin_record(event['ItemId'])
            if response:
                return {
                    'statusCode': 200,
                    'body': json.dumps('Admin record deleted successfully'),
                    'headers': {
                        'Content-Type': 'application/json',
                    }
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Error deleting admin record'),
                    'headers': {
                        'Content-Type': 'application/json',
                    }
                }

        case 'get':
            response = get_admin_record(event['ItemId'])
            if response:
                return {
                    'statusCode': 200,
                    'body': json.dumps(response),
                    'headers': {
                        'Content-Type': 'application/json',
                    }
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Error getting admin records'),
                    'headers': {
                        'Content-Type': 'application/json',
                    }
                }

        case _:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid operation'),
                'headers': {
                    'Content-Type': 'application/json',
                }
            }
