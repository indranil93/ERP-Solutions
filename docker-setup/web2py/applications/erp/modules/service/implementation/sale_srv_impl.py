from gluon import current
from service.interface.sale_srv import SaleService

class SaleServiceImplementation(SaleService):

    def __init__(self):
        self.sale_dao = current.sale_dao
        self.bill_dao = current.bill_dao  
        self.api_service = current.api_service          

    def insert_sale(self,data):
        """
        Updates database with sales details.

        Inserts sales data instances in sales_materials table.
        Updates stock table also by directly communicating with sale_dao.
        """
        key = "description1"
        max_bill_no = self.bill_dao.get_max_bill_number()
        curr_bill_no = None
        res = {}
        if max_bill_no == None:
            curr_bill_no = 1
        else:
            curr_bill_no = int(max_bill_no) + 1
        if isinstance(data[key], list):        
            #self.sale_dao.insert_multiple_sale(data, curr_bill_no)
            data["curr_bill_no"] = curr_bill_no
            data["user_id"] = current.auth.user.id
            res = self.api_service.post("/sale/add/multiple", data)
        else:        
            #self.sale_dao.insert_single_sale(data, curr_bill_no)
            data["curr_bill_no"] = curr_bill_no
            data["user_id"] = current.auth.user.id
            res = self.api_service.post("/sale/add/single", data)
        return res
    
    def get_sales_history_data(self):
        """
        Returns the sales_history.

        Collects the sales data from sales_material table grouped by purchase_date and ordered by purchase date.
        Returns to dashboard view to show the statistics for analysis.
        """
        #sales_history = self.sale_dao.get_sales_history_data()   
        data = { "user_id" : current.auth.user.id}   
        sales_history = self.api_service.get("/sale/history", data)
        amount = []
        datetime = []
        date_amount = dict()
        for history_item in sales_history:
            current_date = history_item.purchase_date
            current_date = str(current_date)[:10]
            current_amount = history_item.amount
            if(current_date not in date_amount):
                date_amount[current_date] = float(current_amount)
            else:
                date_amount[current_date] = date_amount[current_date] + float(current_amount)
        date_amount = sorted(date_amount.items())
        for key,val in date_amount:
            amount.append(val)
            datetime.append(key)
        
        sales_history = [amount, datetime]
        return sales_history
    
    def get_trending_purchaser(self):
        """
        Returns the trending purchaser.

        Collects the company id of latest 5 sellers from purchase_material and joins it with company table to collect details 
        of 5 latest purchasers corresponding to various 5 company_id collected from purchase_material table.
        Directly communicates with sale_dao.
        """
        #purchaser_items = self.sale_dao.get_trending_purchaser()
        data = { "user_id" : current.auth.user.id}   
        purchaser_items = self.api_service.get("/sale/trending", data)

        purchaser_names = []
        for item in purchaser_items:
            purchaser_names.append(item.company.name)
        return purchaser_names
        

    def get_auth_user_sale_data_period(self,data):        
        #sale_data = self.sale_dao.get_auth_user_sale_data_period(data)
        data["user_id"] = current.auth.user.id
        sale_data = self.api_service.get("/sale/period", data)
        return sale_data


