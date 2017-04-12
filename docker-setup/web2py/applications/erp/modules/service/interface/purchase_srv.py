from abc import ABCMeta, abstractmethod

class PurchaseService(object):

    @abstractmethod
    def insert_purchase(self, data):
        pass

    @abstractmethod
    def get_trending_seller(self):
        pass

    @abstractmethod
    def get_auth_user_purchase_data_period(self,data):
        pass