from abc import ABCMeta, abstractmethod

class StockDAO(object):
    
    @abstractmethod
    def get_stock(self, user_id):
        pass

    @abstractmethod
    def get_auth_user_stock_table_view(self, user_id):
        pass
    
    @abstractmethod
    def get_trending_stock(self, user_id):
        pass