from werkzeug.wrappers import Request, Response


def read_image():
    with open('0.jpg', 'rb') as image:
        f = image.read()
        b = bytearray(f)
        return b

def server(environ, start_response):
    response = Response(content_type='image/ipeg')
    img = read_image()
    response.data = img
    response.headers['content-disposition'] = 'attachment; filename="0.jpg"'
    return response(environ, start_response)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 3000, server)
