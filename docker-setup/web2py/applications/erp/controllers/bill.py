@auth.requires_login()
def index():    
    bill_data = bill_service.get_auth_user_bill_data()
    return locals()

@auth.requires_login()
def generate():
    """
        Generates bill using database.
        
        Consraint: User should be authenticated.
        Returns locals variables to be used in view in html page.
    """
    bill_no = request.args[0]
    company = ""    
    bill_data = bill_service.get_generate_bill_data(bill_no)
    company, total_sum = bill_service.get_total_bill_sum(bill_data)    
    return locals()