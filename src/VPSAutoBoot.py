from src.SVMC import SolusVMClient
from json import loads as jLoad
import time as t

"""
VPS AutoBoot

Author: Michael Dennis

"""

class AutoBoot:
    def __init__(self,**kwargs):

        self.logConfig = {
            'enabled': kwargs.get('log',False),
            'type': kwargs.get('logType','print'),
            'filePath': kwargs.get('logPath','out.log'),
            'level': kwargs.get('logLevel',0)
        }
        path = kwargs.get('configPath', './config.json')
        with open(path) as f:
            self.conf = jLoad(f.read())

    def runAll(self):
        host = self.conf['hostname']

        for server in self.conf['servers'].keys():
            self.runServer(
                server
            )

    def runServer(self,server):
        VM = SolusVMClient(
            self.conf['hostname'],
            self.conf['servers'][server]['key'],
            self.conf['servers'][server]['hash']
        )
        VMState = VM.status()['vmstat']

        if VMState != 'online':
            VM.boot()
            self._log("VM '"+server+"' is offline. booting",1)
        else:
            self._log("VM '"+server+"' is online.",0)

    def _log(self,message,importance=0):
        now = t.strftime('%Y-%m-%d %H:%M:%S', t.localtime())
        conf = self.logConfig
        if conf['enabled']:
            if importance >= conf['level']:
                msg = "[%s]  %s\n"%(now, message)

                if conf['type'] == 'file':
                    with open(conf['filePath'],'a') as f:
                        f.write(msg)
                else:
                    print(msg,end='')
