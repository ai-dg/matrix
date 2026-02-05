from linalg.matrix import Matrix
from linalg.vector import Vector
from linalg.logger import Logger
logger = Logger()


def main():

    logger.info("#" * 60)
    logger.info("#                 EX07 - Matrix multiplication             #")
    logger.info("#" * 60)

    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])

    v = Vector([4., 2.])
    logger.info(f"{u.ft_matmul_vect(v)}")

    u = Matrix([
        [2., 0.],
        [0., 2.]
    ])

    v = Vector([4., 2.])
    logger.info(f"{u.ft_matmul_vect(v)}")

    u = Matrix([
        [2., -2.],
        [-2., 2.]
    ])

    v = Vector([4., 2.])
    logger.info(f"{u.ft_matmul_vect(v)}")

    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])

    v = Matrix([
        [1., 0.],
        [0., 1.]
    ])
    logger.info(f"{u.ft_matmul_matrix(v)}")

    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])

    v = Matrix([
        [2., 1.],
        [4., 2.]
    ])
    logger.info(f"{u.ft_matmul_matrix(v)}")

    u = Matrix([
        [3., -5.],
        [6., 8.]
    ])

    v = Matrix([
        [2., 1.],
        [4., 2.]
    ])
    logger.info(f"{u.ft_matmul_matrix(v)}")

    logger.info("#" * 60)
    logger.info("#                   END OF EX07                        #")
    logger.info("#" * 60)


if __name__ == "__main__":
    main()
