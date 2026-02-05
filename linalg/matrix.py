from __future__ import annotations

import sys
import copy
from typing import TYPE_CHECKING
from linalg.logger import Logger
logger = Logger()

if TYPE_CHECKING:
    from linalg.vector import Vector


class Matrix:
    data: list[list]
    shape: tuple

    def ft_create_zero_matrix(self, data):
        values = data[0]
        rows = values[0]
        columns = values[1]

        if rows <= 0 or columns <= 0:
            logger.error("Matrix shape must be positive")
            sys.exit(1)

        self.data = []
        for i in range(rows):
            to_add = []
            for j in range(columns):
                to_add.append(0.0)
            self.data.append(to_add)

    def ft_create_matrix(self, data):
        self.data = copy.deepcopy(data[0])

    def ft_check_rows_of_data(self, matrix):
        if not isinstance(matrix, list):
            logger.error("Verify your lists")
            sys.exit(1)

        if len(matrix) == 0:
            logger.error("Empty matrix is not allowed")
            sys.exit(1)

        for row in matrix:
            if not isinstance(row, list):
                logger.error("Verify your lists of lists")
                sys.exit(1)
            if len(row) == 0:
                logger.error("Empty row is not allowed")
                sys.exit(1)

            for value in row:
                if not isinstance(value, (int, float)):
                    logger.error("Verify numeric values in matrix")
                    sys.exit(1)

    def ft_take_a_choice(self, data):
        choice = ""

        if len(data) != 1:
            logger.info("One argument is authorized in the Matrix class")
            sys.exit(1)

        if isinstance(data[0], tuple):
            if len(data[0]) != 2:
                logger.error("Shape must be a tuple like (rows, columns)")
                sys.exit(1)
            for value in data[0]:
                if not isinstance(value, int):
                    return choice
            choice = "1"
            return choice

        if isinstance(data[0], list):
            self.ft_check_rows_of_data(data[0])
            choice = "2"
            return choice

        return choice

    def ft_define_shape_of_data(self):
        rows = len(self.data)
        if rows == 0:
            logger.error("Empty matrix")
            sys.exit(1)

        max_columns = len(self.data[0])

        for row in self.data:
            columns = 0
            for _ in row:
                columns += 1

            if columns != max_columns:
                logger.info(f"Columns: {columns}, expected: {max_columns}")
                logger.info("The lists don't have the same dimensions.")
                sys.exit(1)

        self.shape = (rows, max_columns)

    def ft_add_matrix(self, other):
        if not isinstance(other, Matrix):
            logger.error("Addition expects a Matrix")
            sys.exit(1)

        if self.shape != other.shape:
            logger.error(
                f"Matrices must have the same shape, got {
                    self.shape} and {
                    other.shape}")
            sys.exit(1)

        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return Matrix(result)

    def ft_sub_matrix(self, other, order: str = "normal"):
        if not isinstance(other, Matrix):
            logger.error("Substraction expects a Matrix")
            sys.exit(1)

        if self.shape != other.shape:
            logger.error(
                f"Matrices must have the same shape, got {
                    self.shape} and {
                    other.shape}")
            sys.exit(1)

        if order != "normal":
            return other.ft_sub_matrix(self, "normal")

        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)

        return Matrix(result)

    def ft_div_matrix(self, other, order: str = "normal"):
        if not isinstance(other, (int, float)):
            logger.error("Division expects a scalar")
            sys.exit(1)

        if other == 0:
            logger.error("Division by zero")
            sys.exit(1)

        if order != "normal":
            logger.error("Scalar / Matrix is not defined")
            sys.exit(1)

        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                row.append(self.data[i][j] / other)
            result.append(row)

        return Matrix(result)

    def ft_scale_matrix(self, other, order: str = "normal"):
        if not isinstance(other, (int, float)):
            logger.error("Scaling expects a scalar")
            sys.exit(1)

        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                row.append(self.data[i][j] * other)
            result.append(row)

        return Matrix(result)

    def ft_matmul_matrix(self, other, order: str = "normal"):
        if not isinstance(other, Matrix):
            logger.error("Multiplication expects a Matrix")
            sys.exit(1)

        if order != "normal":
            return other.ft_matmul_matrix(self, "normal")

        if self.shape[1] != other.shape[0]:
            logger.error("columns of first must match rows of second")
            sys.exit(1)

        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(other.shape[1]):
                mult = 0.0
                for k in range(self.shape[1]):
                    mult += self.data[i][k] * other.data[k][j]
                row.append(mult)
            result.append(row)

        return Matrix(result)

    def ft_mul_matrix(self, other: "Matrix"):
        if not isinstance(other, Matrix):
            logger.error("Multiplication expects a Matrix")
            sys.exit(1)

        if self.shape != other.shape:
            logger.error(
                f"Hadamard multiplication requires same shape "
                f"(got {self.shape} and {other.shape})"
            )
            sys.exit(1)

        result = []
        for row_data, row_other in zip(self.data, other.data):
            row = []
            for value_data, value_other in zip(row_data, row_other):
                row.append(value_data * value_other)
            result.append(row)

        return Matrix(result)
    
    def ft_matmul_vect(self, other):
        from linalg.vector import Vector
        if not isinstance(other, Vector):
            logger.error("Multiplication expects a Vector")
            sys.exit(1)

        if self.shape[1] != other.shape[0]:
            logger.error(
                f"Error: matrix columns ({self.shape[1]}) "
                f"must match vector rows ({other.shape[0]})"
            )
            sys.exit(1)

        result = []

        for i in range(self.shape[0]):
            mult = 0.0
            for j in range(self.shape[1]):
                mult += self.data[i][j] * other.data[j][0]
            result.append([mult])

        return Vector(result)

    def ft_transpose(self):
        result = []
        for i in range(self.shape[1]):
            row = []
            for j in range(self.shape[0]):
                row.append(self.data[j][i])
            result.append(row)

        return Matrix(result)

    def __init__(self, *data):
        self.data = []
        choice = self.ft_take_a_choice(data)

        if choice == "1":
            self.ft_create_zero_matrix(data)
        elif choice == "2":
            self.ft_create_matrix(data)
        else:
            logger.info("Error")
            sys.exit(1)

        self.ft_define_shape_of_data()

    def __str__(self):
        return "[" + "\n ".join(str(row) for row in self.data) + "]"

    def __add__(self, other):
        return self.ft_add_matrix(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.ft_sub_matrix(other)

    def __rsub__(self, other):
        return other.ft_sub_matrix(self)

    def __truediv__(self, other):
        return self.ft_div_matrix(other)

    def __rtruediv__(self, other):
        return self.ft_div_matrix(other, "r")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.ft_scale_matrix(other)

        if isinstance(other, Matrix):
            return self.ft_mul_matrix(other)

        logger.error("Invalid * operation")
        sys.exit(1)


    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.ft_scale_matrix(other)

        logger.error("Invalid reverse * operation")
        sys.exit(1)


    def __matmul__(self, other):
        from linalg.vector import Vector
        if isinstance(other, Vector):
            return self.ft_matmul_vect(other)

        if isinstance(other, Matrix):
            return self.ft_matmul_matrix(other)

        logger.error("Invalid @ operation")
        sys.exit(1)


    def __rmatmul__(self, other):
        logger.error("Invalid @ operation: Matrix must be on the left")
        sys.exit(1)

    def __repr__(self):
        return f"Matrix({self.data})"

    def T(self):
        return self.ft_transpose()

    def ft_get_shape(self):
        return f"{self.shape}"

    

    def ft_trace(self):
        if self.shape[0] != self.shape[1]:
            logger.error("Trace expects a square matrix")
            sys.exit(1)

        result = 0.0
        for i in range(self.shape[0]):
            result += self.data[i][i]
        return result

    def ft_row_echelon(self, eps: float = 1e-12):
        m, n = self.shape
        A = [row[:] for row in self.data]

        pivot_row = 0
        pivots = []

        for pivot_col in range(n):
            if pivot_row >= m:
                break
            best_row = pivot_row
            best_abs = abs(A[best_row][pivot_col])
            for row in range(pivot_row + 1, m):
                value = abs(A[row][pivot_col])
                if value > best_abs:
                    best_abs = value
                    best_row = row

            if best_abs < eps:
                continue

            if best_row != pivot_row:
                A[pivot_row], A[best_row] = A[best_row], A[pivot_row]

            pivot = A[pivot_row][pivot_col]
            inv = 1.0 / pivot
            for col in range(pivot_col, n):
                A[pivot_row][col] *= inv

            for row in range(pivot_row + 1, m):
                factor = A[row][pivot_col]
                if abs(factor) < eps:
                    A[row][pivot_col] = 0.0
                    continue
                A[row][pivot_col] = 0.0
                for col in range(pivot_col + 1, n):
                    A[row][col] -= factor * A[pivot_row][col]

            pivots.append((pivot_row, pivot_col))
            pivot_row += 1

        for pivot_row, pivot_col in reversed(pivots):
            for row in range(pivot_row - 1, -1, -1):
                factor = A[row][pivot_col]
                if abs(factor) < eps:
                    A[row][pivot_col] = 0.0
                    continue
                A[row][pivot_col] = 0.0
                for col in range(pivot_col + 1, n):
                    A[row][col] -= factor * A[pivot_row][col]

        return Matrix(A)

    def ft_recursive_determinant(self, matrix):
        size = len(matrix)

        if size == 1:
            return matrix[0][0]

        if size == 2:
            return (matrix[0][0] * matrix[1][1]) - \
                (matrix[0][1] * matrix[1][0])

        determinant = 0.0

        for col in range(size):
            minor = []
            for row in range(1, size):
                line = []
                for j in range(size):
                    if j != col:
                        line.append(matrix[row][j])
                minor.append(line)

            cofactor_sign = -1.0 if (col % 2 == 1) else 1.0
            determinant += cofactor_sign * \
                matrix[0][col] * self.ft_recursive_determinant(minor)

        return determinant

    def ft_determinant(self):
        if self.shape[0] != self.shape[1]:
            logger.error("Determinant expects a square matrix")
            sys.exit(1)

        n = self.shape[0]

        if n > 4:
            logger.error("Determinant only required up to 4x4")
            sys.exit(1)

        return self.ft_recursive_determinant(self.data)

    def ft_inverse(self, eps: float = 1e-12): 
        if self.shape[0] != self.shape[1]:
            logger.error("Inverse expects a square matrix")
            sys.exit(1)

        if self.ft_determinant() == 0:
            logger.error("Singular matrix")
            sys.exit(1)


        m, n = self.shape
        aug = []
        
        for i in range(n):
            row = self.data[i][:]
            identity_part = [0.0] * n
            identity_part[i] = 1.0
            row.extend(identity_part)
            aug.append(row)

        for pivot_col in range(n):

            pivot_row = pivot_col
            best_row = pivot_row
            best_abs = abs(aug[best_row][pivot_col])
            for row in range(pivot_row + 1, n):
                value = abs(aug[row][pivot_col])
                if value > best_abs:
                    best_abs = value
                    best_row = row

            if best_abs < eps:
                logger.error("Matrix is singular (no inverse)")
                sys.exit(1)

            if best_row != pivot_row:
                aug[pivot_row], aug[best_row] = aug[best_row], aug[pivot_row]

            pivot = aug[pivot_row][pivot_col]
            inv_pivot = 1.0 / pivot
            for col in range(2 * n):
                aug[pivot_row][col] *= inv_pivot

            for row in range(n):
                if row == pivot_row:
                    continue
                factor = aug[row][pivot_col]
                if abs(factor) < eps:
                    aug[row][pivot_col] = 0.0
                    continue

                aug[row][pivot_col] = 0.0
                for col in range(pivot_col + 1, 2 * n):
                    aug[row][col] -= factor * aug[pivot_row][col]

        inv = []
        for i in range(n):
            inv.append(aug[i][n:])

        return Matrix(inv)

    def ft_rank(self, eps: float = 1e-12):
        echelon = self.ft_row_echelon()
        rank = 0

        for row in echelon.data:
            for x in row:
                if abs(x) > eps:
                    rank += 1
                    break

        return rank


def main():

    import numpy as np

    logger.info("-----------Case shape-----------")
    case1 = (5, 3)
    m1_alpha = Matrix(case1)
    m1 = np.zeros(case1)

    logger.info(f"Custom function: \n{m1_alpha}, shape {m1_alpha.shape}")
    logger.info(f"Original function: \n{m1}, shape {m1.shape}")

    logger.info("-----------Case lists -----------")
    case2 = [[1, 2, 4], [4, 3, 1]]
    m2_alpha = Matrix(case2)
    m2 = np.array(case2, np.float32)

    logger.info(f"Custom function: \n{m2_alpha}, shape {m2_alpha.shape}")
    logger.info(f"Original function: \n{m2}, shape {m2.shape}")

    logger.info("-----------Case 3 -----------")
    case3 = [[1, 2, 4], [4, 3, 1]]
    m3_alpha = Matrix(case3)
    m3 = np.array(case3, np.float32)

    logger.info(f"Custom function: \n{m3_alpha}, shape {m3_alpha.shape}")
    logger.info(f"Original function: \n{m3}, shape {m3.shape}")

    logger.info("-----------Add-----------")
    m4 = m2 + m3
    logger.info(f"Result sum m2 and m3 (numpy): \n{m4}")

    m4_alpha = m2_alpha + m3_alpha
    logger.info(f"Result custom sum m2 and m3: \n{m4_alpha}")

    logger.info("-----------Sub-----------")
    m5 = m2 - m3
    logger.info(f"Result sub m2 and m3 (numpy): \n{m5}")

    m5_alpha = m2_alpha - m3_alpha
    logger.info(f"Result custom sub m2 and m3: \n{m5_alpha}")

    logger.info("-----------Div scalar-----------")
    div_scalar = 2
    m6 = m2 / div_scalar
    logger.info(f"Result div m2 / {div_scalar} (numpy): \n{m6}")

    m6_alpha = m2_alpha / div_scalar
    logger.info(f"Result custom div m2 / {div_scalar}: \n{m6_alpha}")

    logger.info("-----------Transpose-----------")
    m7 = m2.T
    logger.info(f"Transpose numpy m2:\n{m7}, shape {m7.shape}")

    m7_alpha = m2_alpha.T()
    logger.info(f"Transpose custom m2:\n{m7_alpha}, shape {m7_alpha.shape}")

    logger.info("-----------Mul (Matrix x Matrix)-----------")
    caseA = [[1, 2, 3], [4, 5, 6]]
    caseB = [[7, 8], [9, 10], [11, 12]]

    A_alpha = Matrix(caseA)
    B_alpha = Matrix(caseB)

    A = np.array(caseA, np.float32)
    B = np.array(caseB, np.float32)

    m8 = A @ B
    logger.info(f"Result A @ B (numpy):\n{m8}, shape {m8.shape}")

    m8_alpha = A_alpha * B_alpha
    logger.info(f"Result custom A * B:\n{m8_alpha}, shape {m8_alpha.shape}")

    logger.info("-----------Error tests-----------")

    logger.info("Case: add shape mismatch")
    try:
        bad1 = Matrix([[1, 2], [3, 4]]) + Matrix([[1, 2, 3], [4, 5, 6]])
        print(bad1)
    except SystemExit:
        logger.info("OK: caught SystemExit (shape mismatch)")

    logger.info("Case: mul shape mismatch")
    try:
        bad2 = Matrix([[1, 2, 3]]) * Matrix([[1, 2, 3]])
        print(bad2)
    except SystemExit:
        logger.info("OK: caught SystemExit (mul mismatch)")

    logger.info("Case: division by zero")
    try:
        bad3 = Matrix([[1, 2], [3, 4]]) / 0
        print(bad3)
    except SystemExit:
        logger.info("OK: caught SystemExit (division by zero)")


if __name__ == "__main__":
    main()
