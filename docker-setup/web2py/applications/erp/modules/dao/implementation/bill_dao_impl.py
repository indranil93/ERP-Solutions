from gluon import current
from dao.interface.bill_dao import BillDAO

class BillDAOImplementation(BillDAO):
    def __init__(self):
        pass
    
    def get_auth_user_bill_data(self): 
        """
        Returns bill_data corresponding to particular sale from sales_material table.

        Constraints: User should be authenticated.
        Response: bill_number,company,purchase_date.
        """   
        db = current.db
        auth = current.auth
        data = db(db.sales_materials.user_id == auth.user.id).select(db.sales_materials.bill_no,db.sales_materials.company,db.sales_materials.purchase_date,groupby=db.sales_materials.bill_no)
        return data

    def get_generate_bill_data(self,data):
        """
        Generates bill_data corresponding to given bill_no.

        Selects the bill_data corresponding to given user and bill_no.
        Response: Returns bill_data correspoding to particular bill_no.
        """
        db = current.db
        auth = current.auth
        data = db(db.sales_materials.user_id == auth.user.id and db.sales_materials.bill_no == data).select()
        return data

    def get_max_bill_number(self):
        """
        Returns maximum bill_no from dales_material table in database.

        Returns the bill_no of latest bill to predict next bill_no to be generated.
        """
        db = current.db
        auth = current.auth
        max_bill_number = db(db.sales_materials).select(db.sales_materials.bill_no.max())[0]["MAX(sales_materials.bill_no)"]
        return max_bill_number
