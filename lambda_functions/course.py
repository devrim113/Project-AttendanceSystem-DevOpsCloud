import logging
import json
import boto3
import base64
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
            },
            ConditionExpression='attribute_not_exists(ItemId) AND attribute_not_exists(ItemType)'
        )
        if response:
            return make_response(200, 'Record created or updated successfully.')
        return make_response(400, 'Error creating course')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


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
        if response.get('Item') is not None:
            return make_response(200, response['Item'])
        return make_response(404, 'Course not found')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


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
        if response:
            return make_response(200, 'Record created or updated successfully.')
        return make_response(400, 'Error updating course, not updated')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])


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
        if response:
            return make_response(200, 'Record deleted successfully')
        return make_response(404, 'Course not found')
    except ClientError as e:
        print(e.response['Error']['Message'])
        return make_response(400, 'Request not finished succesfully: ' + e.response['Error']['Message'])

def decode_jwt(token):
    header, payload, signature = token.split(".")

    # Base64 decode and deserialize header 
    header_json = base64.b64decode(header + "==").decode("utf-8")
    header_data = json.loads(header_json)

    # Base64 decode and deserialize payload
    payload_json = base64.b64decode(payload + "==").decode("utf-8")
    payload_data = json.loads(payload_json)

    return header_data, payload_data

def check_permission(token):
    try:
        _ , payload = decode_jwt(token)
        return ("Admins" in payload["cognito:groups"]) or ("Teachers" in payload["cognito:groups"]) or ("Students" in payload["cognito:groups"]) 
    except:
        return False

def lambda_handler(event, context):
    """
    Lambda handler function to interact with the DynamoDB table.
    The function will perform the operation specified in the 'func' query parameter.
    The following operations are supported:
    - create_course: Create a course.
    - get_course: Get a course.
    - update_course: Update a course.
    - delete_course: Delete a course.

    Args:
        event (dict): The event object from the Lambda function.
        context (object): The context object from the Lambda function.

    Returns:
        dict: The response object for the API Gateway.

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


    # try: 
    #     if (not check_permission(event["headers"]['Authorization'])) and (not event["headers"]['Authorization'] == "PYTEST_CODE"):
    #         return make_response(403, "You do not have permission to perform this operation.")
    # except:
    #     return make_response(403, "You do not have permission to perform this operation.")
    
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
        case 'create_course':
            return create_course(body['ItemId'], body['CourseName'], body['DepartmentId'], body['Classes'])

        case 'get_course':
            return get_course(query_params['ItemId'])

        case 'update_course':
            return update_course(body['ItemId'], body['CourseName'], body['DepartmentId'], body['Classes'])

        case 'delete_course':
            return delete_course(query_params['ItemId'])

        case _:
            return make_response(400, 'Invalid operation')
