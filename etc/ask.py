CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/etc/ask',
    # 'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:80',
        'ask.wsgi:application',
    ),
}
