from __future__ import annotations

import sys
import copy
from typing import TYPE_CHECKING

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
            print("Error: matrix shape must be positive")
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
            print("Error: Verify your lists")
            sys.exit(1)

        if len(matrix) == 0:
            print("Error: empty matrix is not allowed")
            sys.exit(1)

        for row in matrix:
            if not isinstance(row, list):
                print("Error: Verify your lists of lists")
                sys.exit(1)
            if len(row) == 0:
                print("Error: empty row is not allowed")
                sys.exit(1)

            for value in row:
                if not isinstance(value, (int, float)):
                    print("Error: Verify numeric values in matrix")
                    sys.exit(1)

    def ft_take_a_choice(self, data):
        choice = ""

        if len(data) != 1:
            print("One argument is authorized in the Matrix class")
            sys.exit(1)

        if isinstance(data[0], tuple):
            if len(data[0]) != 2:
                print("Error: shape must be a tuple like (rows, columns)")
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
            print("Error: empty matrix")
            sys.exit(1)

        max_columns = len(self.data[0])

        for row in self.data:
            columns = 0
            for _ in row:
                columns += 1

            if columns != max_columns:
                print(f"Columns: {columns}, expected: {max_columns}")
                print("The lists don't have the same dimensions.")
                sys.exit(1)

        self.shape = (rows, max_columns)

    def ft_add_matrix(self, other):
        if not isinstance(other, Matrix):
            print("Error: addition expects a Matrix")
            sys.exit(1)

        if self.shape != other.shape:
            print(f"Error: matrices must have the same shape, got {self.shape} and {other.shape}")
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
            print("Error: substraction expects a Matrix")
            sys.exit(1)

        if self.shape != other.shape:
            print(f"Error: matrices must have the same shape, got {self.shape} and {other.shape}")
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
            print("Error: division expects a scalar")
            sys.exit(1)

        if other == 0:
            print("Error: division by zero")
            sys.exit(1)

        if order != "normal":
            print("Error: scalar / Matrix is not defined")
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
            print("Error: scaling expects a scalar")
            sys.exit(1)

        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                row.append(self.data[i][j] * other)
            result.append(row)

        return Matrix(result)

    def ft_mul_matrix(self, other, order: str = "normal"):
        if not isinstance(other, Matrix):
            print("Error: multiplication expects a Matrix")
            sys.exit(1)

        if order != "normal":
            return other.ft_mul_matrix(self, "normal")

        if self.shape[1] != other.shape[0]:
            print("Error: columns of first must match rows of second")
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
            print("Error")
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

        print("Error: invalid multiplication")
        sys.exit(1)

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.ft_scale_matrix(other)
        
        if isinstance(other, Matrix):
            return other.ft_mul_matrix(other)

        print("Error: invalid reverse multiplication")
        sys.exit(1)

    def __repr__(self):
        return f"Matrix({self.data})"

    def T(self):
        return self.ft_transpose()

    def shape(self):
        return f"{self.shape}"
    
    def ft_mul_vect(self, other):
        from linalg.vector import Vector
        if not isinstance(other, Vector):
            print("Error: multiplication expects a Vector")
            sys.exit(1)

        if self.shape[1] != other.shape[0]:
            print(
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
                


    def ft_trace(self):
        result = 0.0

        for i in range(self.shape[1]):
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
            best = pivot_row
            best_abs = abs(A[best][pivot_col])
            for r in range(pivot_row + 1, m):
                v = abs(A[r][pivot_col])
                if v > best_abs:
                    best_abs = v
                    best = r

            if best_abs < eps:
                continue

            if best != pivot_row:
                A[pivot_row], A[best] = A[best], A[pivot_row]

            pivot = A[pivot_row][pivot_col]
            inv = 1.0 / pivot
            for c in range(pivot_col, n):
                A[pivot_row][c] *= inv

            for r in range(pivot_row + 1, m):
                factor = A[r][pivot_col]
                if abs(factor) < eps:
                    A[r][pivot_col] = 0.0
                    continue
                A[r][pivot_col] = 0.0
                for c in range(pivot_col + 1, n):
                    A[r][c] -= factor * A[pivot_row][c]

            pivots.append((pivot_row, pivot_col))
            pivot_row += 1

        for pr, pc in reversed(pivots):
            for r in range(pr - 1, -1, -1):
                factor = A[r][pc]
                if abs(factor) < eps:
                    A[r][pc] = 0.0
                    continue
                A[r][pc] = 0.0
                for c in range(pc + 1, n):
                    A[r][c] -= factor * A[pr][c]

        return Matrix(A)
    

    def ft_recursive_determinant(self, matrix):
        size = len(matrix)

        if size == 1:
            return matrix[0][0]

        if size == 2:
            return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

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
            determinant += cofactor_sign * matrix[0][col] * self.ft_recursive_determinant(minor)

        return determinant


    def ft_determinant(self):
        if self.shape[0] != self.shape[1]:
            print("Error: determinant expects a square matrix")
            sys.exit(1)

        n = self.shape[0]

        if n > 4:
            print("Error: determinant only required up to 4x4")
            sys.exit(1)

        return self.ft_recursive_determinant(self.data)


    def ft_inverse(self, eps: float = 1e-12):
        if self.ft_determinant() == 0:
            print("Error: singular matrix")

        if self.shape[0] != self.shape[1]:
            print("Error: inverse expects a square matrix")
            sys.exit(1)

        n = self.shape[0]

        aug = []
        for i in range(n):
            row = self.data[i][:] 
            identity_part = [0.0] * n
            identity_part[i] = 1.0
            row.extend(identity_part)
            aug.append(row)

        for pivot_col in range(n):
        
            pivot_row = pivot_col
            best = pivot_row
            best_abs = abs(aug[best][pivot_col])
            for r in range(pivot_row + 1, n):
                v = abs(aug[r][pivot_col])
                if v > best_abs:
                    best_abs = v
                    best = r

            if best_abs < eps:
                print("Error: matrix is singular (no inverse)")
                sys.exit(1)

           
            if best != pivot_row:
                aug[pivot_row], aug[best] = aug[best], aug[pivot_row]

            pivot = aug[pivot_row][pivot_col]
            inv_pivot = 1.0 / pivot
            for c in range(2 * n):
                aug[pivot_row][c] *= inv_pivot

            for r in range(n):
                if r == pivot_row:
                    continue
                factor = aug[r][pivot_col]
                if abs(factor) < eps:
                    aug[r][pivot_col] = 0.0
                    continue

                aug[r][pivot_col] = 0.0
                for c in range(pivot_col + 1, 2 * n):
                    aug[r][c] -= factor * aug[pivot_row][c]

 
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

    print("-----------Case shape-----------")
    case1 = (5, 3)
    m1_alpha = Matrix(case1)
    m1 = np.zeros(case1)

    print(f"Custom function: \n{m1_alpha}, shape {m1_alpha.shape}")
    print(f"Original function: \n{m1}, shape {m1.shape}")

    print("-----------Case lists -----------")
    case2 = [[1, 2, 4], [4, 3, 1]]
    m2_alpha = Matrix(case2)
    m2 = np.array(case2, np.float32)

    print(f"Custom function: \n{m2_alpha}, shape {m2_alpha.shape}")
    print(f"Original function: \n{m2}, shape {m2.shape}")

    print("-----------Case 3 -----------")
    case3 = [[1, 2, 4], [4, 3, 1]]
    m3_alpha = Matrix(case3)
    m3 = np.array(case3, np.float32)

    print(f"Custom function: \n{m3_alpha}, shape {m3_alpha.shape}")
    print(f"Original function: \n{m3}, shape {m3.shape}")

    print("-----------Add-----------")
    m4 = m2 + m3
    print(f"Result sum m2 and m3 (numpy): \n{m4}")

    m4_alpha = m2_alpha + m3_alpha
    print(f"Result custom sum m2 and m3: \n{m4_alpha}")

    print("-----------Sub-----------")
    m5 = m2 - m3
    print(f"Result sub m2 and m3 (numpy): \n{m5}")

    m5_alpha = m2_alpha - m3_alpha
    print(f"Result custom sub m2 and m3: \n{m5_alpha}")

    print("-----------Div scalar-----------")
    div_scalar = 2
    m6 = m2 / div_scalar
    print(f"Result div m2 / {div_scalar} (numpy): \n{m6}")

    m6_alpha = m2_alpha / div_scalar
    print(f"Result custom div m2 / {div_scalar}: \n{m6_alpha}")

    print("-----------Transpose-----------")
    m7 = m2.T
    print(f"Transpose numpy m2:\n{m7}, shape {m7.shape}")

    m7_alpha = m2_alpha.T()
    print(f"Transpose custom m2:\n{m7_alpha}, shape {m7_alpha.shape}")

    print("-----------Mul (Matrix x Matrix)-----------")
    caseA = [[1, 2, 3], [4, 5, 6]]
    caseB = [[7, 8], [9, 10], [11, 12]]

    A_alpha = Matrix(caseA)
    B_alpha = Matrix(caseB)

    A = np.array(caseA, np.float32)
    B = np.array(caseB, np.float32)

    m8 = A @ B
    print(f"Result A @ B (numpy):\n{m8}, shape {m8.shape}")

    m8_alpha = A_alpha * B_alpha
    print(f"Result custom A * B:\n{m8_alpha}, shape {m8_alpha.shape}")

    print("-----------Error tests-----------")

    print("Case: add shape mismatch")
    try:
        bad1 = Matrix([[1, 2], [3, 4]]) + Matrix([[1, 2, 3], [4, 5, 6]])
        print(bad1)
    except SystemExit:
        print("OK: caught SystemExit (shape mismatch)")

    print("Case: mul shape mismatch")
    try:
        bad2 = Matrix([[1, 2, 3]]) * Matrix([[1, 2, 3]])
        print(bad2)
    except SystemExit:
        print("OK: caught SystemExit (mul mismatch)")

    print("Case: division by zero")
    try:
        bad3 = Matrix([[1, 2], [3, 4]]) / 0
        print(bad3)
    except SystemExit:
        print("OK: caught SystemExit (division by zero)")




if __name__ == "__main__":
    main()