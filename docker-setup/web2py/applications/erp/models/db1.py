
from gluon.tools import Auth, Service, PluginManager

import time, datetime

auth = Auth(db)
auth.settings.login_next =  URL('default', 'home')
auth.settings.register_next = URL('default', 'home')

"""
       Manages purchase details by vendors.
"""
db.define_table('purchase',
	Field('user_id', 'reference auth_user', default=auth.user.id if auth.user else None, writable=False, readable=True),
	Field('purchase_date','date',requires=IS_NOT_EMPTY()),
	Field('company_name',requires=IS_NOT_EMPTY()),
	Field('address',requires=IS_NOT_EMPTY()),
	Field('mail_id'),
	Field('phone_no'),
	Field('invoice_no',requires=IS_NOT_EMPTY(),unique=True),
	Field('vat_no'),
	Field('vat_amount','double'),
	Field('total_amount','double'),
	#migrate='purchase.table'
	)


"""
        Manages purchaser and vendor company details.
"""
db.define_table('company',
	Field('user_id', 'reference auth_user', default=auth.user.id if auth.user else None, writable=False, readable=True),
	Field('name',requires=IS_NOT_EMPTY()),
	Field('address',requires=IS_NOT_EMPTY()),
	Field('phone',requires=IS_NOT_EMPTY()),
	Field('email',requires=IS_NOT_EMPTY()),
	#migrate='company.table'
	)


"""
        Manages purchase material details.

		purchase material is bought from to suppliers.

"""
db.define_table('purchase_materials',
	Field('user_id', 'reference auth_user', default=auth.user.id if auth.user else None, writable=False, readable=True),
	Field('description',requires=IS_NOT_EMPTY()),
	Field('quantity',requires=IS_NOT_EMPTY()),
	Field('rate','double',requires=IS_NOT_EMPTY()),
	Field('vat','double',requires=IS_NOT_EMPTY()),
	Field('company','reference company'),
	Field('amount','double', requires=IS_NOT_EMPTY()),
	Field('payment', requires=IS_IN_SET(("PENDING","CASH","RTGS", "CREDIT CARD", "DEBIT CARD", "OTHER")),default="PENDING"),
	Field('purchase_date','datetime',default=datetime.datetime.now()),
	#migrate='purchase_materials.table'
	)

"""
        Manages sales material details.
		
		Sales material is sold to vendors.
		Also used to generate bill(invoice)

"""
db.define_table('sales_materials',
	Field('user_id', 'reference auth_user', default=auth.user.id if auth.user else None, writable=False, readable=True),
	Field('description',requires=IS_NOT_EMPTY()),
	Field('quantity',requires=IS_NOT_EMPTY()),
	Field('rate','double',requires=IS_NOT_EMPTY()),
	Field('vat','double',requires=IS_NOT_EMPTY()),
	Field('company','reference company'),
	Field('bill_no','integer', requires=IS_NOT_EMPTY()),
	Field('amount', requires=IS_NOT_EMPTY()),
	Field('payment', requires=IS_IN_SET(("PENDING","CASH","RTGS", "CREDIT CARD", "DEBIT CARD", "OTHER")),default="PENDING"),	
	Field('purchase_date','datetime',default=datetime.datetime.now()),	
	Field('amount','double'),
	#migrate='sales_materials.table'
	)

"""
        Manages stock details.
		
		To be checked while selling Sales material sold to vendors.

"""
db.define_table('stock',
	Field('user_id', 'reference auth_user', default=auth.user.id if auth.user else None, writable=False, readable=True),
	Field('description', requires=IS_NOT_EMPTY()),
	Field('quantity',requires=IS_NOT_EMPTY()),
	#migrate='stock.table'
	)

"""
       	Manages Quotation details.
		
		Used to generate quotations.

"""
db.define_table('quotation',
	Field('user_id','reference auth_user',default=auth.user.id if auth.user else None, writable=False,readable=True), #reference_auth_user giving error.. Query Not Supported.
	Field('description',requires=IS_NOT_EMPTY()),
	Field('quantity',requires=IS_NOT_EMPTY()),
	Field('rate','double',requires=IS_NOT_EMPTY()),
	Field('vat','double',requires=IS_NOT_EMPTY()),
	Field('company','reference company'),
	Field('bill_no','integer', requires=IS_NOT_EMPTY()),
	Field('amount','double', requires=IS_NOT_EMPTY()),
	Field('payment', requires=IS_IN_SET(("PENDING","CASH","RTGS", "CREDIT CARD", "DEBIT CARD", "OTHER")),default="PENDING"),
	Field('isActive','integer',default=1,requires=IS_NOT_EMPTY()),
	Field('purchase_date','datetime',default=datetime.datetime.now()),
	#migrate=True,fake_migrate=True
	)

db.purchase_materials.company.requires = IS_IN_DB(db, 'company.id', '%(name)s') #IS_EMPTY_OR

db.sales_materials.company.requires = IS_IN_DB(db, 'company.id','%(name)s') #IS_EMPTY_OR

# Populate test data

"""
	Provides explicit login details while running unit tests.

	Unit test run should not use an authenticated  session always as it needs to be independent 
	of authentication module. Thus we provide explicit authentication tails to run unit test on 
	that particular module
"""
if web2pytest.is_running_under_test(request, request.application):
    # add user
	check_user = db(db.auth_user.id == 1).select()
	if not check_user or len(check_user) == 0:
		db.auth_user.insert(            
				password = db.auth_user.password.validate('test1234')[0],
				email = 'adityagaykar@gmail.com',
				first_name = 'Aditya',
				last_name = 'Gaykar',
				role = 'admin',
				id="1"
			)
		db.commit()			
#set thread local objects
from gluon import current

current.db = db
current.auth = auth