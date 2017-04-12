
from gluon.tools import Auth, Service, PluginManager

import time, datetime

auth = Auth(db)
auth.settings.login_next =  URL('home')
auth.settings.register_next = URL('home')

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
	# migrate='purchase.table'
	)

db.define_table('company',
	Field('user_id', 'reference auth_user', default=auth.user.id if auth.user else None, writable=False, readable=True),
	Field('name',requires=IS_NOT_EMPTY()),
	Field('address',requires=IS_NOT_EMPTY()),
	Field('phone',requires=IS_NOT_EMPTY()),
	Field('email',requires=IS_NOT_EMPTY()),
	# migrate='company.table'
	)

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
	# migrate='purchase_materials.table'
	)


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
	# migrate='sales_materials.table'
	)

db.define_table('stock',
	Field('user_id', 'reference auth_user', default=auth.user.id if auth.user else None, writable=False, readable=True),
	Field('description', requires=IS_NOT_EMPTY()),
	Field('quantity',requires=IS_NOT_EMPTY()),
	# migrate='stock.table'
	)

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
	Field('purchase_date','datetime',default=datetime.datetime.now()),
	Field('isActive','integer',default=1,requires=IS_NOT_EMPTY())
	# migrate='quotations.table'
	)

db.purchase_materials.company.requires = IS_IN_DB(db, 'company.id', '%(name)s') #IS_EMPTY_OR

db.sales_materials.company.requires = IS_IN_DB(db, 'company.id','%(name)s') #IS_EMPTY_OR

# Populate test data
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
	
	# add 

#allow basic login
auth.settings.allow_basic_login = True
#set thread local objects
from gluon import current

current.db = db
current.auth = auth