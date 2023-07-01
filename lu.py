import numpy as np
import math


def check_determinant_non_zero(matrix):
    """
    Verifica que el determinante de una matriz sea distinto de cero.
    :param matrix:
    :return:
    """
    determinant = np.linalg.det(matrix)
    return determinant != 0


def read_matrix_row_by_column(n):
    """
    Lee una matriz de nxn por filas y columnas.
    :param n:
    :return:
    """
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            element = int(input(f"Ingrese el elemento ({i}, {j}) de la matriz: "))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)


def decompose_LU(matrix):
    """
    Descompone una matriz cuadrada en una matriz triangular inferior y una matriz triangular superior.
    :param matrix:
    :return:
    """
    n = matrix.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for k in range(n):
        L[k, k] = 1
        for j in range(k, n):
            U[k, j] = matrix[k, j] - np.dot(L[k, :k], U[:k, j])
        for i in range(k + 1, n):
            L[i, k] = (matrix[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k]

    return L, U


def solve_LU(matrix, vector):
    """
    Resuelve un sistema de ecuaciones lineales de la forma Ax = vector, donde A es una matriz cuadrada.
    :param matrix:
    :param vector:
    :return:
    """
    L, U = decompose_LU(matrix)
    y = forward_substitution(L, vector)
    x = backward_substitution(U, y)
    return x


def forward_substitution(L, vector):
    """
    Resuelve un sistema de ecuaciones lineales de la forma Ly = vector, donde L es una matriz triangular inferior.
    :param L:
    :param vector:
    :return:
    """
    n = L.shape[0]
    y = np.zeros(n)
    for i in range(n):
        y[i] = vector[i] - np.dot(L[i, :i], y[:i])
    return y


def backward_substitution(U, vector):
    """
    Resuelve un sistema de ecuaciones lineales de la forma Ux = vector, donde U es una matriz triangular superior.
    :param U:
    :param vector:
    :return:
    """
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if U[i, i] != 0:
            x[i] = (vector[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
        else:
            raise ZeroDivisionError("División entre cero encontrada en el cálculo de x[i]")
    return x


def count_elementary_operations(n):
    """
    Calcula la cantidad de operaciones elementales necesarias para resolver un sistema de ecuaciones de nxn.
    :param n:
    :return:
    """
    forward_sub_count = math.ceil((n ** 2) / 2)
    backward_sub_count = math.ceil(n * (n + 1) / 2)
    total_operations = forward_sub_count + backward_sub_count
    return forward_sub_count, backward_sub_count, total_operations


def generate_nonzero_determinant_matrix(n):
    """
    Genera una matriz cuadrada de nxn con determinante distinto de cero.
    :param n:
    :return:
    """
    matrix = np.random.rand(n, n)
    while np.linalg.det(matrix) == 0:
        matrix = np.random.rand(n, n)
    return matrix


def main():
    print("\n\t\tTrabajo Practico LU\n")
    print("\tIntegrantes:\n\t\tAgustin Narvaez, Tomas Venturini")
    print()
    print("""Consigna:
    Para resolver la ecuacion matricial Ax = b, el metodo LU, cuando es factible, lleva tres etapas. Tomamos aqui solo las dos ultimas, 
    y pedimos que para estas calculen cuantas operaciones elementales seran necesarias en el peor caso, dada A una matriz de nxn 
    y dado b un vector de nx1.
    a) Determinar en funcion de n cuantas operaciones elementales lleva en el peor caso despejar el vector y en la ecuacion matricial Ly = b.
    b) Determinar en funcion de n cuantas operaciones elementales lleva en el peor caso despejar el vector x en la ecuacion matricial Ux = y.
    c) Determinar la cantidad total de operaciones elementales necesarias para resolver el sistema Ax = b utilizando el metodo LU.
    """)
    n = int(input("Ingrese la dimensión de la matriz cuadrada A: "))
    option = 0
    while option != 1 and option != 2:
        option = int(input("Ingrese 1 para ingresar la matriz A manualmente o 2 para generar una matriz aleatoria: "))
        if option == 1:
            A = read_matrix_row_by_column(n)
        elif option == 2:
            A = generate_nonzero_determinant_matrix(n)
            print(f"La matriz A generada es:\n{A}")
        else:
            print("Opción inválida.")
    b = np.array(input("Ingrese el vector b separado por espacios: ").split(), dtype=int)

    if check_determinant_non_zero(A):
        forward_count, backward_count, total_count = count_elementary_operations(n)
        print(f"\nOperaciones elementales para despejar y: {forward_count}")
        print(f"Operaciones elementales para despejar x: {backward_count}")
        print(f"Total de operaciones elementales necesarias: {total_count}\n")
        x = solve_LU(A, b)
        print(f"La solución del sistema es x = {x}")
    else:
        print("La matriz A tiene determinante cero. El método LU no es factible para resolver el sistema.")


main()
