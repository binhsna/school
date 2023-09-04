# -*- coding: utf-8 -*-
{
    'name': 'School',
    'summary': 'school',
    'sequence': 1,
    'description': """App quản lý trường học""",
    'version': '12.0.0.1',
    'author': 'Binh Nguyen Cong',
    'website': 'https://www.odoo.com/page/school-management',
    'category': 'school',
    'depends': ['website'],
    'data': [
        'views/school_view.xml',
        'views/class_view.xml',
        'views/student_view.xml',
        'views/subject_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
