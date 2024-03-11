import boto3

def lambda_handler(event, context):
    username = event.get('userName', None)
    if(username == None):
        return {'status': 'No username provided', 'statusCode': 400}
    
    iam_client = boto3.client('iam')
    
    is_admin = event.get('clientMetadata', {}).get("isAdmin", False)
    is_teacher = event.get('clientMetadata', {}).get("isTeacher", False)

    group_name = 'Students'
    if is_teacher:
        group_name = 'Teachers'
    elif is_admin:
        group_name = 'Admins'

    try:
        response = iam_client.add_user_to_group(
            GroupName=group_name,
            UserName=username
        )
        return {'status': 'User added to group successfully', 'statusCode': 200}
    
    except Exception as e:
        print(e)
        return {'status': 'Failed to add user to group',  'statusCode': 502}

