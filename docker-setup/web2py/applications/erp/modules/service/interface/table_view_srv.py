from abc import ABCMeta, abstractmethod

class TableViewService(object):

    @abstractmethod
    def get_companies_for_auth_user(self):    
        pass

    @abstractmethod
    def get_auth_user_purchase_table_view(self):
        pass

    @abstractmethod
    def get_auth_user_sale_table_view(self):
        pass

    @abstractmethod
    def get_auth_user_stock_table_view(self):
        pass
    
    @abstractmethod
    def get_auth_user_quotation_table_view(self):
        pass

    @abstractmethod
    def get_auth_user_company_table_view(self):
        pass
    
