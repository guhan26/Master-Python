
# Simple pytest program

import pytest

def func(x):
    return x +5

def test_methodd():
    assert func(3) == 8

# Multiple test

import pytest

# Markers
@pytest.mark.one
def test_method1():
    x = 5
    y =10
    assert x == y

@pytest.mark.two
def test_method2():
    a = 15
    b = 20
    assert a+5 == b


# Grouping

class TestClass:
    def test_one(self):
        x = "hello"
        assert 'e' in x

    def test_two(self):
        x = 'helloworld'
        assert hasattr(x,"check")

# fixture in pytest

import pytest

@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 25
    return [a,b,c]

# A test that is expected to fail
@pytest.mark.xfail
def test_method1(numbers):
    x = 15
    assert numbers[0] == x

# Skipping a specific test function
@pytest.mark.skip
def test_method2(numbers):
    y = 20
    assert  numbers[1] == y


def test_method3(numbers):
    z = 25
    assert numbers[2] == z



# parametrize in pytest

import pytest

@pytest.mark.parametrize("x,y,z",[(10,20,200),(20,40,200)])
def test_method(x,y,z):
    assert x*y == z

# Test API 

import pytest
import requests
import json

def test_login_valid():
# Define the API endpoint
    url = "https://reqres.in/api/login/"
# Define the login credentials
    data = {'email': 'eve.holt@reqres.in','password':'cityslicka'}
# Send POST request to the API
    response = requests.post(url, data=data)
    token = json.loads(response.text)
# Check that the response status code is 200 (OK)
    assert response.status_code == 200
# Verify that the token in the response matches the expected value
    assert token['token'] == "QpwL5tke4Pnpja7X4"

# Markers

import pytest

# This are the multiple markers
# Annotation
@pytest.mark.login
@pytest.mark.regression
def test_regression():
    print("Test 1")

# A test that is expected to fail
@pytest.mark.xfail
def test_regression2():
    print("Test 1")
    assert 4 == 5


@pytest.mark.sanity
def test_regression2():
    print("Test 1") 

