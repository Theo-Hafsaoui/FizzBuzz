modulo_string = [
    (3, "Fizz"),
    (5, "Buzz"),
]


def fizzBuzz(limit: int, n_modulo_string=modulo_string) -> list[str]:
    """
    Take a range k to n and return the string representation of the number
    at the exeption of the mutiple of 3 and 5 where rsp subtistute to `Fizz` and `Buzz`
    """
    res = []
    for i in range(1, limit + 1):
        new_value = ""
        for mod in n_modulo_string:
            if i % mod[0] == 0:
                new_value += mod[1]
        if not new_value:
            new_value = str(i)
        res.append(new_value)
    return res
