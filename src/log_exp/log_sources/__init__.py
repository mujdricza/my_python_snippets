import logging


logger = logging.getLogger(__name__)

logger.warning(f"{__name__} logger warning on root-level.")
logger.info(f"{__name__} logger info on root-level.")
logger.debug(f"{__name__} logger debug on root-level.")

def main():
    logger.warning(f"{__name__} logger warning in main().")
    logger.info(f"{__name__} logger info in main().")
    logger.debug(f"{__name__} logger debug in main().")


