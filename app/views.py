from app import blg


@blg.route('/')
@blg.route('/index')
def index():
    return "Hello, World"
