import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from ssh import SSHConnection

class MyFileHandler(RotatingFileHandler):
    """
    ...
    """
    def rotate(self, source, dest):
        # print("Rotation is triggered")
        super().rotate(source, dest)

        if self.ssh_open:
            put_result = self.ssh_connection.put(self.baseFilename,
                                                    self.destfile)
            print(self.baseFilename, self.destfile, put_result)
        else:
            raise Exception("No SSH connection!")

        if put_result:
            # remove log file
            pass

        # host = '192.168.56.101'
        # username = 'sklyuev'
        # password = '283314'
        # port = 22
        #
        # localpath = "/Users/sklyuev/Documents/github/Experiments/qwer.log.1"
        # remotepath = "/home/sklyuev/test2.txt"
        # ssh = SSHConnection(host, username, password, port)
        # print("SSH obj:", ssh)
        # print(host, username, password, port, localpath, remotepath)
        # # print(os.listdir("/home/sklyuev"))
        # put_res = ssh.put(localpath, remotepath)
        # print(put_res)

    def setup_ssh(self, host, username, password, port, destfile):
        """
        Open SSH connection
        """
        print(host, username, password, port)
        self.ssh_connection = SSHConnection(host, username, password, port)
        print("Log SSH:", self.ssh_connection)
        self.destfile = destfile
        self.ssh_open = True


def setup_log(logfile, destfile, maxBytes, backup, host, username, password, port):
    """
    Returns a custom rotating logger
    """

    print("1")
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    # add a rotating handler
    handler = MyFileHandler(logfile, maxBytes=300, backupCount=5)
    print("2")
    # setup ssh
    handler.setup_ssh(host, username, password, port, destfile)
    print("3")
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


if __name__ == "__main__":
    config = {
        'logfile': "/Users/sklyuev/Documents/github/Experiments/qwer.log",
        'destfile': "/home/sklyuev/test2.txt",
        'maxBytes': 300,
        'backup': 5,
        # SSH config
        'host': "192.168.56.101",
        'username': "sklyuev",
        'password': "283314",
        'port': 22
    }

    setup_log(**config)

    # Write messages into the log
    # for i in range(50):
    #     logger.info("Test message")
    #     time.sleep(1)
