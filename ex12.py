from linalg.matrix import Matrix
from linalg.logger import Logger
logger = Logger()


def main():

    logger.info("#" * 60)
    logger.info("#                 EX12 - Inverse              #")
    logger.info("#" * 60)

    logger.info("#" * 20 + " 1 " + "#" * 20)
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]
    ])

    logger.info(f"\n{u.ft_inverse()}")

    logger.info("#" * 20 + " 2 " + "#" * 20)
    u = Matrix([
        [2., 0., 0.],
        [0., 2., 0.],
        [0., 0., 2.]
    ])

    logger.info(f"\n{u.ft_inverse()}")

    logger.info("#" * 20 + " 3 " + "#" * 20)
    u = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.]
    ])

    logger.info(f"\n{u.ft_inverse()}")

    logger.info("#" * 60)
    logger.info("#                   END OF EX12                        #")
    logger.info("#" * 60)


if __name__ == "__main__":
    main()
