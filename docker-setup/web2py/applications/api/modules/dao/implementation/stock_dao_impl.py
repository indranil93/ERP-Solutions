from gluon import current, SQLFORM
from dao.interface.stock_dao import StockDAO

class StockDAOImplementation(StockDAO):

    def __init__(self):
        pass        

    def get_stock(self,user_id):
        db = current.db
        auth = current.auth
        stock = db(db.stock.quantity > 0 and db.stock.user_id == user_id).select()
        return stock

    def get_auth_user_stock_table_view(self, user_id):
        db = current.db        
        query = db.stock.user_id==user_id
        stock_table = SQLFORM.smartgrid(db.stock,user_signature=False,constraints=dict(stock=query), create=False)
        return stock_table

    def get_trending_stock(self,user_id):
        db = current.db        
        query = db.sales_materials.user_id == user_id
        stock_items = db(query).select(db.sales_materials.description, orderby=~db.sales_materials.purchase_date, distinct=True,limitby=(0, 5))
        return stock_items