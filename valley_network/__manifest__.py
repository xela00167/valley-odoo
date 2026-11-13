{
    'name': 'Valley Network',
    'version': '19.0.1.0.0',
    'category': 'Services',
    'summary': 'Connect with Valley - The European Professional Network',
    'description': '''
Valley Network
==============

Join Valley, the European professional network where companies say what they need
right now and find the right people.

- Find partners
- Hire talent
- Meet investors

This app adds a Valley page to your Odoo instance with a direct link to join Valley.
    ''',
    'author': 'Valley Network',
    'website': 'https://valleynetwork.eu',
    'license': 'LGPL-3',
    'depends': ['base', 'web'],
    'data': [
        'views/valley_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'valley_network/static/src/valley_page/valley_page.js',
            'valley_network/static/src/valley_page/valley_page.xml',
            'valley_network/static/src/valley_page/valley_page.scss',
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
