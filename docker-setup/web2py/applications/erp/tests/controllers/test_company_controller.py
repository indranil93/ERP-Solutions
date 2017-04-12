from override_login import override_login
"""
    Runs unit test on companies_controller.

    Overrides the user authentication to avoid module dependency in unit test.
    Is also provided with explicit login authentication details.
"""

def test_company_page(web2py):    
    override_login(web2py)    
    result = web2py.run('company', 'index', web2py)    
    result['auth'] = web2py.auth         
    html = web2py.response.render('company/index.html', result)
    assert "Companies" in html