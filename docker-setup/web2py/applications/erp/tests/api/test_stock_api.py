import requests
import yaml, cPickle

def test_stock_user():    
    response = requests.get("http://stock/api/v1/stock/user", {"user_id" : 1})        
    response_dict = yaml.safe_load(response.content)
    assert "data" in response_dict

def test_stock_trending():
    response = requests.get("http://stock/api/v1/stock/trending", {"user_id" : 1})        
    response_dict = yaml.safe_load(response.content)
    assert "data" in response_dict
