import requests
import yaml, cPickle

def test_company_user():
    response = requests.get("http://company/api/v1/company/user", {"user_id" : 1})        
    response_dict = yaml.safe_load(response.content)
    assert "data" in response_dict