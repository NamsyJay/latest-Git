import logging

def main() -> None:
    # Basic Logging Example 
    logging.basicConfig(
        level=logging.CRITICAL,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="accounts.log", # This ensures that the log message sare written into a file.         
    )

    logging.debug('This Message displays a Debug Message!')
    logging.info('This Message displays Information on Scalify!')
    logging.warning('This Message displays a Warning For Scalify Competitiors!')
    logging.error('This Message displays an Error For Scalify Users!')
    logging.critical('This Message displays a Critical Error For Scalify Admins!')


if __name__ == '__main__':
    main()
