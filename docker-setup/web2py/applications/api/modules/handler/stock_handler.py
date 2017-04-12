import cPickle
import json
from gluon import current
class StockHandler:
    
    def __init__(self):
        self.stock_dao = current.stock_dao
    
    def handle_request(self, request):
        args = request.args
        user_id = request.vars["user_id"]
        result= {}
        if args[0] == "user":
            result = self.stock_dao.get_stock(user_id)    
        elif args[0] == "trending":
            result = self.stock_dao.get_trending_stock(user_id)
        result = { "data" : cPickle.dumps(result)}
        return result
