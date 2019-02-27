# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'VTiger Base Connector Calender',
    'version': '11.0.1.0.0',
    'category': '',
    'license': 'AGPL-3',
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'maintainer': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'https://www.serpentcs.com',
    'depends': [
        'vtiger_connector_base',
        'calendar',
    ],
    'data': [
        'views/res_company_view.xml',
        'views/calendar_views.xml',
    ],
    'installable': True,
}
