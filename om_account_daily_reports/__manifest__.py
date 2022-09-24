# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Cash Book, Day Book, Bank Book Financial Reports',
    'version': '13.0.3.0.0',
    'category': 'Invoicing Management',
    'summary': 'Cash Book, Day Book and Bank Book Report For Odoo 13',
    'description': 'Cash Book, Day Book and Bank Book Report For Odoo 13',
    'sequence': '10',
    'author': 'Odoo Mates',
    'license': 'LGPL-3',
    'company': 'Odoo Mates',
    'maintainer': 'Odoo Mates',
    'support': 'odoomates@gmail.com',
    'website': 'https://www.odoomates.tech',
    'depends': ['account'],
    'live_test_url': '',
    'demo': [],
    'data': [
        'views/om_daily_reports.xml',
        'wizards/daybook.xml',
        'wizards/cashbook.xml',
        'wizards/bankbook.xml',
        'reports/reports.xml',
        'reports/report_daybook.xml',
        'reports/report_cashbook.xml',
        'reports/report_bankbook.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'live_test_url': 'https://www.youtube.com/watch?v=PEh-an8iCO0',
    'images': ['static/description/banner.gif'],
    'qweb': [],
}
