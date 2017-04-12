import requests
import yaml, cPickle


def test_purchase_trending():
    response = requests.get("http://purchase/api/v1/purchase/trending", {"user_id" : 1})        
    response_dict = yaml.safe_load(response.content)
    assert "data" in response_dict