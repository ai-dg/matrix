from __future__ import annotations

from math import sqrt
import sys
import copy

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from linalg.matrix import Matrix

class Vector:
    data: list[list]
    shape: tuple

    def ft_create_zero_vector(self, data):
        values = data[0]
        rows = values[0]
        columns = values[1]

        if rows <= 0 or columns <= 0:
            print("Error: Vector shape must be positive")
            sys.exit(1)

        self.data = []
        for i in range(rows):
            to_add = []
            for j in range(columns):
                to_add.append(0.0)
            self.data.append(to_add)

    def ft_create_vector(self, data):
        self.data = copy.deepcopy(data[0])

    def ft_check_rows_of_data(self, vector):
        if not isinstance(vector, list):
            print("Error: Verify your lists")
            sys.exit(1)

        if len(vector) == 0:
            print("Error: empty Vector is not allowed")
            sys.exit(1)

        for row in vector:
            if not isinstance(row, list):
                print("Error: Verify your lists of lists")
                sys.exit(1)
            if len(row) == 0:
                print("Error: empty row is not allowed")
                sys.exit(1)

            for value in row:
                if not isinstance(value, (int, float)):
                    print("Error: Verify numeric values in Vector")
                    sys.exit(1)

    def ft_take_a_choice(self, data):
        choice = ""

        if len(data) != 1:
            print("One argument is authorized in the Vector class")
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
            print("Error: empty Vector")
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

        if self.shape[0] != 1 and self.shape[1] != 1:
            print(f"Error: Vector must be a row or column vector, got {self.shape}")
            sys.exit(1)

    def ft_add_vector(self, other):
        if not isinstance(other, Vector):
            print("Error: addition expects a Vector")
            sys.exit(1)

        if self.shape != other.shape:
            print(f"Error: vectors must have the same shape, got {self.shape} and {other.shape}")
            sys.exit(1)

        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return Vector(result)

    def ft_sub_vector(self, other, order: str = "normal"):
        if not isinstance(other, Vector):
            print("Error: substraction expects a Vector")
            sys.exit(1)

        if self.shape != other.shape:
            print(f"Error: vectors must have the same shape, got {self.shape} and {other.shape}")
            sys.exit(1)

        if order != "normal":
            return other.ft_sub_vector(self, "normal")

        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)

        return Vector(result)

    def ft_div_vector(self, other, order: str = "normal"):
        if not isinstance(other, (int, float)):
            print("Error: division expects a scalar")
            sys.exit(1)

        if other == 0:
            print("Error: division by zero")
            sys.exit(1)

        if order != "normal":
            print("Error: scalar / Vector is not defined")
            sys.exit(1)

        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                row.append(self.data[i][j] / other)
            result.append(row)

        return Vector(result)

    def ft_scale_vector(self, other, order: str = "normal"):
        if not isinstance(other, (int, float)):
            print("Error: scaling expects a scalar")
            sys.exit(1)

        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                row.append(self.data[i][j] * other)
            result.append(row)

        return Vector(result)

    def ft_mul_vector(self, other):
        if not isinstance(other, Vector):
            print("Error: dot expects a Vector")
            sys.exit(1)

        if self.shape != other.shape:
            print(f"Error: vectors must have the same shape, got {self.shape} and {other.shape}")
            sys.exit(1)

        mult = 0.0
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                mult += self.data[i][j] * other.data[i][j]

        return mult

    def ft_transpose(self):
        result = []
        for i in range(self.shape[1]):
            row = []
            for j in range(self.shape[0]):
                row.append(self.data[j][i])
            result.append(row)

        return Vector(result)
    
    def ft_normalize_vector_input(self, data):
        if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data):
            return [[x] for x in data]
        return data

    def __init__(self, *data):
        self.data = []
        if isinstance(data[0], list):
            data = (self.ft_normalize_vector_input(data[0]),)

        choice = self.ft_take_a_choice(data)

        if choice == "1":
            self.ft_create_zero_vector(data)
        elif choice == "2":
            self.ft_create_vector(data)
        else:
            print("Error")
            sys.exit(1)

        self.ft_define_shape_of_data()

    def __str__(self):
        return "[" + "\n ".join(str(row) for row in self.data) + "]"

    def __add__(self, other):
        return self.ft_add_vector(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.ft_sub_vector(other)

    def __rsub__(self, other):
        if not isinstance(other, Vector):
            print("Error: substraction expects a Vector")
            sys.exit(1)
        return other.ft_sub_vector(self)

    def __truediv__(self, other):
        return self.ft_div_vector(other)

    def __rtruediv__(self, other):
        return self.ft_div_vector(other, "r")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.ft_scale_vector(other)

        if isinstance(other, Vector):
            return self.ft_mul_vector(other)

        print("Error: invalid multiplication")
        sys.exit(1)

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.ft_scale_vector(other)
        
        if isinstance(other, Vector):
            return other.ft_mul_vector(other)

        print("Error: invalid reverse multiplication")
        sys.exit(1)

    def __repr__(self):
        return f"Vector({self.data})"

    def T(self):
        return self.ft_transpose()


    def shape(self):
        return f"{self.shape}"
        
    def ft_norm_1(self):
        norm = 0.0

        for row in self.data:
            for v in row:
                norm += abs(v)

        return norm


    def ft_norm(self):
        norm = 0.0

        for row in self.data:
            for v in row:
                norm += v * v

        return sqrt(norm)


    def ft_norm_inf(self):
        norm = 0.0

        for row in self.data:
            for v in row:
                if abs(v) > norm:
                    norm = abs(v)

        return norm
    
    def ft_mul_matrix(self, other):
        from linalg.matrix import Matrix
        if not isinstance(other, Matrix):
            print("Error: multiplication expects a Matrix")
            sys.exit(1)

        if self.shape[1] != other.shape[0]:
            print(
                f"Error: matrix columns ({self.shape[1]}) "
                f"must match matrix rows ({other.shape[0]})"
            )
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

def main():

    import numpy as np

    print("-----------Case shape (row vector)-----------")
    case1 = (1, 5)
    v1_alpha = Vector(case1)
    v1 = np.zeros(case1)

    print(f"Custom function: \n{v1_alpha}, shape {v1_alpha.shape}")
    print(f"Original function: \n{v1}, shape {v1.shape}")

    print("-----------Case lists (row vector)-----------")
    case2 = [[1, 2, 4]]
    v2_alpha = Vector(case2)
    v2 = np.array(case2, np.float32)

    print(f"Custom function: \n{v2_alpha}, shape {v2_alpha.shape}")
    print(f"Original function: \n{v2}, shape {v2.shape}")

    print("-----------Case 3 (row vector)-----------")
    case3 = [[4, 3, 1]]
    v3_alpha = Vector(case3)
    v3 = np.array(case3, np.float32)

    print(f"Custom function: \n{v3_alpha}, shape {v3_alpha.shape}")
    print(f"Original function: \n{v3}, shape {v3.shape}")

    print("-----------Add-----------")
    v4 = v2 + v3
    print(f"Result sum v2 and v3 (numpy): \n{v4}")

    v4_alpha = v2_alpha + v3_alpha
    print(f"Result custom sum v2 and v3: \n{v4_alpha}")

    print("-----------Sub-----------")
    v5 = v2 - v3
    print(f"Result sub v2 and v3 (numpy): \n{v5}")

    v5_alpha = v2_alpha - v3_alpha
    print(f"Result custom sub v2 and v3: \n{v5_alpha}")

    print("-----------Div scalar-----------")
    div_scalar = 2
    v6 = v2 / div_scalar
    print(f"Result div v2 / {div_scalar} (numpy): \n{v6}")

    v6_alpha = v2_alpha / div_scalar
    print(f"Result custom div v2 / {div_scalar}: \n{v6_alpha}")

    print("-----------Scalar mul-----------")
    mul_scalar = 3
    v7 = v2 * mul_scalar
    print(f"Result v2 * {mul_scalar} (numpy): \n{v7}")

    v7_alpha = v2_alpha * mul_scalar
    print(f"Result custom v2 * {mul_scalar}: \n{v7_alpha}")

    v7b = mul_scalar * v2
    print(f"Result {mul_scalar} * v2 (numpy): \n{v7b}")

    v7b_alpha = mul_scalar * v2_alpha
    print(f"Result custom {mul_scalar} * v2: \n{v7b_alpha}")

    print("-----------Transpose-----------")
    v8 = v2.T
    print(f"Transpose numpy v2:\n{v8}, shape {v8.shape}")

    v8_alpha = v2_alpha.T()
    print(f"Transpose custom v2:\n{v8_alpha}, shape {v8_alpha.shape}")

    print("-----------Dot (Vector x Vector)-----------")

    dot_np = float(np.dot(v2.reshape(-1), v3.reshape(-1)))
    print(f"Result dot(v2, v3) (numpy): {dot_np}")

    dot_alpha = v2_alpha * v3_alpha
    print(f"Result custom dot(v2, v3): {dot_alpha}")

    print("-----------Column vector tests-----------")
    col_case = [[1], [2], [4]]  # (3,1)
    vc_alpha = Vector(col_case)
    vc = np.array(col_case, np.float32)

    print(f"Custom column vector:\n{vc_alpha}, shape {vc_alpha.shape}")
    print(f"Numpy column vector:\n{vc}, shape {vc.shape}")

    print("Transpose column vector (custom):")
    print(vc_alpha.T(), vc_alpha.T().shape)

    print("-----------Error tests-----------")

    print("Case: invalid vector shape (2x3)")
    try:
        bad0 = Vector([[1, 2, 3], [4, 5, 6]])
        print(bad0)
    except SystemExit:
        print("OK: caught SystemExit (invalid vector shape)")

    print("Case: add shape mismatch")
    try:
        bad1 = Vector([[1, 2]]) + Vector([[1, 2, 3]])
        print(bad1)
    except SystemExit:
        print("OK: caught SystemExit (shape mismatch)")

    print("Case: dot shape mismatch (row vs col)")
    try:
        bad2 = Vector([[1, 2, 3]]) * Vector([[1], [2], [3]])
        print(bad2)
    except SystemExit:
        print("OK: caught SystemExit (dot mismatch)")

    print("Case: division by zero")
    try:
        bad3 = Vector([[1, 2, 3]]) / 0
        print(bad3)
    except SystemExit:
        print("OK: caught SystemExit (division by zero)")

    print("Case: scalar / Vector (not defined)")
    try:
        bad4 = 2 / Vector([[1, 2, 3]])
        print(bad4)
    except SystemExit:
        print("OK: caught SystemExit (scalar / Vector not defined)")



if __name__ == "__main__":
    main()