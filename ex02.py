from linalg.matrix import Matrix
from linalg.vector import Vector
import sys


def ft_lerp(u, v, t):
    if type(u) != type(v):
        print(f"u and v are not same type: {type(u)}:{type(v)}")
        sys.exit(1)

    if not isinstance(t, (int, float)):
        print("t are not an scalar")
        sys.exit(1)

    if isinstance(u, (int, float)) and isinstance(v, (int, float)):
        return (u * (1 - t)) + (v * t)

    if not isinstance(u, (Vector, Matrix)):
        print("u and v must be scalar, Vector or Matrix")
        sys.exit(1)

    if u.shape != v.shape:
        print(f"u and v don't have the same shape: {u.shape}:{v.shape}")
        sys.exit(1)

    return (u * (1 - t)) + (v * t)

def main():

    print("\n" + "#" * 60)
    print("#                 EX02 - Linear interpolation             #")
    print("#" * 60)

    print("\n" + "#" * 20 + " Scalars " + "#" * 20)
    print(f"{ft_lerp(0., 1., 0.)}")

    print(f"{ft_lerp(0., 1., 1.)}")
    
    print(f"{ft_lerp(0., 1., 0.5)}")

    print(f"{ft_lerp(21., 42., 0.3)}")

    print("\n" + "#" * 20 + " Vectors " + "#" * 20)
    print(f"{ft_lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3)}")

    print("\n" + "#" * 20 + " Matrices " + "#" * 20)
    print(
        ft_lerp(
            Matrix([
                [2., 1.],
                [3., 4.]
            ]),
            Matrix([
                [20., 10.],
                [30., 40.]
            ]),
            0.5
        )
    )

    print("\n" + "#" * 60)
    print("#                   END OF EX02                        #")
    print("#" * 60)

    

if __name__ == "__main__":
    main()