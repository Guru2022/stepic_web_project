CONFIG = {
    # 'mode': 'wsgi',
    'working_dir': '/home/box/web',
    # 'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:80',
        '--bind=unix:/tmp/gunicorn.sock',
        '--access-logfile=/home/box/gunicorn.log',
        'hello:web_app',
    ),
}
