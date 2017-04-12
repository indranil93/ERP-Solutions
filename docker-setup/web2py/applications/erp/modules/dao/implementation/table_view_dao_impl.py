from gluon import current, SQLFORM
from dao.interface.table_view_dao import TableViewDAO

class TableViewDAOImplementation(TableViewDAO):
    def __init__(self):
        pass
    
    def get_auth_user_stock_table_view(self):
        """
        Generates the table view from stock table.

        Returns table view with corresponding details.
        Not required to arrange in table explicily in html code.
        """
        db = current.db
        auth = current.auth
        query = db.stock.user_id==auth.user.id
        stock_table = SQLFORM.smartgrid(db.stock,user_signature=False,constraints=dict(stock=query), create=False)
        return stock_table

    def get_auth_user_sale_table_view(self):
        """
        Generates the table view from sales_materials table.

        Returns table view with corresponding details.
        Not required to arrange in table explicily in html code.
        """
        db = current.db
        auth = current.auth
        query = db.sales_materials.user_id==auth.user.id
        sale_table = SQLFORM.smartgrid(db.sales_materials,user_signature=False,constraints=dict(sales_materials=query), create=False)
        return sale_table

    def get_auth_user_quotation_table_view(self):
        """
        Generates the table view from quotations table.

        Returns table view with corresponding details.
        Not required to arrange in table explicily in html code.
        """
        db = current.db
        auth = current.auth
        query = db.quotation.user_id==auth.user.id
        quotation_table = SQLFORM.smartgrid(db.quotation,user_signature=False,constraints=dict(sales_materials=query), create=False)
        return quotation_table

    def get_auth_user_purchase_table_view(self):
        """
        Generates the table view from purchase_materials table.

        Returns table view with corresponding details.
        Not required to arrange in table explicily in html code.
        """
        db = current.db
        auth = current.auth
        query = db.purchase_materials.user_id==auth.user.id
        purchase_table = SQLFORM.smartgrid(db.purchase_materials,user_signature=False,constraints=dict(purchase_materials=query), create=False)
        return purchase_table
    
    def get_auth_user_company_table_view(self):
        """
        Generates the table view from company table.

        Returns table view with corresponding details.
        Not required to arrange in table explicily in html code.
        """
        db = current.db
        auth = current.auth
        query = db.company.user_id==auth.user.id
        table = SQLFORM.smartgrid(db.company,user_signature=False,constraints=dict(company=query), create=True)
        return table