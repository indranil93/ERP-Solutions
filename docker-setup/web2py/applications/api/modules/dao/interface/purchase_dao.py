from abc import ABCMeta, abstractmethod

class PurchaseDAO(object):

    @abstractmethod
    def insert_single_purchase(self, data):
        pass

    @abstractmethod
    def insert_multiple_purchase(self, data):
        pass

    @abstractmethod
    def get_trending_seller(self, user_id):
        pass

    @abstractmethod
    def get_auth_user_purchase_data_period(self,data):
        pass

