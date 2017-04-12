from gluon import current
from service.interface.table_view_srv import TableViewService

class TableViewServiceImplementation(TableViewService):
    def __init__(self):
        self.table_view_dao = current.table_view_dao

    def get_auth_user_stock_table_view(self):
        """
        Generates the table view from stock table.

        Returns table view with corresponding details.
        Not required to arrange in table explicily in html code.
        Directly communicates with table_view_dao to collect data from database and organized as table_view.
        """
        stock_table = self.table_view_dao.get_auth_user_stock_table_view()
        return stock_table
    
    def get_auth_user_sale_table_view(self):
        """
        Generates the table view from sales_materials table.

        Returns table view with corresponding details.
        Not required to arrange in table explicily in html code.
        Directly communicates with table_view_dao to collect data from database and organized as table_view.
        """
        sale_table = self.table_view_dao.get_auth_user_sale_table_view()
        return sale_table

    def get_auth_user_quotation_table_view(self):
        """
        Generates the table view from quotations table.

        Returns table view with corresponding details.
        Not required to arrange in table explicily in html code.
        Directly communicates with table_view_dao to collect data from database and organized as table_view.
        """
        quotation_table = self.table_view_dao.get_auth_user_quotation_table_view()
        return quotation_table

    def get_auth_user_purchase_table_view(self):
        """
        Generates the table view from purchase_materials table.

        Returns table view with corresponding details.
        Not required to arrange in table explicily in html code.
        Directly communicates with table_view_dao to collect data from database and organized as table_view.
        """
        table = self.table_view_dao.get_auth_user_purchase_table_view()
        return table

    def get_auth_user_company_table_view(self):
        """
        Generates the table view from companies table.

        Returns table view with corresponding details.
        Not required to arrange in table explicily in html code.
        Directly communicates with table_view_dao to collect data from database and organized as table_view.
        """
        table = self.table_view_dao.get_auth_user_company_table_view()
        return table