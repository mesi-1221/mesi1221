# -*- coding: utf-8 -*-
{
    'name': 'Withhold on Total Amount',
    'version': '16.0.1.1.0',
    "sequence": -100,
    'category': 'Sales Management',
    'summary': "Discount on Total ",
    'depends': ['account'],
    'data': [
        # 'views/inherit_grand_total.xml',
        'views/withholding_view.xml',
    ],
    "web.assets_backend": [

    ],
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    "auto_install": False,
}
