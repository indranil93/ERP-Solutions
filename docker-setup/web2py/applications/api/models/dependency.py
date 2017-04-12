"""file to manage all dependencies"""

from gluon import current

# from service.implementation.bill_srv_impl import BillServiceImplementation
# from service.implementation.company_srv_impl import CompanyServiceImplementation
# from service.implementation.purchase_srv_impl import PurchaseServiceImplementation
# from service.implementation.stock_srv_impl import StockServiceImplementation
# from service.implementation.sale_srv_impl import SaleServiceImplementation
# from service.implementation.quotation_srv_impl import QuotationServiceImplementation

from dao.implementation.bill_dao_impl import BillDAOImplementation
from dao.implementation.company_dao_impl import CompanyDAOImplementation
from dao.implementation.purchase_dao_impl import PurchaseDAOImplementation
from dao.implementation.stock_dao_impl import StockDAOImplementation
from dao.implementation.sale_dao_impl import SaleDAOImplementation
from dao.implementation.quotation_dao_impl import QuotationDAOImplementation

from handler.stock_handler import StockHandler
from handler.purchase_handler import PurchaseHandler
from handler.sale_handler import SaleHandler
from handler.bill_handler import BillHandler
from handler.quotation_handler import QuotationHandler
from handler.company_handler import CompanyHandler

current.bill_dao = BillDAOImplementation()
current.company_dao = CompanyDAOImplementation()
current.purchase_dao = PurchaseDAOImplementation()
current.stock_dao = StockDAOImplementation()
current.sale_dao = SaleDAOImplementation()
current.quotation_dao = QuotationDAOImplementation()

bill_dao = current.bill_dao
company_dao = current.company_dao
purchase_dao = current.purchase_dao
stock_dao = current.stock_dao
sale_dao = current.sale_dao
quotation_dao = current.quotation_dao

stock_handler = StockHandler()
bill_handler = BillHandler()
purchase_handler = PurchaseHandler()
sale_handler = SaleHandler()
quotation_handler = QuotationHandler()
company_handler = CompanyHandler()


# bill_service = BillServiceImplementation()
# company_service = CompanyServiceImplementation()
# purchase_service = PurchaseServiceImplementation()
# stock_service = StockServiceImplementation()
# sale_service = SaleServiceImplementation()
# quotation_service = QuotationServiceImplementation()