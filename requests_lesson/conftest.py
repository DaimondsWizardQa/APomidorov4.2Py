import pytest
import requests

@pytest.fixture(scope="session")
def session_req():
    return requests.Session()