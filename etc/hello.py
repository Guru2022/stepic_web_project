CONFIG = {
    # 'mode': 'wsgi',
    'working_dir': '/home/box/web/hello.py',
    # 'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8080',
        'web_app',
    ),
}
