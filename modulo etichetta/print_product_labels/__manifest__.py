# -*- coding: utf-8 -*-
{
    'name': "print_product_labels",

    'summary': """
       prodotto""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    # NB i report vanno inseriti in fondo alla lista dei data
    'data': [
        # 'security/ir.model.access.csv',
        'data/report_paperformat.xml',
        'report/print_label_product_report.xml',
        'report/print_etichetta.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
