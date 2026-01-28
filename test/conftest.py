import pytest
import random

@pytest.fixture(scope='function')
def function_scope():
    return random.randint(1, 99)


@pytest.fixture(scope='class')
def class_scope():
    return random.randint(100, 200)


@pytest.fixture(scope='module')
def module_scope():
    return random.randint(200, 299)

@pytest.fixture(scope='session')
def session_scope():
    return random.randint(300, 399)

