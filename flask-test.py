from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
    <html>
    <head><title>my flask app</title></head>
    <body><h1>Hello from Flask</h1>
    <marquee>hi welcome from my app</marquee>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
