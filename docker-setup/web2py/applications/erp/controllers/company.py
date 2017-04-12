@auth.requires_login()
def index():        
    """
        Collects comapny data using database.
        
        Consraint: User should be authenticated.
        Returns locals variables to be used in view in html page.
    """
    company_table = table_view_service.get_auth_user_company_table_view()
    return locals()
