from contextlib import contextmanager
from collections.abc import Iterator
import time
from typing import Any


def fibonacci_spiral(n):
    # Проверка, что заданное количество не меньше нуля
    if n <= 0:
        return "Количество должно быть положительным числом"

    # Создание матрицы для спирали Фибоначчи
    matrix = [[0] * n for _ in range(n)]

    # Инициализация первой строки
    for i in range(n):
        matrix[i][0] = i + 1

    # Инициализация первого столбца
    for i in range(n):
        matrix[0][i] = i + 1

    # Заполнение остальных элементов спирали
    for layer in range(2, n):
        for i in range(layer, n):
            matrix[i - layer][layer - 1] = matrix[i - layer][layer - 2] + matrix[i - layer + 1][layer - 2]
        for i in range(layer - 1, 0, -1):
            matrix[i][n - layer] = matrix[i - 1][n - layer] + matrix[i][n - layer - 1]

    return matrix


@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    finally:
        return print(time.time() - start)



with timer() as times:
    new = []
    # Пример использования функц
    for row in fibonacci_spiral(280):
        new.append(row)

    times



