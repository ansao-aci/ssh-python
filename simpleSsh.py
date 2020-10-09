import paramiko as ssh

host=("10.197.143.95", 22)
t0 = ssh.Transport(host)
t0.start_client()

user="root"
password="insieme"
t0.auth_password(user,password)

ch = t0.open_session()
ch.set_combine_stderr(True)
ch.exec_command("su - stack")
retcode = ch.recv_exit_status()
buf=b''
while ch.recv_ready():
    buf+=(ch.recv(1024))
print(buf.decode('utf-8'))




