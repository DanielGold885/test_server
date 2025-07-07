import logging

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

# File handler
file_handler = logging.FileHandler("server.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

# Attach handlers (but prevent duplicates on reload)
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
