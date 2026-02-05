from linalg.vector import Vector
from linalg.logger import Logger
logger = Logger()


def main():

    logger.info("#" * 60)
    logger.info("#                 EX04 - Norm             #")
    logger.info("#" * 60)

    logger.info("#" * 20 + " Vector([0., 0., 0.]) " + "#" * 20)
    u = Vector([0., 0., 0.])
    logger.info(f"{u.ft_norm_1(), u.ft_norm(), u.ft_norm_inf()}")

    logger.info("#" * 20 + " Vector([1., 2., 3.] " + "#" * 20)
    u = Vector([1., 2., 3.])
    logger.info(f"{u.ft_norm_1(), u.ft_norm(), u.ft_norm_inf()}")

    logger.info("#" * 20 + " Vector([-1., -2.] " + "#" * 20)
    u = Vector([-1., -2.])
    logger.info(f"{u.ft_norm_1(), u.ft_norm(), u.ft_norm_inf()}")

    logger.info("#" * 60)
    logger.info("#                   END OF EX04                        #")
    logger.info("#" * 60)


if __name__ == "__main__":
    main()
