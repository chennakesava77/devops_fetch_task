import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("devopsfetch")
handler = RotatingFileHandler("devopsfetch.log", maxBytes=1000000, backupCount=5)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def log_info(title, data):
    logger.info(f"{title}: {data}")
