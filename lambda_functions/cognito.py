import json
import logging
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('AllData')
UserPoolId = "eu-central-1_jiDMNCeuM"


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

def create_user_record(email, user_name, title):
    try:
        client = boto3.client('cognito-idp')
        response_cognito = client.admin_create_user(
                UserPoolId=UserPoolId,
                Username=email,
                UserAttributes=[
                    {
                        'Name': 'email',
                        'Value': email
                    },
                    {
                        'Name': 'email_verified',
                        'Value': 'false'
                    },
                    {
                        'Name': 'name',
                        'Value': user_name
                    }
                ],
            )
        user_id = response_cognito['User']['Username']

        response_Add_To_Group = client.admin_add_user_to_group(
            UserPoolId=UserPoolId,
            Username=user_id,
            GroupName=title
        )

        response = table.put_item(
            Item={
                'ItemId': user_id,
                'UserName': user_name,
                'ItemType': title
            },
            ConditionExpression='attribute_not_exists(ItemId) AND attribute_not_exists(ItemType)'
        )
        return (response and response_Add_To_Group and response_cognito, None)
    except Exception as e:
        return (False, e)

def create_teacher_record(email, user_name):
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
    result = create_user_record(email, user_name, 'Students')
    if result[0]:
        return make_response(200, 'Record created successfully.')
    return make_response(400, f'Record not created. {result[1]}')

def create_admin_record(email, user_name):
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
    result = create_user_record(email, user_name, 'Admins')
    if result[0]:
        return make_response(200, 'Record created successfully.')
    return make_response(400, f'Record not created. {result[1]}')

def create_student_record(email, user_name):
    """
    Create object for a teacher.

    Args:
        email (str): The email of the user.
        user_name (str): The name of the user.

    Returns:
        dict: The response from the table.put_item() operation.

    Raises:
        ClientError: If an error occurs while putting the item.
    """
    result = create_user_record(email, user_name, '')
    if result[0]:
        return make_response(200, 'Record created successfully.')
    return make_response(400, f'Record not created. {result[1]}')

def lambda_handler(event, context):
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
        case 'create_teacher_record':
            return create_teacher_record(body['email'], body['user_name'])
        case 'create_admin_record':
            return create_admin_record(body['email'], body['user_name'])
        case 'create_student_record':
            return create_student_record(body['email'], body['user_name'])
        case _:
            return make_response(400, 'Invalid operation')