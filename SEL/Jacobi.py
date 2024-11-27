from sympy import *
from math import e, pi
from tabulate import tabulate


def format(table: list, headers: list) -> None:
    print(
        tabulate(
            table,
            headers=headers,
            tablefmt="pretty",
        )
    )
