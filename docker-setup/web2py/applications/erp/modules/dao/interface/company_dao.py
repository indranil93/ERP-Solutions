from abc import ABCMeta, abstractmethod

class CompanyDAO(object):

    @abstractmethod
    def get_companies_for_auth_user(self):
        pass