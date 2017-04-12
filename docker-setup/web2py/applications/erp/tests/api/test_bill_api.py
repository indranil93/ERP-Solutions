import requests
import yaml, cPickle
def test_bill_user():
    response = requests.get("http://bill/api/v1/bill/user", {"user_id" : 1})        
    response_dict = yaml.safe_load(response.content)
    assert "data" in response_dict

def test_bill_generate():
    response = requests.get("http://bill/api/v1/bill/generate", {"user_id" : 1, "data" : 1})        
    response_dict = yaml.safe_load(response.content)
    assert "data" in response_dict