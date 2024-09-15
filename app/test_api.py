from fastapi.testclient import TestClient

from .api import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == ["OK"]


def test_fizz_happy_path():
    response = client.get(
        "/v1/fizz",
        params={
            "int1": "3",
            "int2": "5",
            "str1": "Fizz",
            "str2": "Buzz",
            "limit": "20",
        },
    )
    assert response.status_code == 200
    assert (
        response.content
        == b'["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz","16","17","Fizz","19","Buzz"]'
    )


def test_fizz_with_incorrect_parameter():
    response = client.get(
        "/v1/fizz",
        params={
            "int1": "a",
            "int2": "5",
            "str1": "Fizz",
            "str2": "Buzz",
            "limit": "20",
        },
    )
    assert response.status_code == 422
    assert response.json()["detail"]["errors"] == [
        {"code": "internal_error", "detail": "cannot read int1 : param int1 Nan"}
    ]
