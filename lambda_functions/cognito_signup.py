import json
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('AllData')

def lambda_handler(event, context):
    user_id = event['userName']
    # try:
    name = event['request']['userAttributes'].get('name', "Unknown")
    userPoolId = event['userPoolId']

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
            'ItemType': "Student"
        },
        ConditionExpression='attribute_not_exists(ItemId) AND attribute_not_exists(ItemType)'
    )
    # except Exception as e:
    #     print(f"Error processing user {user_id}: {str(e)}")
    #     e["error"] = str(e)

    # Always return the event object in its expected format for Cognito triggers
    return event
