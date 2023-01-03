# -*- coding: utf-8 -*-
{
    'name': "Header Custom Layout Report",
    'version': '16.0.1.0.0',
    'summary': 'A module to configure report header and footer',
    'description': 'A module to configure report header and footer manually from company form',
    'category': 'All',
    'license': 'LGPL-3',
    'depends': ['base','account'],
    'author': "Eng.Abdullah Essa",
    'data': [
        'report/base_document_layout.xml',
        'views/views.xml',
        # "data/report_paperformat.xml",
        # "report/account_report.xml",
        # "views/invoice_report.xml",
        "views/invoice_view.xml",
        "views/res_company.xml",
    ],
    'images': ['static/description/header_footer.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
