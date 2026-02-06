import pytest
import requests
from pytest_bdd import given, when, then, parsers

@pytest.fixture
def context():
    """Shared context for BDD scenarios"""
    return {
        'base_url': 'https://jsonplaceholder.typicode.com',
        'response': None,
        'headers': {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    }
