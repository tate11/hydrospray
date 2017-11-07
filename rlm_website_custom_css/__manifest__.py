# -*- coding: utf-8 -*-
{
    'name': "RLM Website Custom CSS",

    'summary': """
        Custom CSS Module""",

    'description': """
        Custom CSS Module 
    """,

    'author': "russ@redlabmedia.com",
    'website': "http://www.redlabmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/resources.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'css': ['static/src/css/custom.css'],
}