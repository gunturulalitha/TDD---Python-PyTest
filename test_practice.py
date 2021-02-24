import pytest
import requests
import json

def func(x):
    return x + 5

@pytest.mark.skip
def test_func():
    assert func(3) == 8

@pytest.mark.xfail
def test_add():
    assert 10 + 10 == 20

''' Parameterix=ze Fixtures '''

@pytest.mark.parametrize("x,y,z",[(10,20,30) , (10,80,90)])
def test_param(x,y,z):
    assert x + y == z

@pytest.mark.parametrize("a,b" , [(10,10)])
def test_param_add(a,b):
    assert a*b == 100


''' Using pytest for testing an API '''
''' Validating Login Details'''

def test_login_check():
    url = "https://reqres.in/api/login"
    data = {    "email": "eve.holt@reqres.in",
                "password": "cityslicka"
           }
    response = requests.get(url , data = data)
    token = json.loads(response.text)
    print("Status Code : " , response.status_code)
    assert response.status_code == 200

def test_division(input_total):
    if input_total % 5 == 0:
        assert True


def test_length():
    assert len("") == 0


def test_str():
    str = "catandapple"
    assert str[6:] == "apple"

def test_str_reverse():
    str = "catandapple"
    assert str[::-1] == "elppadnatac"
