from linalg.matrix import Matrix
from linalg.vector import Vector
import sys

def ft_dot(u, v):
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        print("Error: dot expects two Vectors")
        sys.exit(1)

    if u.shape != v.shape:
        print("Error: vectors must have same shape")
        sys.exit(1)

    result = 0.0
    for row_u, row_v in zip(u.data, v.data):
        for a, b in zip(row_u, row_v):
            result += a * b

    return result


def main():

    print("\n" + "#" * 60)
    print("#                 EX03 - Dot product             #")
    print("#" * 60)

    u = Vector([0., 0.])
    v = Vector([1., 1.])

    print("\n" + "#" * 20 + " First " + "#" * 20)

    print(f"u * v: \n{u * v}")
    print(f"u * v: \n{u.__mul__(v)}")
    print(f"u * v: \n{ft_dot(u, v)}")

    u = Vector([1., 1.])
    v = Vector([1., 1.])

    print("\n" + "#" * 20 + " Second " + "#" * 20)
    print(f"u * v: \n{u * v}")
    print(f"u * v: \n{u.__mul__(v)}")
    print(f"u * v: \n{ft_dot(u, v)}")



    print("\n" + "#" * 20 + " Third " + "#" * 20)
    u = Vector([-1., 6.])
    v = Vector([3., 2.])
    print(f"u * v: \n{u * v}")
    print(f"u * v: \n{u.__mul__(v)}")
    print(f"u * v: \n{ft_dot(u, v)}")

    print("\n" + "#" * 60)
    print("#                   END OF EX03                        #")
    print("#" * 60)




if __name__ == "__main__":
    main()