from override_login import override_login
"""
    Runs unit test on sale_controller.

    Overrides the user authentication to avoid module dependency in unit test.
    Is also provided with explicit login authentication details.
"""

def test_sale_page(web2py):         
    override_login(web2py)
    result = web2py.run('sale', 'index', web2py)    
    result['auth'] = web2py.auth     
    html = web2py.response.render('sale/index.html', result)
    assert "Sales materialses" in html

def test_add_sale_page(web2py):         
    override_login(web2py)        
    result = web2py.run('sale', 'add', web2py)    
    result['auth'] = web2py.auth     
    html = web2py.response.render('sale/add.html', result)
    assert "Add Sale" in html