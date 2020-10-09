import paramiko as ssh

class SSHTool():
    def __init__(self, host, user, auth,
            via=None, via_user=None, via_auth=None):
        if via:
            t0 = ssh.Transport(via)
            t0.start_client()
            t0.auth_password(via_user, via_auth);
            # setup forwarding from 127.0.0.1:<free_random_port> to |host|
            channel = t0.open_channel('direct-tcpip', host, ('127.0.0.1',1234))
            self.transport = ssh.Transport(channel)
        else:
            self.transport = ssh.Transport(host)
        self.transport.start_client()
        self.transport.auth_password(user, auth)

    def run(self, cmd):
        ch = self.transport.open_session()
        ch.set_combine_stderr(True)
        ch.exec_command(cmd)
        retcode = ch.recv_exit_status()
        buf = ''
        while  ch.recv_ready():
            buf += ch.recv(1024)
        retuen (buf, retcode)

host=("192.168.24,10", 22)
opflex=("10.197.145.211",22)
via_host = ("10.197.143.95",22)
ssht = SSHTool(host, "heat-admin", "",
        via=via_host, via_user="root", via_auth="insieme")
print(ssht.run("ovs-vsctl list qos"))



