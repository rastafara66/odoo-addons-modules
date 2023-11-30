# -*- coding: utf-8 -*-
{
    'name': "ATM - auto export/import orders",
    'summary': """Automatically creates a scheduled task to export/import orders to/from the json file""",
    'description': """Automatically creates a scheduled task to export/import orders to/from the json file""",
    'author': "chukhin",
    'website': "https://github.com/rastafara66",
    'category': 'Tools',
    'version': '16.0.1.23.11.38',
	'license': 'LGPL-3',
	'images': [
		'images/thumb.png',
		'images/atm_settings.png'
	],
	'price': 00.00,
	'currency': 'EUR',
    'depends': ['base',
                'account',
                'sale',
	],
    'data': [
		'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
		'views/res_config_settings_views.xml',
        'data/cron.xml',	
    ],
    'demo': [
        'data/product_demo.xml',
    ],
    #     'odoo.cron': [
    #     '1 1 * * * atm.OrderList.export_order_list_to_json()',
    # ],
}
