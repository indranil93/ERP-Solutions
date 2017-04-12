from gluon import current, SQLFORM
from dao.interface.quotation_dao import QuotationDAO

class QuotationDAOImplementation(QuotationDAO):

    def __init__(self):
        pass

    def insert_single_quotation(self,data,curr_bill_no):
        """
        Inserts one instance in quotation table.

        Inserts one instance with next bill_no to curr_bill_no with corresponding details in data.
        """
        db = current.db
        auth = current.auth
        db.quotation.insert(description=data["description1"],
                quantity=data["quantity1"],
                rate=data["rate1"],
                vat=data["vat1"],
                company=data["company1"],
                bill_no=curr_bill_no,
                payment=data["payment1"],
                amount=data["amount1"],
                isActive=1,
                purchase_date=data["purchase_date1"]
                )
        db(db.quotation.bill_no ==  curr_bill_no).update(isActive=1)
        rows = db(db.quotation.bill_no == curr_bill_no).select()
    
    def insert_multiple_quotaion(self,data,curr_bill_no):
        """
        Inserts multiple instances in quotation table.
        
        Inserts multiple instances next consecutive bill_nos to curr_bill_no with corresponding details in data.
        """
        db = current.db
        auth = current.auth
        key = "description1"
        total = len(data[key])
        # print "TOTAL : ",total
        for i in range(total):                
            db.quotation.insert(description=data["description1"][i],
                quantity=data["quantity1"][i],
                rate=data["rate1"][i],
                vat=data["vat1"][i],
                company=data["company1"],
                payment=data["payment1"][i],
                bill_no=curr_bill_no,
                amount=data["amount1"][i],
                purchase_date=data["purchase_date1"]
                )

    def get_auth_user_quotation_data(self):
        """
        Returns quotation data from quotation table.

        Returns quotation data to quotation_srv .
        """
        db = current.db
        auth = current.auth
        quotation_data = db(db.quotation.user_id == auth.user.id).select(db.quotation.isActive,db.quotation.bill_no,db.quotation.company,db.quotation.purchase_date,groupby=db.quotation.purchase_date)
        return quotation_data

    def get_max_quote_bill_no(self):
        """
        Returns maximum bill_no from quotation table.

        Returns maximum bill_no for choosing the next bill_no for new quotation.
        """
        db = current.db
        auth = current.auth
        max_bill_number = db(db.quotation).select(db.quotation.bill_no.max())[0]["MAX(quotation.bill_no)"]
        return max_bill_number

    def get_generate_bill_data(self,bill_no):
        """
        Returns bill_data corresponding to current bill_no from quotation table.
        """
        db = current.db
        auth = current.auth
        data = db(db.quotation.user_id == auth.user.id and db.quotation.bill_no == bill_no).select()
        return data

    def get_auth_user_bill_quote(self,bill_no):
        """
        Returns quotation corresponding to current bill_no from quotation table.
        """
        db = current.db;
        auth = current.auth
        data = db(db.quotation.user_id == auth.user.id and db.quotation.bill_no == bill_no).select()
        return data
    
    def can_be_sold_single(self,stock_count,quote_quantity):
        """
        Returns true if stock has corresponding quantity of particular item.

        Used as check while generating quotations.
        """
        return stock_count >= quote_quantity

    def can_be_sold_multiple(self,data):
        """
        Returns true if stock has corresponding quantities of corresponding items.

        Used as check while generating quotations.
        """
        db = current.db
        auth = current.auth
        key = "description"
        total = len(data)
        print "TOTAL : ",total
        quotation_quantity_count = dict()
        for i in range(total):
            stock_count_row = db(db.stock.description == data[i]["description"]).select()
            stock_count = int(stock_count_row[0]["quantity"])
            if data[i]["description"] not in quotation_quantity_count.keys():
                quotation_quantity_count[data[i]["description"]] = int(data[i]["quantity"])
            else:
                quotation_quantity_count[data[i]["description"]] += int(data[i]["quantity"])
            if stock_count < quotation_quantity_count[data[i]["description"]]:
                return False
        return True

    def insert2sale_single(self,data,curr_bill_no):
        """
        Inserts details of corresponding material in quotation to sales_material once quotation is accepted.

        NOTE: Quotation is for single item so one instance will be added.
        """
        db=current.db
        auth=current.auth
        stock_count = db(db.stock.description == data[0]["description"]).select()
        if self.can_be_sold_single(int(stock_count),int(data[0]["quantity"])):
            db.sales_materials.insert(description=data[0]["description"],
                    quantity=data[0]["quantity"],
                    rate=data[0]["rate"],
                    vat=data[0]["vat"],
                    company=data[0]["company"],
                    payment=data[0]["payment"],
                    amount=data[0]["amount"],
                    bill_no=curr_bill_no,
                    purchase_date=data[0]["purchase_date"]
                    )
            db(db.quotation.bill_no == data[0]["bill_no"]).update(isActive=0)
            if len(stock_count) == 0:
                db.stock.insert(description =data[0]["description"],quantity=data[0]["quantity"])
            else:
                db(db.stock.description == data[0]["description"]).update(quantity=(int(stock_count[0].quantity) - int(data[0]["quantity"])))
            return True
        else:
            return False
        
    def insert2sale_multiple(self,data,curr_bill_no):
        """
        Inserts details of corresponding materials in quotation to sales_material once quotation is accepted.

        NOTE: Quotation is for multiple items so multiple instances will be added.
        """
        db = current.db
        auth = current.auth
        key = "description"
        total = len(data)
        quotation_quantity_count = dict()
        if self.can_be_sold_multiple(data):   
            for i in range(total):
                print "insert row:",i,data[i]
                stock_count_row = db(db.stock.description == data[i]["description"]).select()
                stock_count = int(stock_count_row[0]["quantity"])    
                db.sales_materials.insert(description=data[i]["description"],
                    quantity=data[i]["quantity"],
                    rate=data[i]["rate"],
                    vat=data[i]["vat"],
                    company=data[i]["company"],
                    payment=data[i]["payment"],
                    bill_no=curr_bill_no,
                    amount=data[i]["amount"],
                    purchase_date=data[i]["purchase_date"]
                    )
                db(db.stock.description == data[i]["description"]).update(quantity=stock_count - int(data[i]["quantity"]))
        else:
            return False
        db(db.quotation.bill_no == data[0]["bill_no"]).update(isActive=0)
        return True