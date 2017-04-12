@auth.requires_login()
def index():
    sale_table = table_view_service.get_auth_user_sale_table_view()
    return locals()

@auth.requires_login()
def add():
    """
        Insert stock data in database.
        
        Consraint: User should be authenticated.
        Returns to view part.
    """
    companies = company_service.get_companies_for_auth_user()
    stock = stock_service.get_stock()
    return locals()   

@auth.requires_login()
def insert_sale():
    """
        Insert sales data in database.
        
        Consraint: User should be authenticated.
        Redirects to home page after insertion.
    """
    data = request.vars;    
    res = sale_service.insert_sale(data)
    session.flash = str(res)
    redirect(URL("default","home"))

@auth.requires_login()
def sale_history():
    sales_history_data = sale_service.get_sales_history_data()
    return response.json(sales_history_data)
