def web_app(env, response):
    response('200 OK', [('Content-Type', 'text/plain')])
    env["wsgi.errors"].write(str(env))
    return "\n".join(env["QUERY_STRING"].split('&'))
