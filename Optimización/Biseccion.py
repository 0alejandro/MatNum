import math
from sympy import *
from tabulate import tabulate
from random import *


###MODIFICAR DELTA###
delta = 0.5


###MODIFICAR FUNCION###
def function(x: float) -> float:
    return 1.2 * x - pow((0.1 * x), 3)


def recalculate(a: float, b: float) -> float:
    x1 = (a + b) / 2 - delta / 2
    x2 = (a + b) / 2 + delta / 2

    return x1, x2


def refining(x0: float, x1: float, x2: float) -> float:
    fx0, fx1, fx2 = function(x=x0), function(x=x1), function(x=x2)
    x3 = (
        fx0 * ((x1**2) - (x2**2))
        + fx1 * ((x2**2) - (x0**2))
        + fx2 * ((x0**2) - (x1**2))
    ) / (2 * fx0 * (x1 - x2) + 2 * fx1 * (x2 - x0) + 2 * fx2 * (x0 - x1))
    return x3


def biseccion(a: float, b: float, it: float) -> list:
    data = []

    for i in range(it):
        x1, x2 = recalculate(a=a, b=b)
        fx1, fx2 = function(x=x1), function(x=x2)
        data.append([i + 1, a, b, x1, x2, fx1, fx2])
        if fx1 == fx2:
            a, b = x2, x1
        elif fx1 < fx2:
            a = x1
        else:
            b = x2

    ref = refining(x0=a, x1=b, x2=(a + b) / 2)

    format(table=data, headers=["it", "a", "b", "x1", "x2", "fx1", "fx2"])
    format(
        table=[[a, b, ref, function(ref), round(ref), round(function(ref))]],
        headers=[
            "a",
            "b",
            "refinamiento",
            "f(refinamiento)",
            "refinamiento aprox",
            "f(refinamiento aprox)",
        ],
    )


def format(table: list, headers: list) -> None:
    print(
        tabulate(
            table,
            headers=headers,
            tablefmt="pretty",
        )
    )


def main():
    a, b = input("Valores iniciales de a y b: ").split()
    a, b = int(a), int(b)
    it = int(input("Cantidad de iteraciones: "))
    biseccion(a=a, b=b, it=it)


main()
