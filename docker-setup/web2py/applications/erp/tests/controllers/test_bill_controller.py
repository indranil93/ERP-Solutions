from override_login import override_login
"""
    Runs unit test on bill_controller.

    Overrides the user authentication to avoid module dependency in unit test.
    Is also provided with explicit login authentication details.
"""
def test_bill_page(web2py):         
    override_login(web2py)        
    result = web2py.run('bill', 'index', web2py)    
    result['auth'] = web2py.auth     
    html = web2py.response.render('bill/index.html', result)
    assert "Sales Bills" in html