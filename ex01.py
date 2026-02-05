from linalg.vector import Vector
import sys
from linalg.logger import Logger
logger = Logger()


def ft_linear_combination(vectors: list[Vector], coefs: list[float]) -> Vector:

    if not isinstance(vectors, list):
        logger.error("Vectors must be a list")
        sys.exit(1)

    if not isinstance(coefs, list):
        logger.error("Coefs must be a list")
        sys.exit(1)

    if len(vectors) == 0:
        logger.error("Empty vector list")
        sys.exit(1)

    if len(vectors) != len(coefs):
        logger.error("Vectors and coefs must have the same length")
        sys.exit(1)

    if not isinstance(vectors[0], Vector):
        logger.error("Vectors must contain Vector objects")
        sys.exit(1)

    shape = vectors[0].shape

    for v in vectors:
        if not isinstance(v, Vector):
            logger.error("Vectors must contain Vector objects")
            sys.exit(1)
        if v.shape != shape:
            logger.error(
                f"All vectors must have the same shape, got {
                    v.shape} and {shape}")
            sys.exit(1)

    for c in coefs:
        if not isinstance(c, (int, float)):
            logger.error("Coefficients must be scalars")
            sys.exit(1)

    result = Vector((shape[0], shape[1]))

    for i in range(len(vectors)):
        result = result + (vectors[i] * coefs[i])

    return result


def main():
    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])

    v1 = Vector([1., 2., 3.])
    v2 = Vector([0., 10., -100.])

    logger.info("#" * 60)
    logger.info("#                 EX01 - Linear combination              #")
    logger.info("#" * 60)

    logger.info("#" * 20 + " [10., -2., 0,5] " + "#" * 20)
    print(ft_linear_combination([e1, e2, e3], [10., -2, 0.5]))

    logger.info("#" * 20 + " [10., -2] " + "#" * 20)
    print(ft_linear_combination([v1, v2], [10., -2]))

    logger.info("#" * 60)
    logger.info("#                   END OF EX01                        #")
    logger.info("#" * 60)


if __name__ == "__main__":
    main()
