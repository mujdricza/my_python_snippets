import logging

# logging.basicConfig(level=logging.DEBUG)  # this has effect to all following logging statements
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # this has effect for the non-root logging statements of the current logger

logger.warning(f"{__name__} logger warning on root-level.")
logger.info(f"{__name__} logger info on root-level.")
logger.debug(f"{__name__} logger debug on root-level.")

def main():
    # logging.basicConfig(level=logging.DEBUG)  # this does not do anything
    # logger.setLevel(logging.DEBUG)  # this has scope for the current logger
    logger.warning(f"{__name__} logger warning in main().")
    logger.info(f"{__name__} logger info in main().")
    logger.debug(f"{__name__} logger debug in main().")