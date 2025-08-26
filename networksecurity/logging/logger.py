import logging
import os
from datetime import datetime

class NetworkSecurityException(Exception):
    pass

# Define log directory
log_dir = os.path.join("logs", "exception")
os.makedirs(log_dir, exist_ok=True)
log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_file_path = os.path.join(log_dir, log_file)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Remove all handlers associated with the logger object (prevents duplicate logs)
logger.handlers.clear()

# Create file handler and set formatter
file_handler = logging.FileHandler(log_file_path)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info("Logger initialized and log file created.")

if __name__ == "__main__":
    try:
        logger.info("Enter try block")
        print("Enter try block")
        x = 1 / 0
        print("This is not printed")
    except Exception as e:
        logger.error("Exception occurred in try block", exc_info=True)
        raise NetworkSecurityException("Network security exception occurred") from e