from abc import ABCMeta, abstractmethod

class BillDAO(object):

    @abstractmethod
    def get_auth_user_bill_data(self, user_id):    
        pass

    @abstractmethod
    def get_generate_bill_data(self,data, user_id): 
        pass

    @abstractmethod
    def get_max_bill_number(self, user_id):
        pass
