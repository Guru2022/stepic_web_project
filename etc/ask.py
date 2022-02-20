CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/git/stepic_web_project/ask',
    # 'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:80',
        'ask.wsgi:application',
    ),
}
