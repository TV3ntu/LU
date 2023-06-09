import numpy as np
from tabulate import tabulate


def count_operations_L(n):
    """
    Calcula el número de operaciones elementales en el peor caso para despejar y en Ly = b
    :param n:
    :return:
    """
    # Matriz triangular inferior L tiene n(n+1)/2 elementos no nulos
    return n * (n + 1) // 2


def count_operations_U(n):
    """
    Calcula el número de operaciones elementales en el peor caso para despejar x en Ux = y
    :param n:
    :return:
    """
    # Matriz triangular superior U tiene n(n+1)/2 elementos no nulos
    return n * (n + 1) // 2


def count_operations_total(n):
    """
    Calcula el número total de operaciones elementales en el peor caso para las etapas (a) y (b) del método LU
    :param n:
    :return:
    """
    return count_operations_L(n) + count_operations_U(n)


# Ejemplo de uso:
n = np.random.randint(2, 6)  # Tamaño de la matriz A
A = np.random.rand(n, n)  # Matriz A aleatoria de tamaño nxn
b = np.random.rand(n, 1)  # Vector b aleatorio de tamaño nx1
print("Matriz A:")
print(tabulate(A, tablefmt="fancy_grid"))
print("Vector b:")
print(tabulate(b, tablefmt="fancy_grid"))
print("n:", n)

# Calcular el número de operaciones elementales en el peor caso para despejar y en Ly = b
operations_L = count_operations_L(n)
print("Operaciones elementales para despejar y en Ly = b:", operations_L)

# Calcular el número de operaciones elementales en el peor caso para despejar x en Ux = y
operations_U = count_operations_U(n)
print("Operaciones elementales para despejar x en Ux = y:", operations_U)

# Calcular el número total de operaciones elementales en el peor caso para las etapas (a) y (b) del método LU
operations_total = count_operations_total(n)
print("Operaciones elementales totales para las etapas (a) y (b):", operations_total)
