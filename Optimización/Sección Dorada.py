import math
from tabulate import tabulate

phi = -1 + (1 + math.sqrt(5)) / 2


###MODIFICAR FUNCION###
def function(x: float) -> float:
    return 1.2 * x - math.pow((0.1 * x), 3)


def recalculate(a: float, b: float) -> float:
    x1 = a + phi * (b - a)
    x2 = b - phi * (b - a)

    return x1, x2


def refining(x0: float, x1: float, x2: float) -> float:
    fx0, fx1, fx2 = function(x=x0), function(x=x1), function(x=x2)
    x3 = (
        fx0 * ((x1**2) - (x2**2))
        + fx1 * ((x2**2) - (x0**2))
        + fx2 * ((x0**2) - (x1**2))
    ) / (2 * fx0 * (x1 - x2) + 2 * fx1 * (x2 - x0) + 2 * fx2 * (x0 - x1))
    return x3


def golden_section(a: float, b: float, it: float) -> list:
    data = []

    for i in range(it):
        x1, x2 = recalculate(a=a, b=b)
        fx1, fx2 = function(x=x1), function(x=x2)
        data.append([i + 1, a, b, x1, x2, fx1, fx2])
        if fx1 == fx2:
            a, b = x2, x1
        elif fx1 < fx2:
            b = x1
        else:
            a = x2

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
    if __name__ == "__main__":
        a, b = input("Valores iniciales de a y b: ").split()
        a, b = int(a), int(b)
        it = int(input("Cantidad de iteraciones: "))
        golden_section(a=a, b=b, it=it)


main()
