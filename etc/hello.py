CONFIG = {
    # 'mode': 'wsgi',
    'working_dir': '/home/box/web',
    # 'python': '/usr/bin/python',
    '--access-logfile /home/box/gunicorn.log',
    'args': (
        '--bind=0.0.0.0:8080',
        'hello:web_app',
    ),
}
