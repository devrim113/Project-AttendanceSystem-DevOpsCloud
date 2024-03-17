import json
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

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

def lambda_handler(event, context):
    user_id = event['userName']
    try:
        name = event['request']['userAttributes']['name']
    except:
        name = "Unknown"
    userPoolId = event['userPoolId']
    try:
        client = boto3.client('cognito-idp')
        response_Add_To_Group = client.admin_add_user_to_group(
            UserPoolId=userPoolId,
            Username=user_id,
            GroupName="Students"
        )

        response = table.put_item(
            Item={
                'ItemId': user_id,
                'UserName': name,
                'ItemType': "Students"
            },
            ConditionExpression='attribute_not_exists(ItemId) AND attribute_not_exists(ItemType)'
        )
        return make_response(200, "User added to group and table")
    except Exception as e:
        return make_response(403, f"Something went wrong. Please try again. Error: {str(e)}" )