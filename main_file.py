#!/usr/bin/python3
import logging
import time
import handler
logger = logging.getLogger("main_file")

logging.basicConfig(filename="logger.log",
                    filemode="w+",
                    level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')

def main():
    config = {
        'logfile': "/Users/sklyuev/Documents/github/Logger/qwer.log.1",
        'destfile': "/home/sklyuev/",
        'maxBytes': 300,
        'backup': 5,
        # SSH config
        'host': "192.168.56.101",
        'username': "sklyuev",
        'password': "283314",
        'port': 22
    }

    mylogger = handler.setup_log(**config)

    # Write messages into the log
    for i in range(10):
        mylogger.info("Test message")
        time.sleep(1)

if __name__ == "__main__":
    main()
