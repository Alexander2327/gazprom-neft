import sys
from typing import List


def is_safe_cell(mat: List[list], visited: List[list], x: int, y: int) -> bool:
    """Функция проверяет возможность перехода к ячейке"""

    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and \
           not (mat[x][y] == 1 or visited[x][y])


def find_shortest(mat: List[list], visited: List[list], i: int, j: int, dest: tuple,
                  min_dist: int = sys.maxsize, dist: int = 0) -> int:
    """Рекурсивная функция поиска кратчайшего пути"""

    if (i, j) == dest:
        return min(dist, min_dist)

    visited[i][j] = 1

    if is_safe_cell(mat, visited, i + 1, j):
        min_dist = find_shortest(mat, visited, i + 1, j, dest, min_dist, dist + 1)

    if is_safe_cell(mat, visited, i, j + 1):
        min_dist = find_shortest(mat, visited, i, j + 1, dest, min_dist, dist + 1)

    if is_safe_cell(mat, visited, i - 1, j):
        min_dist = find_shortest(mat, visited, i - 1, j, dest, min_dist, dist + 1)

    if is_safe_cell(mat, visited, i, j - 1):
        min_dist = find_shortest(mat, visited, i, j - 1, dest, min_dist, dist + 1)

    visited[i][j] = 0

    return min_dist


def shortest_path(mat: List[list], src: tuple, dest: tuple) -> int:
    """ Функция поиска кратчайшего пути.
    Возвращает число, если путь найден, иначе -1"""

    i, j = src
    x, y = dest

    if not mat or len(mat) == 0 or mat[i][j] == 1 or mat[x][y] == 1:
        return -1

    (M, N) = (len(mat), len(mat[0]))

    visited = [[False for _ in range(N)] for _ in range(M)]

    min_dist = find_shortest(mat, visited, i, j, dest)

    if min_dist != sys.maxsize:
        return min_dist
    else:
        return -1


if __name__ == '__main__':
    mat = [
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 0],
    ]

    source = (0, 0)
    destination = (len(mat) - 1, len(mat[0]) - 1)

    min_dist = shortest_path(mat, source, destination)

    print(min_dist)
