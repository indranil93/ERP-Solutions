from gluon import current, SQLFORM
from dao.interface.stock_dao import StockDAO

class StockDAOImplementation(StockDAO):

    def __init__(self):
        pass        

    def get_stock(self):
        """
        Returns the stock_items from stock table.

        Collects the stock_items details from stock table showing stock_items available in warehouse currently.
        """
        db = current.db
        auth = current.auth
        stock = db(db.stock.quantity > 0 and db.stock.user_id == auth.user.id).select()
        return stock    

    def get_trending_stock(self):
        """
        Returns the trending stock_items being sold.

        Collects the stock_items details of latest 5 stock_items from sales_material 
        ordered by purchase_date to track the latest demand in market.
        """
        db = current.db
        auth = current.auth
        query = db.sales_materials.user_id == auth.user.id
        stock_items = db(query).select(db.sales_materials.description, orderby=~db.sales_materials.purchase_date, distinct=True,limitby=(0, 5))
        return stock_items