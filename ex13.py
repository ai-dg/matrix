from linalg.matrix import Matrix
import sys

def main():

    print("\n" + "#" * 60)
    print("#                 EX13 - Rank              #")
    print("#" * 60)

    print("\n" + "#" * 20 + " 1 " + "#" * 20)
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]
    ])

  
    print(f"{u.ft_rank()}")

    print("\n" + "#" * 20 + " 2 " + "#" * 20)
    u = Matrix([
        [ 1., 2., 0., 0.],
        [ 2., 4., 0., 0.],
        [-1., 2., 1., 1.]
    ])

  
    print(f"{u.ft_rank()}")

    print("\n" + "#" * 20 + " 3 " + "#" * 20)
    u = Matrix([
        [ 8., 5., -2.],
        [ 4., 7., 20.],
        [ 7., 6., 1.],
        [21., 18., 7.]
    ])

  
    print(f"{u.ft_rank()}")



    print("\n" + "#" * 60)
    print("#                   END OF EX13                        #")
    print("#" * 60)




if __name__ == "__main__":
    main()