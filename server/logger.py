import logging

def setup_logger(name = "MY_TUTOR"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] --- [%(message)s]")
    ch.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler

    return logger
logger = setup_logger()

logger.info("RAG process started")
logger.debug("Debugging ")
logger.error("failed to load")
logger.critical("Critical message")



