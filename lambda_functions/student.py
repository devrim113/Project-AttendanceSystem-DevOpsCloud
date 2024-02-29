import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,Access-Control-Allow-Origin'
        },
        'body': json.dumps('Hello from Lambda!')
    }