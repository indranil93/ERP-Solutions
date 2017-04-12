@auth.requires_login()
def index():
    """
        Shows quotations using database.
        
        Consraint: User should be authenticated.
        Returns locals variables to be used in view in html page.
    """
    quotation_table = table_view_service.get_auth_user_quotation_table_view()
    quotation_data = quotation_service.get_auth_user_quotation_data()
    # bill_data = quotation_service.get_auth_user_quote_bill_data()
    return locals()
    

@auth.requires_login()
def add_quotation():
    """
        Generates and adds quotations using database.
        
        Consraint: User should be authenticated.
        Returns locals variables to be used in view in html page.
    """
    companies = company_service.get_companies_for_auth_user()
    stock = stock_service.get_stock()
    return locals()

@auth.requires_login()
def insert_quotation():
    data = request.vars;    
    status = quotation_service.insert_quotation(data)   
    session.flash = status     
    redirect(URL("default","home"))
    
@auth.requires_login()
def generate():
    bill_no = request.args[0]
    company = ""    
    bill_data = quotation_service.get_generate_bill_data(bill_no)
    total_sum = quotation_service.get_total_bill_sum(bill_data)    
    return locals()

@auth.requires_login()
def transfer_quotation2Sale():
    bill_no = request.args[0]
    #data = quotation_service.get_auth_user_bill_quote(bill_no)
    status = quotation_service.transfer2sale(bill_no)
    session.flash = status
    if status != False:
        redirect(URL("default","home"))
    else:
        redirect(URL("default","error"))