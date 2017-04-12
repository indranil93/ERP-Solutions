import cPickle
import json
from gluon import current
class CompanyHandler:
    
    def __init__(self):
        self.company_dao = current.company_dao
    
    def handle_request(self, request):
        args = request.args
        user_id = request.vars["user_id"]
        result= {}
        if args[0] == "user":
            result = self.company_dao.get_companies_for_auth_user(user_id)  
        result = { "data" : cPickle.dumps(result)}
        return result
        