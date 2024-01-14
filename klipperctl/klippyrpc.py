import json
import logging
from os import getpid
from typing import Optional, Dict, List


class KlippyRPCRequest(object):
    RPCCounter=100 # This is used for generating IDs when they are not specified. It would be better to not do this.
    __id: Optional[int]
    method: str
    params: Optional[Dict]

    def __init__(self, method: str, id=None, **kwargs):
        self.method = method
        self.params = None
        if id:
            self.__id = id
        else:
            self.__id = None
        if kwargs:
            for argk, argv in kwargs.items():
                self[argk] = argv

    def __getitem__(self, key):
        if not self.params:
            return None
        if key not in self.params:
            return None
        return self.params[key]

    def __setitem__(self, key, value):
        if not self.params:
            self.params = {}
            self.params[key] = value

    @property
    def id(self):
        if not self.__id:
            self.__id = self.__generate_id()
        return self.__id

    @id.setter
    def id(self, value):
        if self.__id:
            logging.warning("Overriding the ID of an RPC request which already has an ID. This is probably not what you want")
        self.__id = value
        return value

    @staticmethod
    def __generate_id():
        RPC_COUNTER_MAX=1000000
        generated_id = getpid()*RPC_COUNTER_MAX+(KlippyRPCRequest.RPCCounter%RPC_COUNTER_MAX)
        KlippyRPCRequest.RPCCounter+=1
        return generated_id
        
    
    def encode(self, add_etx: bool = True):
        payload = { 
                   'id': self.id,
                   'method': self.method
                  }
        if self.params:
            payload['params'] = self.params
        return json.dumps(payload) + "\x03" if add_etx else ""
