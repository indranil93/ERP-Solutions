from gluon import current
from service.interface.company_srv import CompanyService
from dao.implementation.company_dao_impl import CompanyDAOImplementation

class CompanyServiceImplementation(CompanyService):
    
    def __init__(self):
        self.api_service = current.api_service
    
    def get_companies_for_auth_user(self): 
        """
        Returns company data from companies table by directly communication to company_dao.
        """   
        companies = self.api_service.get("/company/user", {"user_id" : current.auth.user.id})
        return companies

