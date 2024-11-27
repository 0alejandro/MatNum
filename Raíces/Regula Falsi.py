import math
from sympy import *
from tabulate import tabulate

###AÑADIR VARIABLES###
x = symbols("x", real=True)
###MODIFICAR FUNCION###
expr = (x**3) - 2 * x - 2
data = []


def intervalo(b: float, a0: float, k: float) -> list:
    inter = 1.0 + (b / a0) ** (1 / k)
    if inter > 0:
        return [0, inter]
    else:
        return [inter, 0]


def comprobar(a: float, b: float) -> bool:
    return expr.subs(x, a) * expr.subs(x, b) < 0


def calcular(a: float, b: float):
    res = float(a - ((b - a) / (expr.subs(x, b) - expr.subs(x, a))) * expr.subs(x, a))
    data.append([])
    fx = expr.subs(x, res)
    if res > 0:
        return [res, b, res]
    elif res < 0:
        return [a, res, res]


def error(x, x0):
    return (x - x0) / x


def regulaFalsi(a: float, b: float, errM: float, it: float):
    x = 0

    res = calcular(a, b)
    data.append([0, a, b, res[2], "-"])
    a, b, x = res

    for i in range(it):
        res = calcular(a, b)
        data.append([i + 1, a, b, res[2], error(res[2], x)])
        if errM > error(res[2], x):
            break
        a, b, x = res
    format(table=data, headers=["iteracion", "a", "b", "x", "error"])
    print()


def format(table: list, headers: list) -> None:
    print(
        tabulate(
            table,
            headers=headers,
            tablefmt="pretty",
        )
    )


def main():
    if __name__ == "__main__":
        errM = float(input("Error minimo: "))
        b = float(input("valor absoluto del mayor coeficiente de los negativos: "))
        a0 = float(input("coeficiente de la variable de mayor exponente: "))
        k = float(input("posicion del 1er negativo: "))
        a, b = intervalo(b=b, a0=a0, k=k)
        if comprobar(a, b):
            regulaFalsi(a=a, b=b, errM=errM, it=100)


main()
