import pytest

from app.handler import fizzBuzz


@pytest.mark.parametrize(
    "limit, expected",
    [
        (2, ["1", "2"]),
        (3, ["1", "2", "Fizz"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (
            15,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        ),
    ],
)
def test_fizz_buzz(limit, expected):
    assert fizzBuzz(limit) == expected


def test_should_return_nb():
    got = fizzBuzz(2)
    want = ["1", "2"]
    assert got == want


def test_should_return_Fizz_at_the_end():
    got = fizzBuzz(3)[-1]
    want = "Fizz"
    assert got == want


def test_should_return_Buzz_at_the_end():
    got = fizzBuzz(5)[-1]
    want = "Buzz"
    assert got == want


def test_should_return_fizzBuzz_at_the_end():
    got = fizzBuzz(15)[-1]
    want = "FizzBuzz"
    assert got == want
