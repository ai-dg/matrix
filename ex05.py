from linalg.vector import Vector
import sys
from linalg.logger import Logger
logger = Logger()


def ft_angle_cos(u: Vector, v: Vector) -> float:
    """
    Formule géométrique du produit scalaire
    u * v = ‖u‖ ‖v‖ cos(θ)
    cos(θ) = (u · v) / (‖u‖ ‖v‖)
    """
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        logger.error("The function expects two Vectors")
        sys.exit(1)

    if u.shape != v.shape:
        logger.error("Vectors must have same shape")
        sys.exit(1)

    mult = u @ v
    norm_u = u.ft_norm()
    norm_v = v.ft_norm()

    if norm_u == 0 or norm_v == 0:
        logger.error("Cosine is undefined for zero norm vector")
        sys.exit(1)

    angle = mult / (norm_u * norm_v)

    return angle


def main():

    logger.info("#" * 60)
    logger.info("#                 EX05 - Angle cos             #")
    logger.info("#" * 60)

    u = Vector([1., 0.])
    v = Vector([1., 0.])
    logger.info(f"\n{ft_angle_cos(u, v)}")

    u = Vector([1., 0.])
    v = Vector([0., 1.])
    logger.info(f"\n{ft_angle_cos(u, v)}")

    u = Vector([-1., 1.])
    v = Vector([1., -1.])
    logger.info(f"\n{ft_angle_cos(u, v)}")

    u = Vector([2., 1.])
    v = Vector([4., 2.])
    logger.info(f"\n{ft_angle_cos(u, v)}")

    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    logger.info(f"\n{ft_angle_cos(u, v)}")

    logger.info("#" * 60)
    logger.info("#                   END OF EX05                        #")
    logger.info("#" * 60)


if __name__ == "__main__":
    main()
