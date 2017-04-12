# Inventory Management System - web2py app

### Packages required
* Python 2.7
### Steps to start server
* $ cd web2py
* $ python web2py.py -a 'test1234' -i 127.0.0.1 -p 8000

### Step to start application in browser
* load http://localhost:8000/erp

### Admin user
* username : adityagaykar@gmail.com
* password : test1234

###We are now on aws

### File changes for dev environment setup
* appconfig.ini - update db uri
* web2pytest.py - update test db path
* env var in config - no_proxy=localhost
* fake-migrate fix - try this if you get table already defined error
