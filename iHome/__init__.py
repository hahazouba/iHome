# -*- coding:utf-8 -*-
# 创建应用实例

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import configs

# 创建连接到mysql数据库的对象
db = SQLAlchemy()


def get_app(config_name):
    """使用工厂设计模式，根据传入的不同的config_name,找到不同的配置"""
    app = Flask(__name__)
    # 加载配置参数
    # app.config.from_object(Development)
    app.config.from_object(configs[config_name])

    # 创建链接到mysql数据库的对象
    # db = SQLAlchemy(app)
    db.init_app(app)

    # 创建链接到redis数据库的对象
    redis_store = redis.StrictRedis(host=configs[config_name].REDIS_HOST, port=configs[config_name].REDIS_PORT)

    # 开启CSRF保护：flask需要自己将csrf_token写入到浏览器的cookie
    CSRFProtect(app)
    # 使用flask_session将session数据写入到redis数据库
    Session(app)
    return app
