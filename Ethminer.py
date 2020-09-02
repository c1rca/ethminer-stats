import socket
import json

class Ethminer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def getStats(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.sendall('{"id":0,"jsonrpc":"2.0","method":"miner_getstat1"}\n'.encode('utf-8'))
        resp = ''
        while 1:
            data = s.recv(4096)
            resp += data.decode('utf-8')
            if not data or (len(data) < 4096 and data[-3:] == b']}\n'):
                break
        s.close()
        return resp

    def restart(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.sendall('{"id":0,"jsonrpc":"2.0","method":"miner_restart"}\n'.encode('utf-8'))
        resp = ''
        s.close()
        return resp

    def getMh(self):
        stats = json.loads(self.getStats())
        result = stats['result'][3]
        result = result.split(";")[0]
        Mh = int(str(result)[:2])
        return Mh
