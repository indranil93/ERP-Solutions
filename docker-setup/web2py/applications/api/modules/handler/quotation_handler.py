import cPickle
import json
from gluon import current
class QuotationHandler:
    
    def __init__(self):
        self.quotation_dao = current.quotation_dao
    
    def handle_request(self, request):
        args = request.args
        data = request.vars    
        result= {}
        if args[0] == "add":        
            curr_bill_no = data["curr_bill_no"]
            try:
                if args[1] == "single":                
                    result = self.quotation_dao.insert_single_quotation(data, curr_bill_no)
                elif args[1] == "multiple":
                    result = self.quotation_dao.insert_multiple_quotation(data, curr_bill_no)    
            except Exception as e:
                result =  str(e) + str(" || ") + str(data)
        elif args[0] == "insert2sale":     
            curr_bill_no = data["curr_bill_no"]        
            data = self.quotation_dao.get_auth_user_bill_quote(data["user_id"], data["bill_no"])
            try:
                if len(data) == 1:                
                    result = self.quotation_dao.insert2sale_single(data, curr_bill_no)
                else:
                    result = self.quotation_dao.insert2sale_multiple(data, curr_bill_no)    
                # result  =  str(" || ") + str(data) + " || " + str(data[0])
            except Exception as e:
                result =  str(e) + str(" || ") + str(data) + " || " + str(data[0])
        elif args[0] == "max_bill_no":
            result = self.quotation_dao.get_max_quote_bill_no(data["user_id"])        
        elif args[0] == "user":
            result = self.quotation_dao.get_auth_user_quotation_data(data["user_id"])     
            for item in result:
                tmp_dict = {}
                tmp_dict["name"] = item.company.name
                item.company = tmp_dict   
        elif args[0] == "bill":
            result = self.quotation_dao.get_generate_bill_data(data["user_id"], data["bill_no"])
            for item in result:
                tmp_dict = {}
                tmp_dict["name"] = item.company.name
                item.company = tmp_dict
        elif args[0] == "quote":
            result = self.quotation_dao.get_auth_user_bill_quote(data["user_id"], data["bill_no"])                        
        result = { "data" : cPickle.dumps(result)}
        return result
        