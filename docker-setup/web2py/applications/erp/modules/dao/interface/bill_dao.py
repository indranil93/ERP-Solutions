from abc import ABCMeta, abstractmethod

class BillDAO(object):

    @abstractmethod
    def get_auth_user_bill_data(self):    
        pass

    @abstractmethod
    def get_generate_bill_data(self,data): 
        pass

    @abstractmethod
    def get_max_bill_number(self):
        pass
