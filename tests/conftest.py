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

@pytest.fixture(scope="session")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    import os
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"

@pytest.fixture(scope="session")
def dynamodb(aws_credentials):
    with mock_aws():
        yield boto3.client("dynamodb", region_name="eu-central-1")

@pytest.fixture(scope="session")
def create_dynamodb_table(dynamodb):
    """Create mock DynamoDB table."""
    table_name = "UserData"
    dynamodb.create_table(
        TableName='UserData',
        KeySchema=[
            {'AttributeName': 'UserId', 'KeyType': 'HASH'},
            {'AttributeName': 'CourseId', 'KeyType': 'RANGE'}
            # Add Date as part of the attribute definitions if using it in KeySchema or as an index
        ],
        AttributeDefinitions=[
            {'AttributeName': 'UserId', 'AttributeType': 'S'},
            {'AttributeName': 'CourseId', 'AttributeType': 'S'},
            # {'AttributeName': 'Date', 'AttributeType': 'S'}  # If using Date in keys or indexes
        ],
        ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
    )
    return table_name
