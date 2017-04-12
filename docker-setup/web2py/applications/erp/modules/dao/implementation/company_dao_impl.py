from gluon import current, SQLFORM;
from dao.interface.company_dao import CompanyDAO

class CompanyDAOImplementation(CompanyDAO):    
    def __init__(self):
        pass

    def get_companies_for_auth_user(self):
        """
        Communicates with database to fetch companies.

        Fetches companies and returns.
        """
        db = current.db
        auth = current.auth
        companies = db(db.company.user_id == auth.user.id).select()
        return companies

    