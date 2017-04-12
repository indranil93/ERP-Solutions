from gluon import current
from service.interface.purchase_srv import PurchaseService
import json
import cPickle

class PurchaseServiceImplementation(PurchaseService):
    def __init__(self):
        self.purchase_dao = current.purchase_dao
        self.api_service = current.api_service

    def insert_purchase(self,data):
        """
        Updates database with purchase details.

        Inserts purchase data instances in purchase_materials table.
        Updates stock table also by directly communicating with purchase_dao.
        """
        key = "description1"
        data["user_id"] = current.auth.user.id
        res = ""
        if isinstance(data[key], list):
            #print data[key], "is list"
            #self.purchase_dao.insert_multiple_purchase(data)                    
            res = self.api_service.post("/purchase/add/multiple", data)
        else:
            #print data[key], "is not list"
            #self.purchase_dao.insert_single_purchase(data)            
            res = self.api_service.post("/purchase/add/single", data)
        return res
        
    def get_trending_seller(self):
        """
        Returns the trending seller.

        Collects the company id of latest 5 sellers from sales_material and joins it with company table to collect details 
        of 5 latest sellers corresponding to various 5 company_id collected from sales_material table.
        Directly communicates with purchase_dao.
        """
        #seller_items = self.purchase_dao.get_trending_seller()
        data = { "user_id" : current.auth.user.id}
        seller_items = self.api_service.get("/purchase/trending", data)
        seller_names = []
        for item in seller_items:
            seller_names.append(item.company.name)
        return seller_names

    def get_auth_user_purchase_data_period(self,data):
        db=current.db
        auth=current.auth        
        #purchase_data = self.purchase_dao.get_auth_user_purchase_data_period(data)
        data["user_id"] = current.auth.user.id
        purchase_data = self.api_service.get("/purchase/period", data)
        return purchase_data


    
