import requests
import yaml, cPickle

def test_sale_trending():
    response = requests.get("http://sale/api/v1/sale/trending", {"user_id" : 1})        
    response_dict = yaml.safe_load(response.content)
    assert "data" in response_dict