# coding:utf8
from flask import Flask, jsonify, render_template, request,redirect
app = Flask(__name__)


@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test_redirect')
def test_redirect():
    return redirect('https://www.baidu.com')

@app.route('/test_redirect_flask')
def test_redirect_flask():
    return redirect('http://flask.pocoo.org/')

if __name__ == '__main__':
    app.run(debug=True)