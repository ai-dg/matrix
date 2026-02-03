from linalg.matrix import Matrix
from linalg.vector import Vector
import sys

def ft_cross_product(u: Vector, v: Vector) -> Vector:
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        print("Error: cross product expects two Vectors")
        sys.exit(1)

    if u.shape != v.shape:
        print("Error: vectors must have same shape")
        sys.exit(1)

    if u.shape != (3, 1) and u.shape != (1, 3):
        print(f"Error: cross product expects 3D vectors, got {u.shape}")
        sys.exit(1)


    if u.shape == (3, 1):
        u1, u2, u3 = u.data[0][0], u.data[1][0], u.data[2][0]
        v1, v2, v3 = v.data[0][0], v.data[1][0], v.data[2][0]
        x = u2 * v3 - u3 * v2
        y = u3 * v1 - u1 * v3
        z = u1 * v2 - u2 * v1
        return Vector([[x], [y], [z]])

    u1, u2, u3 = u.data[0][0], u.data[0][1], u.data[0][2]
    v1, v2, v3 = v.data[0][0], v.data[0][1], v.data[0][2]
    x = u2 * v3 - u3 * v2
    y = u3 * v1 - u1 * v3
    z = u1 * v2 - u2 * v1
    return Vector([[x, y, z]])



def main():

    print("\n" + "#" * 60)
    print("#                 EX06 - Cross product             #")
    print("#" * 60)

    u = Vector([0., 0., 1.])
    v = Vector([1., 0., 0.])
    print(f"{ft_cross_product(u, v)}")

    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(f"{ft_cross_product(u, v)}")

    u = Vector([4., 2., -3.])
    v = Vector([-2., -5., 16.])
    print(f"{ft_cross_product(u, v)}")


    print("\n" + "#" * 60)
    print("#                   END OF EX06                        #")
    print("#" * 60)




if __name__ == "__main__":
    main()