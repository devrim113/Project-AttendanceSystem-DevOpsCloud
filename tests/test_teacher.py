import pytest
from teacher import lambda_handler

def test_admin_lambda_handler():
    event = {}
    context = {}
    response = lambda_handler(event, context)
    assert response['statusCode'] == 200
