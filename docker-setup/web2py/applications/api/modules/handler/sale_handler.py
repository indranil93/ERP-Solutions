import cPickle
import json
from gluon import current
class SaleHandler:
    
    def __init__(self):
        self.sale_dao = current.sale_dao
    
    def handle_request(self, request):
        args = request.args
        data = request.vars    
        result= {}
        if args[0] == "add":
            curr_bill_no = data["curr_bill_no"]
            try:
                if args[1] == "single":                
                    result = self.sale_dao.insert_single_sale(data, curr_bill_no)
                elif args[1] == "multiple":
                    result = self.sale_dao.insert_multiple_sale(data, curr_bill_no)    
            except Exception as e:
                result =  str(e) + str(" || ") + str(data)
        elif args[0] == "trending":
            result = self.sale_dao.get_trending_purchaser(data["user_id"])        
        elif args[0] == "history":
            result = self.sale_dao.get_sales_history_data(data["user_id"])        
        elif args[0] == "period":
            result = self.sale_dao.get_auth_user_sale_data_period(data)                
        result = { "data" : cPickle.dumps(result)}        
        return result