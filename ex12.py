from linalg.matrix import Matrix
import sys

def main():

    print("\n" + "#" * 60)
    print("#                 EX12 - Inverse              #")
    print("#" * 60)

    print("\n" + "#" * 20 + " 1 " + "#" * 20)
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]
    ])

  
    print(f"{u.ft_inverse()}")

    print("\n" + "#" * 20 + " 2 " + "#" * 20)
    u = Matrix([
        [2., 0., 0.],
        [0., 2., 0.],
        [0., 0., 2.]
    ])

  
    print(f"{u.ft_inverse()}")

    print("\n" + "#" * 20 + " 3 " + "#" * 20)
    u = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.]
    ])

  
    print(f"{u.ft_inverse()}")



    print("\n" + "#" * 60)
    print("#                   END OF EX12                        #")
    print("#" * 60)




if __name__ == "__main__":
    main()