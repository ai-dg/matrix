from linalg.matrix import Matrix
import sys

def main():

    print("\n" + "#" * 60)
    print("#                 EX09 - Transpose             #")
    print("#" * 60)

    print("\n" + "#" * 20 + " 1 " + "#" * 20)
    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])

  
    print(f"{u.ft_transpose()}")

    u = Matrix([
        [1., 2.],
        [3., 1.]
    ])

    print("\n" + "#" * 20 + " 2 " + "#" * 20)

    print(f"{u.ft_transpose()}")

    u = Matrix([
        [2., -5., 0.],
        [4., 3., 7.],
        [-2., 3., 4.]
    ])

    print("\n" + "#" * 20 + " 3 " + "#" * 20)


    print(f"{u.ft_transpose()}")

    u = Matrix([
        [2., -8., 4.],
        [1., -23., 4.],
        [0., 6., 4.]
    ])

    print("\n" + "#" * 20 + " 4 " + "#" * 20)

    print(f"{u.ft_transpose()}")



    print("\n" + "#" * 60)
    print("#                   END OF EX09                        #")
    print("#" * 60)




if __name__ == "__main__":
    main()