import logging

# NOTE that for root-level logs, the import order is relevant
import module1
import module2
import package.module3 as module3

logging.basicConfig(level=logging.INFO)  # has effect to all further root/non-root level logs in this module, and to non-root level logs in other modules
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # has effect to the current logger on root/non-root level logs

logger.warning(f"{__name__} logger warning on root-level.")
logger.info(f"{__name__} logger info on root-level.")
logger.debug(f"{__name__} logger debug on root-level.")

def main():
    logger.warning(f"{__name__} logger warning in main().")
    logger.info(f"{__name__} logger info in main().")
    logger.debug(f"{__name__} logger debug in main().")


def fct():
    logger_fct = logging.getLogger("".join([__name__, "fct"]))
    logger_fct.warning(f"{__name__} logger warning in fct().")
    logger_fct.info(f"{__name__} logger info in fct().")
    logger_fct.debug(f"{__name__} logger debug in fct().")


if __name__ == "__main__":
    pass

    # logger.setLevel(logging.INFO)
    # logger.warning(f"{__name__} logger warning in main section.")
    # logger.info(f"{__name__} logger info in main section.")
    # main()
    # module1.main()
    # module2.main()
    # module3.main()
    # module1.main()
    # fct()
