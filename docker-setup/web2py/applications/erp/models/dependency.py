"""file to manage all dependencies"""

from gluon import current

from service.implementation.bill_srv_impl import BillServiceImplementation
from service.implementation.company_srv_impl import CompanyServiceImplementation
from service.implementation.purchase_srv_impl import PurchaseServiceImplementation
from service.implementation.stock_srv_impl import StockServiceImplementation
from service.implementation.sale_srv_impl import SaleServiceImplementation
from service.implementation.quotation_srv_impl import QuotationServiceImplementation
from service.implementation.api_srv_impl import APIServiceImplementation
from service.implementation.table_view_srv_impl import TableViewServiceImplementation

from dao.implementation.bill_dao_impl import BillDAOImplementation
from dao.implementation.company_dao_impl import CompanyDAOImplementation
from dao.implementation.purchase_dao_impl import PurchaseDAOImplementation
from dao.implementation.stock_dao_impl import StockDAOImplementation
from dao.implementation.sale_dao_impl import SaleDAOImplementation
from dao.implementation.quotation_dao_impl import QuotationDAOImplementation
from dao.implementation.table_view_dao_impl import TableViewDAOImplementation

current.bill_dao = BillDAOImplementation()
current.company_dao = CompanyDAOImplementation()
current.purchase_dao = PurchaseDAOImplementation()
current.stock_dao = StockDAOImplementation()
current.sale_dao = SaleDAOImplementation()
current.quotation_dao = QuotationDAOImplementation()
current.table_view_dao = TableViewDAOImplementation()
current.api_service = APIServiceImplementation()

bill_service = BillServiceImplementation()
company_service = CompanyServiceImplementation()
purchase_service = PurchaseServiceImplementation()
stock_service = StockServiceImplementation()
sale_service = SaleServiceImplementation()
quotation_service = QuotationServiceImplementation()
table_view_service = TableViewServiceImplementation()
