from abc import ABCMeta, abstractmethod

class QuotationDAO(object):
    
    @abstractmethod
    def insert_single_quotation(self,data,curr_bill_no):
        pass

    @abstractmethod
    def insert_multiple_quotaion(self,data,curr_bill_no):
        pass

    @abstractmethod
    def get_auth_user_quotation_data(self):
        pass

    @abstractmethod
    def get_auth_user_quote_bill_data(self):
        pass

    @abstractmethod
    def get_max_quote_bill_no(self):
        pass

    @abstractmethod
    def get_generate_bill_data(self,bill_no):
        pass

    @abstractmethod
    def get_auth_user_bill_quote(self,bill_no):
        pass

    @abstractmethod
    def insert2sale_single(self,data,curr_bill_no):
        pass

    @abstractmethod
    def insert2sale_multiple(self,data,curr_bill_no):
        pass
