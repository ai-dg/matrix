from linalg.matrix import Matrix
from linalg.logger import Logger
logger = Logger()


def main():

    logger.info("#" * 60)
    logger.info("#                 EX13 - Rank              #")
    logger.info("#" * 60)

    logger.info("#" * 20 + " 1 " + "#" * 20)
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]
    ])

    logger.info(f"\n{u.ft_row_echelon()}")
    logger.info(f"{u.ft_rank()}")

    logger.info("#" * 20 + " 2 " + "#" * 20)
    u = Matrix([
        [1., 2., 0., 0.],
        [2., 4., 0., 0.],
        [-1., 2., 1., 1.]
    ])

    logger.info(f"\n{u.ft_row_echelon()}")
    logger.info(f"{u.ft_rank()}")

    logger.info("#" * 20 + " 3 " + "#" * 20)
    u = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
        [21., 18., 7.]
    ])

    logger.info(f"\n{u.ft_row_echelon()}")
    logger.info(f"{u.ft_rank()}")

    logger.info("#" * 60)
    logger.info("#                   END OF EX13                        #")
    logger.info("#" * 60)


if __name__ == "__main__":
    main()
