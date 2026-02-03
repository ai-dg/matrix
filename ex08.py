from linalg.matrix import Matrix
from linalg.vector import Vector
import sys

def main():

    print("\n" + "#" * 60)
    print("#                 EX08 - Trace             #")
    print("#" * 60)


    print("\n" + "#" * 20 + " 1 " + "#" * 20)
    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])

  
    print(f"{u.ft_trace()}")

    print("\n" + "#" * 20 + " 2 " + "#" * 20)

    u = Matrix([
        [2., -5., 0.],
        [4., 3., 7.],
        [-2., 3., 4.]
    ])


    print(f"{u.ft_trace()}")

    print("\n" + "#" * 20 + " 3 " + "#" * 20)

    u = Matrix([
        [2., -8., 4.],
        [1., -23., 4.],
        [0., 6., 4.]
    ])

    print(f"{u.ft_trace()}")



    print("\n" + "#" * 60)
    print("#                   END OF EX08                        #")
    print("#" * 60)




if __name__ == "__main__":
    main()