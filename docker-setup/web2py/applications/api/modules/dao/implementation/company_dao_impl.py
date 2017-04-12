from gluon import current, SQLFORM;
from dao.interface.company_dao import CompanyDAO

class CompanyDAOImplementation(CompanyDAO):    
    def __init__(self):
        pass

    def get_companies_for_auth_user(self, user_id):
        db = current.db
        auth = current.auth
        companies = db(db.company.user_id == user_id).select()
        return companies

    def get_auth_user_company_table_view(self, user_id):
        db = current.db
        auth = current.auth
        query = db.company.user_id==user_id
        table = SQLFORM.smartgrid(db.company,user_signature=False,constraints=dict(company=query), create=True)
        return table