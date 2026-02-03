from linalg.matrix import Matrix
from linalg.vector import Vector
import sys

def main():

    print("\n" + "#" * 60)
    print("#                 EX07 - Matrix multiplication             #")
    print("#" * 60)

    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])

    v = Vector([4., 2.])
    print(f"{u.ft_mul_vect(v)}")

    u = Matrix([
        [2., 0.],
        [0., 2.]
    ])

    v = Vector([4., 2.])
    print(f"{u.ft_mul_vect(v)}")

    u = Matrix([
        [2., -2.],
        [-2., 2.]
    ])

    v = Vector([4., 2.])
    print(f"{u.ft_mul_vect(v)}")

    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])

    v = Matrix([
        [1., 0.],
        [0., 1.]
    ])
    print(f"{u.ft_mul_matrix(v)}")

    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])

    v = Matrix([
        [2., 1.],
        [4., 2.]
    ])
    print(f"{u.ft_mul_matrix(v)}")

    u = Matrix([
        [3., -5.],
        [6., 8.]
    ])

    v = Matrix([
        [2., 1.],
        [4., 2.]
    ])
    print(f"{u.ft_mul_matrix(v)}")



    print("\n" + "#" * 60)
    print("#                   END OF EX07                        #")
    print("#" * 60)




if __name__ == "__main__":
    main()