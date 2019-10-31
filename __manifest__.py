# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 CCI Connect asbl (http://www.cciconnect.be) All Rights Reserved.
#                       Philmer <philmer@cciconnect.be>

{
    'name': 'mota',
    'version': '1.0',
    'category': 'Accounting',
    'description': """
		prueba dd
	""",
'data': ['views/stock_views.xml','views/sale_order_extend.xml','views/stock_report.xml','views/sale_report.xml'],
'depends' : ['base', 'account', 'stock', 'sale'], 
}    
