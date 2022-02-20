CONFIG = {
    # 'mode': 'wsgi',
    'working_dir': '/home/box/web/stepic_web_project',
    # 'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:80',
        '--bind=unix:/tmp/gunicorn.sock',
        '--access-logfile=/home/box/web/stepic_web_project/gunicorn.log',
        'hello:web_app',
    ),
}
