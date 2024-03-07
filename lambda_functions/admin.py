# This file contains CRUD functions for an AWS Lambda node which interacts with a DynamoDB table
# to store and retrieve student data.

import logging
import json
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

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
        if response:
            return make_response(200, 'Admin record created successfully')
        return make_response(400, 'Error creating admin record')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


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
        if response:
            return make_response(200, 'Admin record updated successfully')
        return make_response(400, 'Error updating admin record')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])

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
        if response:
            return make_response(200, 'Admin record deleted successfully')
        return make_response(404, 'Admin not found')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


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
        if 'Item' in response:
            return make_response(200, response['Item'])
        return make_response(404, 'Admin not found')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


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
        case 'create_admin':
            return create_admin_record(body['ItemId'], body['UserName'])

        case 'update_admin':
            return update_admin_record(body['ItemId'], body['UserName'])

        case 'get_admin':
            return get_admin_record(query_params['ItemId'])

        case 'delete_admin':
            return delete_admin_record(query_params['ItemId'])

        case _:
            return make_response(400, 'Invalid operation')
