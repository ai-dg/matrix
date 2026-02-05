from linalg.matrix import Matrix
from linalg.logger import Logger
logger = Logger()


def main():

    logger.info("#" * 60)
    logger.info("#                 EX10 - Row-echelon             #")
    logger.info("#" * 60)

    logger.info("#" * 20 + " 1 " + "#" * 20)
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]
    ])

    logger.info(f"\n{u.ft_row_echelon()}")

    logger.info("#" * 20 + " 2 " + "#" * 20)
    u = Matrix([
        [1., 2.],
        [3., 4.],
    ])

    logger.info(f"\n{u.ft_row_echelon()}")

    logger.info("#" * 20 + " 3 " + "#" * 20)
    u = Matrix([
        [1., 2.],
        [2., 4.],
    ])

    logger.info(f"\n{u.ft_row_echelon()}")

    logger.info("#" * 20 + " 4 " + "#" * 20)
    u = Matrix([
        [8., 5., -2., 4., 28.],
        [4., 2.5, 20., 4., -4.],
        [8., 5., 1., 4., 17.],
    ])

    logger.info(f"\n{u.ft_row_echelon()}")

    logger.info("#" * 60)
    logger.info("#                   END OF EX10                        #")
    logger.info("#" * 60)


if __name__ == "__main__":
    main()
