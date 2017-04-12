from abc import ABCMeta, abstractmethod

class CompanyService(object):

    @abstractmethod
    def get_companies_for_auth_user(self):    
        pass    