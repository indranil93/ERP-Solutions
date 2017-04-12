from gluon import current, SQLFORM
from dao.interface.purchase_dao import PurchaseDAO

class PurchaseDAOImplementation(PurchaseDAO):
    def __init__(self):
        pass

    def insert_single_purchase(self, data):
        db = current.db
        auth = current.auth
        #insert purchase
        db.purchase_materials.insert(description=data["description1"],
                    quantity=data["quantity1"],
                    rate=data["rate1"],
                    company=data["company1"],
                    payment=data["payment1"],
                    amount=data["amount1"],
                    vat=data["vat1"],
                    purchase_date=data["purchase_date1"],
                    user_id=data["user_id"]
                    )
        stock_count = db(  db.stock.user_id == data["user_id"] and db.stock.description == data["description1"]).select()
        if len(stock_count) == 0:
            db.stock.insert(user_id=data["user_id"],description=data["description1"],quantity=data["quantity1"])
        else:
            db( db.stock.user_id == data["user_id"] and db.stock.description == data["description1"]).update(quantity=(int(stock_count[0].quantity) + int(data["quantity1"])))            
        return { "result" : "OK" }

    def insert_multiple_purchase(self,data):        
        db = current.db
        auth = current.auth             
        #insert purchases
        key = "description1"
        total = len(data[key])   
        res = "OK" 
        for i in range(total):               
            db.purchase_materials.insert(description=data["description1"][i],
                quantity=data["quantity1"][i],
                rate=data["rate1"][i],
                company=data["company1"],
                payment=data["payment1"][i],
                amount=data["amount1"][i],
                vat=data["vat1"][i],
                purchase_date=data["purchase_date1"],
                user_id=data["user_id"]
                )            
            stock_count = db(db.stock.user_id == data["user_id"] and db.stock.description == data["description1"][i]).select()            
            if len(stock_count) == 0:
                db.stock.insert(user_id=data["user_id"],description =data["description1"][i],quantity=data["quantity1"][i])                
            else:
                db(db.stock.user_id == data["user_id"] and db.stock.description == data["description1"][i]).update(quantity=(int(stock_count[0].quantity) + int(data["quantity1"][i])))
        return { "result" : res  }
    

    def get_trending_seller(self, user_id):
        db = current.db
        auth = current.auth        
        seller_items = db(db.sales_materials.user_id == user_id).select(join=db.company.on(db.sales_materials.company == db.company.id), orderby=~db.sales_materials.purchase_date, groupby=db.sales_materials.company, limitby=(0,5))
        return seller_items

    def get_auth_user_purchase_data_period(self,data):
        db=current.db
        auth = current.auth
        purchase_data = db(db.purchase_materials.user_id == data["user_id"] and db.purchase_materials.purchase_date >= data["from_date"] and db.purchase_materials.purchase_date <= data["to_date"]).select()
        return purchase_data