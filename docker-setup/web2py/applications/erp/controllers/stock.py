@auth.requires_login()
def index():
    stock_table = table_view_service.get_auth_user_stock_table_view()
    return locals()    