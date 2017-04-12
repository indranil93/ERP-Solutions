from abc import ABCMeta, abstractmethod

class StockService(object):

    @abstractmethod
    def get_stock(self):
        pass

    @abstractmethod
    def get_trending_stock(self):
        pass

