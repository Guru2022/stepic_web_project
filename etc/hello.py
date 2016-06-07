CONFIG = {
    # 'mode': 'wsgi',
    'working_dir': '/home/dima/git/stepic_web_project',
    # 'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:80',
        '--bind=unix:/tmp/gunicorn.sock',
        '--access-logfile=/home/dima/gunicorn.log',
        'hello:web_app',
    ),
}
