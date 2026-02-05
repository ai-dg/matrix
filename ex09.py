from linalg.matrix import Matrix
from linalg.logger import Logger
logger = Logger()


def main():

    logger.info("#" * 60)
    logger.info("#                 EX09 - Transpose             #")
    logger.info("#" * 60)

    logger.info("#" * 20 + " 1 " + "#" * 20)
    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])

    logger.info(f"\n{u.ft_transpose()}")

    u = Matrix([
        [1., 2.],
        [3., 1.]
    ])

    logger.info("#" * 20 + " 2 " + "#" * 20)

    logger.info(f"\n{u.ft_transpose()}")

    u = Matrix([
        [2., -5., 0.],
        [4., 3., 7.],
        [-2., 3., 4.]
    ])

    logger.info("#" * 20 + " 3 " + "#" * 20)

    logger.info(f"\n{u.ft_transpose()}")

    u = Matrix([
        [2., -8., 4.],
        [1., -23., 4.],
        [0., 6., 4.]
    ])

    logger.info("#" * 20 + " 4 " + "#" * 20)

    logger.info(f"\n{u.ft_transpose()}")

    logger.info("#" * 60)
    logger.info("#                   END OF EX09                        #")
    logger.info("#" * 60)


if __name__ == "__main__":
    main()
