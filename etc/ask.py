CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/dima/git/stepic_web_project/ask',
    # 'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:80',
        'ask.wsgi:application',
    ),
}
