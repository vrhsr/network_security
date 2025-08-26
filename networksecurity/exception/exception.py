import logging

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details=None):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_details = error_details

    def __str__(self):
        details = f" Details: {self.error_details}" if self.error_details else ""
        return f"NetworkSecurityException: {self.error_message}{details}"

if __name__ == "__main__":
    # Configure basic logging
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    logger = logging.getLogger(__name__)

    try:
        logger.info("This is a try message")
        a = 1/0
        print("this will not be printed", a)
    except Exception as e:
        logger.error("An exception occurred: %s", str(e))
        raise NetworkSecurityException("Division by zero error", str(e))