# coding:utf8
from flask import jsonify, render_template, request, redirect
from .forms import Select
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


@main.route('/select',methods=["GET", "POST"])
def select():
    form = Select()
    if request.method == 'POST':
        username = form.username.data
        SelectMultipleField = form.SelectMultipleField.data
        optSelectMultipleField = form.optSelectMultipleField.data
        return render_template('select.html', form=form, username=username, SelectMultipleField=SelectMultipleField,
                               optSelectMultipleField=optSelectMultipleField)

    return render_template('select.html', form=form)
