from fastapi import FastAPI, HTTPException

from app.dao import get_most_used_querry, save_querry
from app.handler import fizzBuzz

app = FastAPI()


def is_int_params_invalide(int_params):
    int_error = []
    for i, name in int_params:
        if not i:
            int_error.append(
                {
                    "code": "internal_error",
                    "detail": f"cannot read {name} : param {name} empty",
                }
            )
        if not i.isnumeric():
            int_error.append(
                {
                    "code": "internal_error",
                    "detail": f"cannot read {name} : param {name} Nan",
                }
            )
    return int_error


def is_str_params_invalide(str_params):
    str_error = []
    for i, name in str_params:
        if not i:
            str_error.append(
                {
                    "code": "internal_error",
                    "detail": f"cannot read {name} : param {name} empty",
                }
            )
        if not i.isalpha():
            str_error.append(
                {
                    "code": "internal_error",
                    "detail": f"cannot read {name} : param {name} Nan",
                }
            )
    return str_error


@app.get("/")
async def root():
    return {"OK"}


@app.get("/v1/stat")
async def stat():
    res = get_most_used_querry()
    print(res)
    return get_most_used_querry()


@app.get("/v1/fizz")
async def fizz_buzz(int1, int2, str1, str2, limit):
    errors = {"errors": []}
    int_params = [(int1, "int1"), (int2, "int2"), (limit, "limit")]
    str_params = [(str1, "str1"), (str2, "str2")]
    errors["errors"] += is_int_params_invalide(int_params)
    errors["errors"] += is_str_params_invalide(str_params)
    if errors["errors"]:
        raise HTTPException(status_code=422, detail=errors)

    modulo_tuple = [(int(int1), str1), (int(int2), str2)]
    save_querry(int1, int2, str1, str2, limit)
    return fizzBuzz(limit=int(limit), n_modulo_string=modulo_tuple)
