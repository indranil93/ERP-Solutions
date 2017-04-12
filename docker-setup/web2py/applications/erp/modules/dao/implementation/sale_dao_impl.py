from gluon import current, SQLFORM
from dao.interface.sale_dao import SaleDAO

class SaleDAOImplementation(SaleDAO):

    def __init__(self):
        pass

    def insert_single_sale(self,data, curr_bill_no):
        """
        Inserts single sales data to database.

        Inserts one instance in sales_materials table to manage details of sale.
        Inserts one instance in stock to manage stock of sold material.
        """
        db = current.db
        auth = current.auth
        db.sales_materials.insert(description=data["description1"],
                quantity=data["quantity1"],
                rate=data["rate1"],
                vat=data["vat1"],
                company=data["company1"],
                payment=data["payment1"],
                amount=data["amount1"],
                bill_no=curr_bill_no,
                purchase_date=data["purchase_date1"]
                )
        stock_count = db(db.stock.description == data["description1"]).select()
        if len(stock_count) == 0:
            db.stock.insert(description =data["description1"],quantity=data["quantity1"])
        else:
            db(db.stock.description == data["description1"]).update(quantity=(int(stock_count[0].quantity) - int(data["quantity1"])))        

    def insert_multiple_sale(self,data, curr_bill_no):
        """
        Inserts multiple sales data to database.

        Inserts multiple instances in sales_materials table to manage details of sales.
        Inserts mutiple instances in stock to manage stocks of sold material.
        """
        db = current.db
        auth = current.auth
        key = "description1"
        total = len(data[key])
        print "TOTAL : ",total
        for i in range(total):                
            db.sales_materials.insert(description=data["description1"][i],
                quantity=data["quantity1"][i],
                rate=data["rate1"][i],
                vat=data["vat1"][i],
                company=data["company1"],
                payment=data["payment1"][i],
                bill_no=curr_bill_no,
                amount=data["amount1"][i],
                purchase_date=data["purchase_date1"]
                )
            stock_count = db(db.stock.description == data["description1"][i]).select()
            if len(stock_count) == 0:
                db.stock.insert(description =data["description1"][i],quantity=data["quantity1"][i])
            else:
                db(db.stock.description == data["description1"][i]).update(quantity=(int(stock_count[0].quantity) - int(data["quantity1"][i])))
    
    def get_sales_history_data(self):
        """
        Returns the sales_history.

        Collects the sales data from sales_material table grouped by purchase_date and ordered by purchase date.
        Returns to sale_srv to return to dashboard view to show the statistics for analysis.
        """
        db = current.db
        auth = current.auth
        sales_history = db(db.sales_materials.user_id == auth.user.id).select(db.sales_materials.amount,db.sales_materials.purchase_date,groupby=db.sales_materials.purchase_date, orderby=db.sales_materials.purchase_date)
        return sales_history

    def get_trending_purchaser(self):
        """
        Returns the trending purchaser.

        Collects the company id of latest 5 purchasers from sales_material and joins it with company table to collect details 
        of 5 latest purchasers corresponding to various 5 company_id collected from purchases_material table.
        """
        db = current.db
        auth = current.auth
        purchaser_items = db(db.purchase_materials).select(join=db.company.on(db.purchase_materials.company == db.company.id), orderby=~db.purchase_materials.purchase_date, groupby=db.purchase_materials.company, limitby=(0,5))
        return purchaser_items

    def get_auth_user_sale_data_period(self,data):
        db=current.db
        auth = current.auth
        sale_data = db(db.sales_materials.user_id == auth.user_id and db.sales_materials.purchase_date >= data["from_date"] and db.sales_materials.purchase_date <= data["to_date"]).select()
        return sale_data
