# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():    
    if auth.user :
        redirect(URL("default","home"))    
    return dict(message=T('Welcome to web2py!'))

def user():    
    """        
        Returns authentication form grid.
        
        When user is not authenticated to log in it returns authentication form 
        grid by default,to be used in view of authentication page in html page.
    """    
    return dict(form=auth())

def generate_statement():
    data = request.vars
    purchase_data = purchase_service.get_auth_user_purchase_data_period(data)
    sale_data = sale_service.get_auth_user_sale_data_period(data) 
    p=0
    s=0

    for purchase in purchase_data:
        p += float(purchase["amount"])        
    for sale in sale_data:
        s += float(sale["amount"])        
    profit = s-p
    return locals()

def error():
    return locals()
    
@auth.requires_login()
def home():
    """
        Returns locals for home page.
        
        Consraint: User should be authenticated.
        Returns locals variables to be used in view of home page in html page.
    """
    stock_items = stock_service.get_trending_stock()    
    purchaser_items = sale_service.get_trending_purchaser()
    seller_items = purchase_service.get_trending_seller()
    return locals()