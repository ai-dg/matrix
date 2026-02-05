from linalg.matrix import Matrix
from linalg.vector import Vector
import sys
from linalg.logger import Logger
logger = Logger()


def ft_lerp(u, v, t):
    """
    Fonction affine: espace d'un espace vectoriel: .
    une fonction linéaire à laquelle on a ajouté un décalage (une translation)
    f(0) = 0
    f(x + y) = f(x) + f(y)
    f(λx) = λf(x)

    
    
    ft(t) = a * t - b ->
    ft(0) = a * t - b = u
    f(0) = b = u -> b = u
    f(1) = a * t + b = v
    f(1) = a + b = v
    f(1) = a = v - u
    f(t) = t(v - u) + u
    f(t) = u - tu + tv

    (1 - t)u + tv
    
    """
    if not isinstance(u, type(v)):
        logger.info(f"u and v are not same type: {type(u)}:{type(v)}")
        sys.exit(1)

    if not isinstance(t, (int, float)):
        logger.info("t are not an scalar")
        sys.exit(1)

    if isinstance(u, (int, float)) and isinstance(v, (int, float)):
        return (u - (t * u) + (t * v) )

    if not isinstance(u, (Vector, Matrix)):
        logger.info("u and v must be scalar, Vector or Matrix")
        sys.exit(1)

    if u.shape != v.shape:
        logger.info(f"u and v don't have the same shape: {u.shape}:{v.shape}")
        sys.exit(1)

    return (u - (t * u) + (t * v) )


def main():

    logger.info("#" * 60)
    logger.info("#                 EX02 - Linear interpolation             #")
    logger.info("#" * 60)

    logger.info("#" * 20 + " Scalars " + "#" * 20)
    logger.info(f"{ft_lerp(0., 1., 0.)}")

    logger.info(f"{ft_lerp(0., 1., 1.)}")

    logger.info(f"{ft_lerp(0., 1., 0.5)}")

    logger.info(f"{ft_lerp(21., 42., 0.3)}")

    logger.info("#" * 20 + " Vectors " + "#" * 20)
    logger.info(f"\n{ft_lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3)}")

    logger.info("#" * 20 + " Matrices " + "#" * 20)
    print(
        ft_lerp(
            Matrix([
                [2., 1.],
                [3., 4.]
            ]),
            Matrix([
                [20., 10.],
                [30., 40.]
            ]),
            0.5
        )
    )

    logger.info("#" * 60)
    logger.info("#                   END OF EX02                        #")
    logger.info("#" * 60)


if __name__ == "__main__":
    main()
