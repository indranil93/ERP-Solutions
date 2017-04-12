from abc import ABCMeta, abstractmethod

class QuotationService(object):    
    
    @abstractmethod
    def insert_quotation(self,data):
        pass
    
    @abstractmethod
    def get_auth_user_quotation_data(self):
        pass

    @abstractmethod
    def get_generate_bill_data(self,bill_no):
        pass

    @abstractmethod
    def get_total_bill_sum(self,bill_data):
        pass
        
    @abstractmethod
    def get_auth_user_bill_quote(self,bill_no):
        pass
    
    @abstractmethod
    def transfer2sale(self,data):
        pass