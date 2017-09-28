#!/usr/bin/env python
# coding:utf8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from app import create_app
from flask_script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# 如果已经定义了环境变量 'FLASK_CONFIG'，则从中读取配置名，否则使用默认配置
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__=='__main__':
    manager.run()