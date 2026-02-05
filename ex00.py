from linalg.matrix import Matrix
from linalg.vector import Vector
from linalg.logger import Logger
logger = Logger()


def ft_add_sub_scale():

    logger.info("#" * 60)
    logger.info("#                 EX00 - ADD / SUB / SCALE              #")
    logger.info("#" * 60)

    # ===================== VECTORS ===================== #
    logger.info("#" * 20 + " VECTORS " + "#" * 20)

    u = Vector([2., 3.])
    v = Vector([5., 7.])

    logger.info("[Initialization]")
    logger.info(f"u:\n{u}")
    logger.info(f"v:\n{v}")

    logger.info("[Addition]")
    logger.info(f"u + v:\n{u + v}")
    logger.info(f"u + v:\n{u.__add__(v)}")

    logger.info("[Subtraction]")
    logger.info(f"u - v:\n{u - v}")
    logger.info(f"u - v:\n{u.__sub__(v)}")

    logger.info("[Scaling]")
    logger.info(f"u * 2:\n{u * 2.}")
    logger.info(f"u * 2:\n{u.__mul__(2.)}")

    # ===================== MATRICES ===================== #
    logger.info("#" * 20 + " MATRICES " + "#" * 19)

    u = Matrix([
        [1., 2.],
        [3., 4.]
    ])

    v = Matrix([
        [7., 4.],
        [-2., 2.]
    ])

    logger.info("[Initialization]")
    logger.info(f"u:\n{u}")
    logger.info(f"v:\n{v}")

    logger.info("[Addition]")
    logger.info(f"u + v:\n{u + v}")
    logger.info(f"u + v:\n{u.__add__(v)}")

    logger.info("[Subtraction]")
    logger.info(f"u - v:\n{u - v}")
    logger.info(f"u - v:\n{u.__sub__(v)}")

    logger.info("[Scaling]")
    logger.info(f"u * 2:\n{u * 2.}")
    logger.info(f"u * 2:\n{u.__mul__(2.)}")

    logger.info("#" * 60)
    logger.info("#                   END OF EX00                        #")
    logger.info("#" * 60)


if __name__ == "__main__":
    ft_add_sub_scale()
