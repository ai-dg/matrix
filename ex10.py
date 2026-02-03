from linalg.matrix import Matrix
import sys

def main():

    print("\n" + "#" * 60)
    print("#                 EX10 - Row-echelon             #")
    print("#" * 60)

    print("\n" + "#" * 20 + " 1 " + "#" * 20)
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]
    ])

  
    print(f"{u.ft_row_echelon()}")

    print("\n" + "#" * 20 + " 2 " + "#" * 20)
    u = Matrix([
        [1., 2.],
        [3., 4.],
    ])

  
    print(f"{u.ft_row_echelon()}")

    print("\n" + "#" * 20 + " 3 " + "#" * 20)
    u = Matrix([
        [1., 2.],
        [2., 4.],
    ])

  
    print(f"{u.ft_row_echelon()}")

    print("\n" + "#" * 20 + " 4 " + "#" * 20)
    u = Matrix([
        [8., 5., -2., 4., 28.],
        [4., 2.5, 20., 4., -4.],
        [8., 5., 1., 4., 17.],
    ])

  
    print(f"{u.ft_row_echelon()}")



    print("\n" + "#" * 60)
    print("#                   END OF EX10                        #")
    print("#" * 60)




if __name__ == "__main__":
    main()