from linalg.matrix import Matrix
from linalg.vector import Vector
import sys

def ft_angle_cos(u : Vector, v: Vector) -> float:
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        print("Error: cosine similarity expects two Vectors")
        sys.exit(1)

    if u.shape != v.shape:
        print("Error: vectors must have same shape")
        sys.exit(1)


    mult = u * v
    norm_u = u.ft_norm()
    norm_v = v.ft_norm()

    if norm_u == 0 or norm_v == 0:
        print("Error: cosine similarity is undefined for zero vector")
        sys.exit(1)

    angle = mult / (norm_u * norm_v)



    return angle


def main():

    print("\n" + "#" * 60)
    print("#                 EX05 - Angle cos             #")
    print("#" * 60)

    u = Vector([1., 0.])
    v = Vector([1., 0.])
    print(f"{ft_angle_cos(u, v)}")

    u = Vector([1., 0.])
    v = Vector([0., 1.])
    print(f"{ft_angle_cos(u, v)}")

    u = Vector([-1., 1.])
    v = Vector([1., -1.])
    print(f"{ft_angle_cos(u, v)}")

    u = Vector([2., 1.])
    v = Vector([4., 2.])
    print(f"{ft_angle_cos(u, v)}")


    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(f"{ft_angle_cos(u, v)}")

    print("\n" + "#" * 60)
    print("#                   END OF EX05                        #")
    print("#" * 60)




if __name__ == "__main__":
    main()