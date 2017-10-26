# -*- coding: utf-8 -*-
{
    'name': "CloudNine Academy",

    'summary': """Manage trainings""",

    'description': """
        Modulo de Academia de CloudNine
    """,

    'author': "Franklin Marte",
    'website': "http://www.CloudNine.com.do",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Academia',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr.employee'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'templates.xml',
        'views/openacademy.xml',
        'views/maestros.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
