def application(env, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)

    return [b"Hello World from foobar application!\n"]