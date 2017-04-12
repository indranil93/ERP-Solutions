from abc import ABCMeta, abstractmethod

class APIService(object):
    
    @abstractmethod
    def get(self,uri,payload):    
        pass
    
    @abstractmethod
    def post(self,uri,payload):
        pass


