from gluon import current
from service.interface.quotation_srv  import QuotationService

class QuotationServiceImplementation(QuotationService):

    def __init__(self):
        self.quotation_dao = current.quotation_dao
        self.bill_dao = current.bill_dao       
        self.api_service = current.api_service 
    
    def insert_quotation(self,data):
        """
        Inserts one instance or multiple instances in quotation table.

        Inserts one instance or multiple instances with next bill_no to curr_bill_no with corresponding details in data.
        Directly communicates with quotation_dao to collect data from database.
        """
        key = "description1"
        #max_bill_no = self.quotation_dao.get_max_quote_bill_no()
        data["user_id"] = current.auth.user.id
        max_bill_no = self.api_service.get("/quotation/max_bill_no", data)
        curr_bill_no = None
        if max_bill_no == None:
            curr_bill_no = 1
        else:
            curr_bill_no = int(max_bill_no) + 1
        if isinstance(data[key], list):        
            #self.quotation_dao.insert_multiple_quotaion(data, curr_bill_no)
            data["curr_bill_no"] = curr_bill_no
            return self.api_service.post("/quotation/add/multiple", data)
        else:        
            #self.quotation_dao.insert_single_quotation(data, curr_bill_no)
            data["curr_bill_no"] = curr_bill_no
            return self.api_service.post("/quotation/add/single", data)            
    
    def get_auth_user_quotation_data(self):
        """
        Returns quotation data from quotation table.

        Directly communicates with quotation_dao to collect data from database.
        Returns quotation data to html view of quotation page.
        """
        #data = self.quotation_dao.get_auth_user_quotation_data()
        data_send = {"user_id" : current.auth.user.id}
        data = self.api_service.get("/quotation/user", data_send)
        return data

    def get_generate_bill_data(self,bill_no):
        """
        Returns bill_data corresponding to current bill_no from quotation table.

        Directly communicates with quotation_dao to collect data from database.
        Returns bill_data to html view.
        """
        #data = self.quotation_dao.get_generate_bill_data(bill_no)
        data_send = {"user_id" : current.auth.user.id}
        data_send["bill_no"] = bill_no
        data = self.api_service.get("/quotation/bill", data_send)
        return data

    def get_total_bill_sum(self,bill_data):
        total_sum = 0
        for item in bill_data:
            company = item.company["name"]
            total_sum += float(item.amount)
        return total_sum


    def get_auth_user_bill_quote(self,bill_no):
        """
        Returns quotation corresponding to current bill_no from quotation table.

        Directly communicates with quotation_dao to collect data from database.
        Returns quotation to html view.
        """
        # data = self.quotation_dao.get_auth_user_bill_quote(bill_no)
        data_send = {"user_id" : current.auth.user.id}
        data_send["bill_no"] = bill_no
        data = self.api_service.get("/quotation/quote", data_send)
        return data

    def transfer2sale(self,bill_no):
        """
        Inserts details of corresponding material in quotation to sales_material once quotation is accepted.

        Directly communicates with quotation_dao to collect data from database.
        NOTE: Quotation may be for single item or multiple items so one instance or mupliple instances will be added respectively.
        Used when quotation is accepted and changed to bill.
        """        
        #key=data[0]['description']        
        #max_bill_no = self.bill_dao.get_max_bill_number()
        # data["user_id"] = current.auth.user.id
        max_bill_no = self.api_service.get("/bill/max_bill_no", {"user_id" : current.auth.user.id})
        curr_bill_no = None
        if max_bill_no == None:
            curr_bill_no = 1
        else:
            curr_bill_no = int(max_bill_no) + 1
        
        return self.api_service.post("/quotation/insert2sale", {"user_id" : current.auth.user.id, "curr_bill_no" : curr_bill_no, "bill_no" : bill_no})