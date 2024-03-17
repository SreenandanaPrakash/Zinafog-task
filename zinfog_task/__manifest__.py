# -*- coding: utf-8 -*-
{
    'name': "sale order custom",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Sreenandana",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/deliverycharge_view_.xml',
        'wizard/wizard.xml',
        'report/sales_report_template.xml',

    ],

}
