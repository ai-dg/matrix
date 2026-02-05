from linalg.vector import Vector
import sys
from linalg.logger import Logger
logger = Logger()


def ft_dot(u, v):
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        logger.error("dot expects two Vectors")
        sys.exit(1)

    if u.shape != v.shape:
        logger.error("Vectors must have same shape")
        sys.exit(1)

    result = 0.0
    for row_u, row_v in zip(u.data, v.data):
        for a, b in zip(row_u, row_v):
            result += a * b

    return result


def main():

    logger.info("#" * 60)
    logger.info("#                 EX03 - Dot product             #")
    logger.info("#" * 60)

    u = Vector([0., 0.])
    v = Vector([1., 1.])

    logger.info("#" * 20 + " First " + "#" * 20)

    logger.info("[u @ b]")
    logger.info(f"u @ v: \n{u @ v}")
    logger.info(f"u @ v: \n{u.__matmul__(v)}")
    logger.info(f"u @ v: \n{ft_dot(u, v)}")

    u = Vector([1., 1.])
    v = Vector([1., 1.])

    logger.info("#" * 20 + " Second " + "#" * 20)
    logger.info(f"u @ v: \n{u @ v}")
    logger.info(f"u @ v: \n{u.__matmul__(v)}")
    logger.info(f"u @ v: \n{ft_dot(u, v)}")

    logger.info("#" * 20 + " Third " + "#" * 20)
    u = Vector([-1., 6.])
    v = Vector([3., 2.])
    logger.info(f"u @ v: \n{u @ v}")
    logger.info(f"u @ v: \n{u.__matmul__(v)}")
    logger.info(f"u @ v: \n{ft_dot(u, v)}")

    logger.info("#" * 60)
    logger.info("#                   END OF EX03                        #")
    logger.info("#" * 60)


if __name__ == "__main__":
    main()
