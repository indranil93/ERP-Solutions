from override_login import override_login

def test_add_quotation_page(web2py):         
    override_login(web2py)        
    result = web2py.run('quotation', 'add_quotation', web2py)    
    result['auth'] = web2py.auth     
    html = web2py.response.render('quotation/add_quotation.html', result)
    assert "Quotation" in html