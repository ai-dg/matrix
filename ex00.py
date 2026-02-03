from linalg.matrix import Matrix
from linalg.vector import Vector

def ft_add_sub_scale():

    print("\n" + "#" * 60)
    print("#                 EX00 - ADD / SUB / SCALE              #")
    print("#" * 60)

    # ===================== VECTORS ===================== #
    print("\n" + "#" * 20 + " VECTORS " + "#" * 20)

    u = Vector([2., 3.])
    v = Vector([5., 7.])

    print("\n[Initialization]")
    print(f"u:\n{u}")
    print(f"v:\n{v}")

    print("\n[Addition]")
    print(f"u + v:\n{u + v}")
    print(f"u + v:\n{u.__add__(v)}")

    print("\n[Subtraction]")
    print(f"u - v:\n{u - v}")
    print(f"u - v:\n{u.__sub__(v)}")

    print("\n[Scaling]")
    print(f"u * 2:\n{u * 2.}")
    print(f"u * 2:\n{u.__mul__(2.)}")

    # ===================== MATRICES ===================== #
    print("\n" + "#" * 20 + " MATRICES " + "#" * 19)

    u = Matrix([
        [1., 2.],
        [3., 4.]
    ])

    v = Matrix([
        [7., 4.],
        [-2., 2.]
    ])

    print("\n[Initialization]")
    print(f"u:\n{u}")
    print(f"v:\n{v}")

    print("\n[Addition]")
    print(f"u + v:\n{u + v}")
    print(f"u + v:\n{u.__add__(v)}")

    print("\n[Subtraction]")
    print(f"u - v:\n{u - v}")
    print(f"u - v:\n{u.__sub__(v)}")

    print("\n[Scaling]")
    print(f"u * 2:\n{u * 2.}")
    print(f"u * 2:\n{u.__mul__(2.)}")

    print("\n" + "#" * 60)
    print("#                   END OF EX00                        #")
    print("#" * 60)


if __name__ == "__main__":
    ft_add_sub_scale()
