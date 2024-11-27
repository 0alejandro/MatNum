from sympy import *
from math import e, pi
from tabulate import tabulate

###AÑADIR VARIABLES###
x = symbols("x")
###MODIFICAR FUNCION###
expr = 1.8 - 7 * exp(-0.04 * x)


def funcion(num: float) -> float:
    return expr.subs(x, num)


def derivada(num: float):
    return diff(expr).subs(x, num)


def format(table: list, headers: list) -> None:
    print(
        tabulate(
            table,
            headers=headers,
            tablefmt="pretty",
        )
    )


def newton(num0: float, errM: float, it: int) -> float:
    data = []
    num, err = 0, 1e9

    num = num0 - (funcion(num0) / derivada(num0))
    err = abs(num - num0) / abs(num)
    num0 = num
    data.append([0, num, "-"])

    for i in range(it + 1):
        num = num0 - (funcion(num0) / derivada(num0))
        err = abs(num - num0) / abs(num)
        if num == num0 or err < errM:
            break
        num0 = num
        data.append([i + 1, num, err])

    format(table=data, headers=["iteracion", "x", "error"])


def main():
    if __name__ == "__main__":
        num0 = float(input("Valor inicial: "))
        errM = float(input("Error minimo: "))
        newton(num0=num0, errM=errM, it=100)


main()
