CONFIG = {
    # 'mode': 'wsgi',
    'working_dir': '/home/box/web/ask',
    # 'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8080',
        '--bind=unix:/tmp/gunicorn.sock',
        '--access-logfile=/home/box/gunicorn.log',
        'ask.wsgi:',
    ),
}

