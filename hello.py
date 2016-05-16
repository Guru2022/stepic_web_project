def web_app(env, response):
    response('200 OK', [('Content-Type', 'text/plain')])
    print(env)
    return env["QUERY_STRING"].split('&')
