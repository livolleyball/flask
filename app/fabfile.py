# coding:utf8
from fabric.api import env,cd,run,sudo

env.hosts =['192.168.64.5']
env.user='root'
env.password ='liyi'

def hello():
    print "hello world"

def deploy():
    with cd('/root/flask'):

        run('pwd')
        run('ls')
        run('git pull')
        run('pip install -r requirments.txt -i https://pypi.douban.com/simple')
        run('python manage.py runserver')

