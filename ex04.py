from linalg.matrix import Matrix
from linalg.vector import Vector
import sys

def main():

    print("\n" + "#" * 60)
    print("#                 EX04 - Norm             #")
    print("#" * 60)

    u = Vector([0., 0., 0.])
    print(f"{u.ft_norm_1(), u.ft_norm(), u.ft_norm_inf()}")

    u = Vector([1., 2., 3.])
    print(f"{u.ft_norm_1(), u.ft_norm(), u.ft_norm_inf()}")

    u = Vector([-1., -2.])
    print(f"{u.ft_norm_1(), u.ft_norm(), u.ft_norm_inf()}")


    print("\n" + "#" * 60)
    print("#                   END OF EX04                        #")
    print("#" * 60)




if __name__ == "__main__":
    main()