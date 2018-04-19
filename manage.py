# -*- coding:utf-8 -*-
# 程序入口

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from iHome import get_app, db

# 使用工厂模式创建app
app = get_app('dev')

# 创建脚本管理对象
manager = Manager(app)

# 让迁移时，app和db建立关联
Migrate(app, db)

# 将数据迁移的脚本，命令添加到脚本管理了器对象
manager.add_command('db', MigrateCommand)


@app.route('/', methods=['POST', 'GET'])
def index():
    # redi_store.set('name','zxc')
    # 设置session
    # session['name']='zxc'

    return 'index'


if __name__ == '__main__':
    app.run()
