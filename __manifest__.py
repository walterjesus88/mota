# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 CCI Connect asbl (http://www.cciconnect.be) All Rights Reserved.
#                       Philmer <philmer@cciconnect.be>

{
    'name': 'mota-engil',
    'version': '1.0',
    'category': 'Accounting',
    'description': """
		Modulo Mota Engil
	""",
'data': [
        #'res_company_data.xml',
        #'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/pedidos_views.xml',
		'views/sale_order_extend.xml',
        'views/report_sale.xml',
        'reports/report_vale_entrega.xml',
        #'views/purchase_views.xml',
        'views/purchase_extend.xml',
		'views/product_template_views.xml',
		'reports/report_guia_remision.xml',
        'reports/guia_report.xml',
        'reports/report_proceso_mota.xml',
		'views/stock_views.xml',
        #'views/openacademy.xml',
        ],
'depends' : ['base', 'account', 'stock', 'sale','purchase'], 
}    
