from wsgiref.simple_server import make_server

class application(object):
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        response_body = ['%s: %s' % (key, value)
                         for key, value in sorted(self.environ.items())]
        response_body = '\n'.join(response_body)

        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain'),
                            ('Content-Length', str(len(response_body)))]
        self.start_response(status, response_headers)
        yield response_body.encode("utf-8")

httpd = make_server(
    '192.168.0.210',
    8077,
    application
)

httpd.handle_request()
