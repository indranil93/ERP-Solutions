import requests
import yaml, cPickle

def test_quotation_user():
    response = requests.get("http://quotation/api/v1/quotation/user", {"user_id" : 1})        
    response_dict = yaml.safe_load(response.content)
    assert "data" in response_dict

def test_quotation_bill():
    response = requests.get("http://quotation/api/v1/quotation/bill", {"user_id" : 1, "bill_no" : 1})        
    response_dict = yaml.safe_load(response.content)
    assert "data" in response_dict

def test_quotation_quote():
    response = requests.get("http://quotation/api/v1/quotation/quote", {"user_id" : 1, "bill_no" : 1})        
    response_dict = yaml.safe_load(response.content)
    assert "data" in response_dict