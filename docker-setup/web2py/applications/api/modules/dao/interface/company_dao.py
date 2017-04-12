from abc import ABCMeta, abstractmethod

class CompanyDAO(object):

    @abstractmethod
    def get_companies_for_auth_user(self, user_id):
        pass

    @abstractmethod
    def get_auth_user_company_table_view(self, user_id):
        pass
