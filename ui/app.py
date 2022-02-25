from Flask import flask

@app.route('/')
def index():
    return 'hi'
