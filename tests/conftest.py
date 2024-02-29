# conftest.py
import os
import sys
import pytest
from moto import mock_aws
import boto3

# Get the directory containing this file (tests/), then go up one level to project_root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lambda_functions_path = os.path.join(project_root, 'lambda_functions')

# Add the 'lambda_functions' directory to sys.path
if lambda_functions_path not in sys.path:
    sys.path.insert(0, lambda_functions_path)


@pytest.fixture(autouse=True)
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    import os
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    yield
    # Remove the environment variables after the test is done
    os.environ.pop('AWS_ACCESS_KEY_ID', None)
    os.environ.pop('AWS_SECRET_ACCESS_KEY', None)
    os.environ.pop('AWS_SECURITY_TOKEN', None)
    os.environ.pop('AWS_SESSION_TOKEN', None)


@pytest.fixture(scope="function")
def dynamodb(aws_credentials):
    with mock_aws():
        yield boto3.client("dynamodb", region_name="eu-central-1")


@pytest.fixture(scope="function")
def create_dynamodb_table(dynamodb):
    """Create mock DynamoDB table."""
    table_name = "AllData"
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'ItemId', 'KeyType': 'HASH'},
            {'AttributeName': 'ItemType', 'KeyType': 'RANGE'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'ItemId', 'AttributeType': 'S'},
            {'AttributeName': 'UserId', 'AttributeType': 'S'},
            {'AttributeName': 'CourseId', 'AttributeType': 'S'},
            {'AttributeName': 'ItemType', 'AttributeType': 'S'},
            {'AttributeName': 'DepartmentID', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        },
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'CourseIDItemTypeIndex',
                'KeySchema': [
                    {'AttributeName': 'CourseId', 'KeyType': 'HASH'},
                    {'AttributeName': 'ItemType', 'KeyType': 'RANGE'}
                ],
                'Projection': {'ProjectionType': 'ALL'},
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                }
            },
            {
                'IndexName': 'ItemIdDepartmentIDIndex',
                'KeySchema': [
                    {'AttributeName': 'ItemId', 'KeyType': 'HASH'},
                    {'AttributeName': 'DepartmentID', 'KeyType': 'RANGE'}
                ],
                'Projection': {'ProjectionType': 'ALL'},
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                }
            },
            {
                'IndexName': 'UserIDCourseIDIndex',
                'KeySchema': [
                    {'AttributeName': 'UserId', 'KeyType': 'HASH'},
                    {'AttributeName': 'CourseId', 'KeyType': 'RANGE'}
                ],
                'Projection': {'ProjectionType': 'ALL'},
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                }
            }
        ]
    )

    # Wait for the table to be created
    dynamodb.get_waiter('table_exists').wait(TableName=table_name)

    yield dynamodb

    # Clean up
    dynamodb.delete_table(TableName=table_name)
