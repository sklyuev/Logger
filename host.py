import paramiko

host = '192.168.56.101'
user = 'sklyuev'
secret = '283314'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
# stdin, stdout, stderr = client.exec_command('ls -l')
client_sftp = client.open_sftp()
print client_sftp.getcwd()
data = stdout.read() + stderr.read()
print(data.decode("utf-8"))
client.close()
