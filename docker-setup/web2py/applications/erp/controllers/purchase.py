@auth.requires_login()
def add():    
    suppliers = company_service.get_companies_for_auth_user()
    return locals()

@auth.requires_login()
def index():    
    purchase_table = table_view_service.get_auth_user_purchase_table_view()
    return locals()

@auth.requires_login()
def insert_purchase():
    data = request.vars;    
    res = purchase_service.insert_purchase(data)        
    session.flash = str(res) + str(" test")
    redirect(URL("default","home")) 