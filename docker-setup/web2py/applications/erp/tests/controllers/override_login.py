"""
fix test login
"""
def override_login(web2py):
    def requires_login(): 
        """ 
        decorator that prevents access to action if not logged in 
        """ 
        def decorator(action): 
            def f(*a, **b): 
                return action(*a, **b) 
            f.__doc__ = action.__doc__ 
            f.__name__ = action.__name__ 
            f.__dict__.update(action.__dict__) 
            return f    
        return decorator
    web2py.auth.requires_login = requires_login
    web2py.auth.settings.allow_basic_login = True    
    web2py.auth.user = web2py.auth.login_bare("adityagaykar@gmail.com","test1234")    
    return web2py