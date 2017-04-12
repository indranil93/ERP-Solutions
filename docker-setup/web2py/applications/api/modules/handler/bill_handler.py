import cPickle
import json
from gluon import current
class BillHandler:
    
    def __init__(self):
        self.bill_dao = current.bill_dao
    
    def handle_request(self, request):
        args = request.args
        user_id = request.vars["user_id"]
        result= {}
        if args[0] == "user":
            result = self.bill_dao.get_auth_user_bill_data(user_id)  
            for item in result:
                tmp_dict = {}
                tmp_dict["name"] = item.company.name
                item.company = tmp_dict
        elif args[0] == "generate":
            data = request.vars["data"]
            result = self.bill_dao.get_generate_bill_data(data, user_id)        
            for item in result:
                tmp_dict = {}
                tmp_dict["name"] = item.company.name
                item.company = tmp_dict
        elif args[0] == "max_bill_no":
            data = request.vars
            result = self.bill_dao.get_max_bill_number(data["user_id"])
        result = { "data" : cPickle.dumps(result)}
        return result