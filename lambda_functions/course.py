import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',  # Allows requests from any origin
            'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE',  # Adjust based on your needs
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,Access-Control-Allow-Origin'  # Ensure this matches the headers your client may send
        },
        'body': json.dumps('Hello from Lambda!')
    }
