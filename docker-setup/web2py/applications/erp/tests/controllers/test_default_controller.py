from override_login import override_login
"""
    Runs unit test on default_controller.

    Overrides the user authentication to avoid module dependency in unit test.
    Is also provided with explicit login authentication details.
"""

def test_index_page(web2py):    
    result = web2py.run('default', 'index', web2py)
    result['auth'] = web2py.auth    
    html = web2py.response.render('default/index.html', result)
    assert "Log in" in html

def test_home_page(web2py):    
    override_login(web2py)    
    result = web2py.run('default', 'home', web2py)    
    result['auth'] = web2py.auth     
    html = web2py.response.render('default/home.html', result)
    assert "Add Purchase" in html

