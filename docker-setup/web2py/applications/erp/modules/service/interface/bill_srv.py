from abc import ABCMeta, abstractmethod

class BillService(object):
    
    @abstractmethod
    def get_auth_user_bill_data(self):    
        pass
    
    @abstractmethod
    def get_generate_bill_data(self,data):
        pass

    @abstractmethod
    def get_total_bill_sum(self):
        pass


