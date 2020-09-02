from Ethminer import Ethminer
from datetime import datetime

def logger(msg):
    now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    f = open("/home/nebula/PycharmProjects/EthMinerAPI/log.txt", "w")
    msg = "%s- %s" % (now, msg)
    f.write(msg)
    f.close()

EthMinerApi = Ethminer(ip="192.168.1.4", port=3333)

Mh = EthMinerApi.getMh()

if(Mh < 45):
    msg = "Miner is running at %s Mh/s, restarting.\n" % Mh
    logger(msg)
    EthMinerApi.restart()
    print(msg)
else:
    print("Miner is running at %s Mh/s" % Mh)





