{
    'name': 'Station Management',
    'version': '1.0.0',
    'category': 'Station',
    'summary': 'Station Management system',
    'description': """This mod""",
    'depends': [],
    'data': [
        'security\ir.model.access.csv',
        'views\menu.xml',
        'views\customer_view.xml',
        r'views\train_view.xml',
        r'views\ticket_view.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
    'sequence': -100,
    'application': True,
}
