import cPickle
import json
from gluon import current
class PurchaseHandler:
    
    def __init__(self):
        self.purchase_dao = current.purchase_dao    
    
    def handle_request(self, request):
        args = request.args
        data = request.vars
        result= {}
        if args[0] == "add":
            try:
                if args[1] == "single":                
                    result = self.purchase_dao.insert_single_purchase(data)
                elif args[1] == "multiple":
                    result = self.purchase_dao.insert_multiple_purchase(data)    
            except Exception as e:
                result =  str(e) + str(" || ") + str(data)
        elif args[0] == "trending":
            result = self.purchase_dao.get_trending_seller(data["user_id"]) 
        elif args[0] == "period":
            result = self.purchase_dao.get_auth_user_purchase_data_period(data)                
        result = { "data" : cPickle.dumps(result)}        
        return result