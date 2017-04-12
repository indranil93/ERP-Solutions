from override_login import override_login

"""
    Runs unit test on purchase_controller.

    Overrides the user authentication to avoid module dependency in unit test.
    Is also provided with explicit login authentication details.
"""
def test_purchase_page(web2py):         
    override_login(web2py)      
    result = web2py.run('purchase', 'index', web2py)    
    result['auth'] = web2py.auth     
    html = web2py.response.render('purchase/index.html', result)
    assert "Purchase materialses" in html

def test_add_purchase_page(web2py):         
    override_login(web2py)        
    result = web2py.run('purchase', 'add', web2py)    
    result['auth'] = web2py.auth     
    html = web2py.response.render('purchase/add.html', result)
    assert "Add Purchase" in html