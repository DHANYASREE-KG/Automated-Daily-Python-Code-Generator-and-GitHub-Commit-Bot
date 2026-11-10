"""
Matrix Transposition and Rotation.

Provides matrix operations on 2D lists without external libraries.
"""


def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Transpose a 2D matrix (swap rows and columns)."""
    if not matrix or not matrix[0]:
        return []
    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]


def rotate_matrix_90_clockwise(matrix: list[list[int]]) -> list[list[int]]:
    """Rotate an N x N matrix 90 degrees clockwise."""
    transposed = transpose_matrix(matrix)
    return [row[::-1] for row in transposed]


if __name__ == "__main__":
    print("=== Matrix Operations ===")
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original:")
    for r in grid:
        print(r)

    print("\n90° Clockwise Rotated:")
    for r in rotate_matrix_90_clockwise(grid):
        print(r)
