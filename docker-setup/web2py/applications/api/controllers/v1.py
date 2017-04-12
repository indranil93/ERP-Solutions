import cPickle
import json

def stock():
    result = stock_handler.handle_request(request)
    return response.json(result)

def purchase():
    result = purchase_handler.handle_request(request)
    return response.json(result)

def sale():
    result = sale_handler.handle_request(request)
    return response.json(result)

def quotation():
    result = quotation_handler.handle_request(request)
    return response.json(result)

def company():
    result = company_handler.handle_request(request)    
    return response.json(result)

def bill():
    result = bill_handler.handle_request(request)    
    return response.json(result)

    """
def stock():
    args = request.args
    user_id = request.vars["user_id"]
    result= {}
    if args[0] == "user":
        result = stock_dao.get_stock(user_id)    
    elif args[0] == "trending":
        result = stock_dao.get_trending_stock(user_id)
    result = { "data" : cPickle.dumps(result)}
    return response.json(result)

def purchase():
    args = request.args
    data = request.vars
    result= {}
    if args[0] == "add":
        try:
            if args[1] == "single":                
                result = purchase_dao.insert_single_purchase(data)
            elif args[1] == "multiple":
                result = purchase_dao.insert_multiple_purchase(data)    
        except Exception as e:
            result =  str(e) + str(" || ") + str(data)
    elif args[0] == "trending":
        result = purchase_dao.get_trending_seller(data["user_id"]) 
    elif args[0] == "period":
        result = purchase_dao.get_auth_user_purchase_data_period(data)                
    result = { "data" : cPickle.dumps(result)}
    return response.json(result)

def sale():
    args = request.args
    data = request.vars    
    result= {}
    if args[0] == "add":
        curr_bill_no = data["curr_bill_no"]
        try:
            if args[1] == "single":                
                result = sale_dao.insert_single_sale(data, curr_bill_no)
            elif args[1] == "multiple":
                result = sale_dao.insert_multiple_sale(data, curr_bill_no)    
        except Exception as e:
            result =  str(e) + str(" || ") + str(data)
    elif args[0] == "trending":
        result = sale_dao.get_trending_purchaser(data["user_id"])        
    elif args[0] == "history":
        result = sale_dao.get_sales_history_data(data["user_id"])        
    elif args[0] == "period":
        result = sale_dao.get_auth_user_sale_data_period(data)                
    result = { "data" : cPickle.dumps(result)}
    return response.json(result)

def quotation():
    args = request.args
    data = request.vars    
    result= {}
    if args[0] == "add":        
        curr_bill_no = data["curr_bill_no"]
        try:
            if args[1] == "single":                
                result = quotation_dao.insert_single_quotation(data, curr_bill_no)
            elif args[1] == "multiple":
                result = quotation_dao.insert_multiple_quotation(data, curr_bill_no)    
        except Exception as e:
            result =  str(e) + str(" || ") + str(data)
    elif args[0] == "insert2sale":     
        curr_bill_no = data["curr_bill_no"]        
        data = quotation_dao.get_auth_user_bill_quote(data["user_id"], data["bill_no"])
        try:
            if len(data) == 1:                
                result = quotation_dao.insert2sale_single(data, curr_bill_no)
            else:
                result = quotation_dao.insert2sale_multiple(data, curr_bill_no)    
            # result  =  str(" || ") + str(data) + " || " + str(data[0])
        except Exception as e:
            result =  str(e) + str(" || ") + str(data) + " || " + str(data[0])
    elif args[0] == "max_bill_no":
        result = quotation_dao.get_max_quote_bill_no(data["user_id"])        
    elif args[0] == "user":
        result = quotation_dao.get_auth_user_quotation_data(data["user_id"])     
        for item in result:
            tmp_dict = {}
            tmp_dict["name"] = item.company.name
            item.company = tmp_dict   
    elif args[0] == "bill":
        result = quotation_dao.get_generate_bill_data(data["user_id"], data["bill_no"])
        for item in result:
            tmp_dict = {}
            tmp_dict["name"] = item.company.name
            item.company = tmp_dict
    elif args[0] == "quote":
        result = quotation_dao.get_auth_user_bill_quote(data["user_id"], data["bill_no"])                        
    result = { "data" : cPickle.dumps(result)}
    return response.json(result)

def company():
    args = request.args
    user_id = request.vars["user_id"]
    result= {}
    if args[0] == "user":
        result = company_dao.get_companies_for_auth_user(user_id)  
    result = { "data" : cPickle.dumps(result)}
    return response.json(result)

def bill():
    args = request.args
    user_id = request.vars["user_id"]
    result= {}
    if args[0] == "user":
        result = bill_dao.get_auth_user_bill_data(user_id)  
        for item in result:
            tmp_dict = {}
            tmp_dict["name"] = item.company.name
            item.company = tmp_dict
    elif args[0] == "generate":
        data = request.vars["data"]
        result = bill_dao.get_generate_bill_data(data, user_id)        
        for item in result:
            tmp_dict = {}
            tmp_dict["name"] = item.company.name
            item.company = tmp_dict
    elif args[0] == "max_bill_no":
        data = request.vars
        result = bill_dao.get_max_bill_number(data["user_id"])
    result = { "data" : cPickle.dumps(result)}
    return response.json(result)

    """