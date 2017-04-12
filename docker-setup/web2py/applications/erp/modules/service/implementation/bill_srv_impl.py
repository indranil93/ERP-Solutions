from gluon import current
from service.interface.bill_srv import BillService
from dao.implementation.bill_dao_impl import BillDAOImplementation

class BillServiceImplementation(BillService):
    def __init__(self):
        self.bill_dao = current.bill_dao
        self.api_service = current.api_service

    def get_auth_user_bill_data(self):  
        """
        Responds to view with bill_data.

        Communicates directly with bill_dao to collect bill_data from sales material table.
        Returns with bill_data to view.
        """
        data = self.api_service.get("/bill/user", { "user_id" : current.auth.user.id})
        return data

    def get_generate_bill_data(self,data):
        """
        Responds to view with bill_data corresponding to given bill_no.

        Communicates directly with bill_dao to collect bill_data from sales material table.
        Returns with bill_data correspoding to particular bill_no to view in html.
        """    
        data = self.api_service.get("/bill/generate", { "user_id" : current.auth.user.id, "data" : data})
        return data

    def get_total_bill_sum(self,bill_data):
        """
        Returns total sum of bill_amount.

        To be used while generating bill.
        """
        total_sum = 0
        for item in bill_data:
            company = item.company["name"]
            total_sum += float(item.amount)
        return company, total_sum