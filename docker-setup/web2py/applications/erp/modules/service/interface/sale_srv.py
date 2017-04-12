from abc import ABCMeta, abstractmethod

class SaleService(object):    

    @abstractmethod
    def insert_sale(self,data):
        pass

    @abstractmethod
    def get_sales_history_data(self):
        pass

    @abstractmethod
    def get_trending_purchaser(self):
        pass

    @abstractmethod
    def getget_auth_user_sale_data_period(self,data):
        pass

