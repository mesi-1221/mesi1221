# -*- coding: utf-8 -*-
{
    'name': 'Withhold Amount',
    'version': '16.0.1.1.0',
    "sequence": -100,
    'category': 'Sales Management',
    'summary': "withholding on Total ",
    'depends': ['account'],
    'data': [
        # 'views/inherit_grand_total.xml',
        'views/withholding_view.xml',
    ],
    "web.assets_backend": [

    ],
    "installable": True,
    "currency": "ETB",
    "application": True,
    "auto_install": False,
}
