
from gluon import current
from service.interface.stock_srv import StockService
import requests
from requests.auth import HTTPBasicAuth
import yaml
import cPickle

class StockServiceImplementation(StockService):
    def __init__(self):
        self.api_service = current.api_service
    
    def get_stock(self):  
        """
        Returns the stock_items from stock table.

        Collects the stock_items details from stock table showing stock_items available in warehouse currently.
        Directly communicates with stock_dao to collect data from database.
        """  
        stock = self.api_service.get("/stock/user", {"user_id" : current.auth.user.id})
        return stock

    def get_trending_stock(self):  
        """
        Returns the trending stock_items being sold.

        Collects the stock_items details of latest 5 stock_items from sales_material 
        ordered by purchase_date to track the latest demand in market.
        Directly communicates with stock_dao to collect data from database.
        """              
        stock_items = self.api_service.get("/stock/trending", {"user_id": current.auth.user.id})
        trending_items = []
        for item in stock_items:            
            trending_items.append(item.description)
        return trending_items