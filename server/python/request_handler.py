from urlparse import parse_qs
from cgi import escape


def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!'

    d = parse_qs(environ['QUERY_STRING'])

    name = escape(d.get('name', [''])[0])

    response = output + ' ' + name

    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(response)))]
    start_response(status, response_headers)

    return [response]
