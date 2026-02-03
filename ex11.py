from linalg.matrix import Matrix
import sys

def main():

    print("\n" + "#" * 60)
    print("#                 EX11 - Determinant              #")
    print("#" * 60)

    print("\n" + "#" * 20 + " 1 " + "#" * 20)
    u = Matrix([
        [ 1., -1.],
        [-1., 1.]
    ])

  
    print(f"{u.ft_determinant()}")

    print("\n" + "#" * 20 + " 2 " + "#" * 20)
    u = Matrix([
        [2., 0., 0.],
        [0., 2., 0.],
        [0., 0., 2.]
    ])

  
    print(f"{u.ft_determinant()}")

    print("\n" + "#" * 20 + " 3 " + "#" * 20)
    u = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.]
    ])

  
    print(f"{u.ft_determinant()}")

    print("\n" + "#" * 20 + " 4 " + "#" * 20)
    u = Matrix([
        [ 8., 5., -2., 4.],
        [ 4., 2.5, 20., 4.],
        [ 8., 5., 1., 4.],
        [28., -4., 17., 1.]
    ])

  
    print(f"{u.ft_determinant()}")



    print("\n" + "#" * 60)
    print("#                   END OF EX11                        #")
    print("#" * 60)




if __name__ == "__main__":
    main()