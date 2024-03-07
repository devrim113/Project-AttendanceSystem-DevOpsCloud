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
        if response:
            return make_response(200, 'Record created successfully')
        return make_response(400, 'Record creation failed')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


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
        if 'Item' in response:
            return make_response(200, response['Item'])
        return make_response(404, 'Department not found')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


def get_department_courses(dep_id):
    """
    Get the courses for a department.

    Args:
        dep_id (str): The ID of the department.

    Returns:
        list: The list of courses for the department.

    Raises:
        ClientError: If an error occurs while querying the items.
    """
    try:
        response = table.query(
            IndexName='DepartmentIdItemTypeIndex',
            KeyConditionExpression=Key('DepartmentId').eq(
                dep_id) & Key('ItemType').eq('Course')
        )
        if 'Items' in response:
            return make_response(200, response['Items'])
        return make_response(404, 'Courses not found')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


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
        if response:
            return make_response(200, 'Record updated successfully')
        return make_response(400, 'Record update failed')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


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
        if response:
            return make_response(200, 'Record deleted successfully')
        return make_response(404, 'Department not found')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


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
        case 'create_department':
            return create_department(body['ItemId'], body['DepartmentName'])

        case 'get_department':
            return get_department(query_params['ItemId'])

        case 'get_department_courses':
            return get_department_courses(query_params['ItemId'])

        case 'update_department':
            return update_department(body['ItemId'], body['DepartmentName'])

        case 'delete_department':
            return delete_department(query_params['ItemId'])

        case _:
            return make_response(400, 'Invalid operation')
