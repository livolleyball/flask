# coding:utf8
from fabric.api import env,cd,run,sudo

env.hosts =['192.168.64.5']
env.user='root'
env.password ='liyi'

def hello():
    print "hello world"

def deploy():
    with cd('/'):
        run('git pull')
        sudo('python app/app.py')

