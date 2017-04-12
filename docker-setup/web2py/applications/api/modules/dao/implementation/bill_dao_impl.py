from gluon import current
from dao.interface.bill_dao import BillDAO

class BillDAOImplementation(BillDAO):
    def __init__(self):
        pass
    
    def get_auth_user_bill_data(self, user_id):    
        db = current.db
        auth = current.auth
        data = db(db.sales_materials.user_id == user_id).select(db.sales_materials.bill_no,db.sales_materials.company,db.sales_materials.purchase_date,groupby=db.sales_materials.bill_no)
        return data

    def get_generate_bill_data(self,data, user_id):
        db = current.db
        auth = current.auth
        data = db(db.sales_materials.user_id == user_id and db.sales_materials.bill_no == data).select()
        return data

    def get_max_bill_number(self, user_id):
        db = current.db
        auth = current.auth
        max_bill_number = db(db.sales_materials.user_id == user_id).select(db.sales_materials.bill_no.max())[0]["MAX(sales_materials.bill_no)"]
        return max_bill_number
