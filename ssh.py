import paramiko
import logging
logger = logging.getLogger(__name__)

class SSHConnection(object):
    """
    Provides API for SSH connection
    """

    def __init__(self, host, username, password, port):
        """
        Initialize and setup connection
        """
        logger.debug("Call SSHConnection constructor")
        self.sftp = None
        self.sftp_open = False

        # open SSH Transport stream
        self.transport = paramiko.Transport((host, port))
        self.transport.connect(username=username, password=password)

    def _openSFTPConnection(self):
        """
        Opens an SFTP connection if not already open
        """
        if not self.sftp_open:
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            self.sftp_open = True

    def get(self, remote_path, local_path):
        """
        Copies a file from the remote host to the local host.
        Returns True if file was copied successfully, otherwise returns False.
        """
        self._openSFTPConnection()
        res = False
        try:
            logger.debug("Call GET")
            self.sftp.get(remote_path, local_path)
        except FileNotFoundError:
            res = False
            logger.error("GET failed")
        else:
            res = True
        finally:
            return res

    def put(self, local_path, remote_path):
        """
        Copies a file from the local host to the remote host
        """
        self._openSFTPConnection()
        res = False
        try:
            logger.info("Call PUT")
            print(local_path, "->", remote_path)
            self.sftp.put(local_path, remote_path)
        except FileNotFoundError:
            logger.error("PUT failed")
            res = False
        else:
            res = True
        finally:
            return res

    def close(self):
        """
        Close SFTP connection and ssh connection
        """
        if self.sftp_open:
            self.sftp.close()
            self.sftp_open = False
        self.transport.close()

if __name__ == "__main__":
    host = '192.168.56.101'
    username = 'sklyuev'
    password = '283314'
    port = 22

    localpath = "/Users/sklyuev/Documents/github/Experiments/qwer.log"
    remotepath = "/home/sklyuev/test2.txt"
    ssh = SSHConnection(host, username, password, port)
    print(host, username, password, port)
    print("SSH obj:", ssh)
    # print(os.listdir("/home/sklyuev"))
    if(ssh.put(localpath, remotepath)):
        print("Success")
        pass
        # os.remove(filename)
        # print(os.listdir("/home/sklyuev"))
    # ssh.close()
