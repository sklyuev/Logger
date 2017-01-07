#!/usr/bin/python3
import logging
import test
# import logging.config
# logging.config.fileConfig("./logging.conf")

logging.basicConfig(filename="example.log",
                    filemode="w",
                    level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')
# create logger
logger = logging.getLogger("main.py")


def main():
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    test.do_something()
    logging.warning("This is a warning")
    logging.error("This is an error message")
    logging.critical("FATAL!!!")

if __name__ == "__main__":
    main()
