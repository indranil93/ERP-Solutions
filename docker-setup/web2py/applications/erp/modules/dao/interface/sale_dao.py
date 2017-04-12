from abc import ABCMeta, abstractmethod

class SaleDAO(object):

    @abstractmethod
    def insert_single_sale(self,data, curr_bill_no):
        pass

    @abstractmethod
    def insert_multiple_sale(self, data, curr_bill_no):
        pass
    
    @abstractmethod
    def get_sales_history_data(self):
        pass

    @abstractmethod
    def get_trending_purchaser(self):
        pass

    @abstractmethod
    def get_auth_user_sale_data_period(self,data):
        pass
