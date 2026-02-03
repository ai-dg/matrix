from linalg.vector import Vector
import sys


def ft_linear_combination(vectors: list[Vector], coefs: list[float]) -> Vector:

    if not isinstance(vectors, list):
        print("Error: vectors must be a list")
        sys.exit(1)

    if not isinstance(coefs, list):
        print("Error: coefs must be a list")
        sys.exit(1)

    if len(vectors) == 0:
        print("Error: empty vector list")
        sys.exit(1)

    if len(vectors) != len(coefs):
        print("Error: vectors and coefs must have the same length")
        sys.exit(1)

    if not isinstance(vectors[0], Vector):
        print("Error: vectors must contain Vector objects")
        sys.exit(1)

    shape = vectors[0].shape

    for v in vectors:
        if not isinstance(v, Vector):
            print("Error: vectors must contain Vector objects")
            sys.exit(1)
        if v.shape != shape:
            print(f"Error: all vectors must have the same shape, got {v.shape} and {shape}")
            sys.exit(1)

    for c in coefs:
        if not isinstance(c, (int, float)):
            print("Error: coefficients must be scalars")
            sys.exit(1)

    result = Vector((shape[0], shape[1]))

    for i in range(len(vectors)):
        result = result + (vectors[i] * coefs[i])

    return result
        

def main():
    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])

    v1 = Vector([1., 2., 3.])
    v2 = Vector([0., 10., -100.])

    print("\n" + "#" * 60)
    print("#                 EX01 - Linear combination              #")
    print("#" * 60)

    print("\n" + "#" * 20 + " [10., -2., 0,5] " + "#" * 20)
    print(ft_linear_combination([e1, e2, e3], [10., -2, 0.5]))

    print("\n" + "#" * 20 + " [10., -2] " + "#" * 20)
    print(ft_linear_combination([v1, v2], [10., -2]))

    print("\n" + "#" * 60)
    print("#                   END OF EX01                        #")
    print("#" * 60)

    

if __name__ == "__main__":
    main()