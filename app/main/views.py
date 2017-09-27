# coding:utf8
from flask import jsonify, render_template, request, redirect
from . import main


@main.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/helloflask/')
def helloflask():
    return render_template('helloflask.html')


@main.route('/goodbyeflask/')
def goodbyeflask():
    return 'goodbye___flask'


@main.route('/user/<username>')
def show_username(username):
    return 'User %s' % username
