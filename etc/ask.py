CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/stepic_web_project/etc/ask',
    # 'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:80',
        'ask.wsgi:application',
    ),
}
