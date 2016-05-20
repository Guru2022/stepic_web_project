CONFIG = {
    'working_dir': '/home/box/web/ask',
    'args': (
        '--bind=0.0.0.0:8000',
        '--access-logfile=/home/box/gunicorn.log',
        'ask.wsgi:',
    ),
}

