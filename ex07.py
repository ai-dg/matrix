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
    logger.info("#" * 20 + " 1 " + "#" * 20)
    logger.info(f"\n{u.ft_matmul_vect(v)}")
    logger.info(f"\n{u @ v}")

    u = Matrix([
        [2., 0.],
        [0., 2.]
    ])

    v = Vector([4., 2.])
    logger.info("#" * 20 + " 2 " + "#" * 20)
    logger.info(f"\n{u.ft_matmul_vect(v)}")
    logger.info(f"\n{u @ v}")

    u = Matrix([
        [2., -2.],
        [-2., 2.]
    ])

    v = Vector([4., 2.])
    logger.info("#" * 20 + " 3 " + "#" * 20)
    logger.info(f"\n{u.ft_matmul_vect(v)}")
    logger.info(f"\n{u @ v}")

    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])

    v = Matrix([
        [1., 0.],
        [0., 1.]
    ])
    logger.info("#" * 20 + " 4 " + "#" * 20)
    logger.info(f"\n{u.ft_matmul_matrix(v)}")
    logger.info(f"\n{u @ v}")

    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])

    v = Matrix([
        [2., 1.],
        [4., 2.]
    ])
    logger.info("#" * 20 + " 5 " + "#" * 20)
    logger.info(f"\n{u.ft_matmul_matrix(v)}")
    logger.info(f"\n{u @ v}")

    u = Matrix([
        [3., -5.],
        [6., 8.]
    ])

    v = Matrix([
        [2., 1.],
        [4., 2.]
    ])
    logger.info("#" * 20 + " 6 " + "#" * 20)
    logger.info(f"\n{u.ft_matmul_matrix(v)}")
    logger.info(f"\n{u @ v}")

    logger.info("#" * 60)
    logger.info("#                   END OF EX07                        #")
    logger.info("#" * 60)


if __name__ == "__main__":
    main()
