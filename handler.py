import logging

from logging.handlers import RotatingFileHandler
from datetime import datetime
from ssh import SSHConnection

logger = logging.getLogger(__name__)

class MyFileHandler(RotatingFileHandler):
    """
    ...
    """
    def rotate(self, source, dest):
        # logger.debug("Call rotate soure:{}, dest:{}".format(source, dest))
        source_file = source.split("/")[-1]
        dest_file = dest.split("/")[-1]
        print(source, source_file)
        print(dest, dest_file)

        super().rotate(source, dest)

        if self.ssh_open:

            put_result = self.ssh_connection.put(dest, self.destfile+dest_file)
            print(dest, "->", self.destfile+dest_file)
            # logger.debug("SSH put source:{} -> dest:{}, res: {}".format(dest,
            #                                                 self.destfile+dest,
            #                                                 put_result))
        else:
            raise Exception("No SSH connection!")
        #
        # if put_result:
        #     # remove log file
        #     pass

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
        logger.debug("Call setup_ssh")
        self.ssh_connection = SSHConnection(host, username, password, port)
        self.destfile = destfile
        self.ssh_open = True


def setup_log(logfile, destfile, maxBytes, backup,
                host, username, password, port):
    """
    Returns a custom rotating logger
    """
    logger.debug("Call setup_log")

    # add handler
    handler = MyFileHandler(logfile, maxBytes=300, backupCount=5)
    logger.debug("Created MyFileHandler")

    # setup ssh
    handler.setup_ssh(host, username, password, port, destfile)
    logger.debug("Added SSH config")

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
