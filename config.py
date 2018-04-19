# -*- coding:utf-8 -*-
# 配置

import redis


class Config(object):
    DEBUG = True
    # 密钥
    SECRET_KEY = ''
    # 配置mysql数据库：真是开发不写127，写数据库真是的ip
    SQLALCHEMY_DARABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/iHome'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis数据库：实际开发使用redis数据库的真实ip
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 配置session参数
    # 指定session存储到redis
    SESSION_TYPE = 'redis'
    # 指定要使用的redis的位置
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 是否要使用secret_key签名session_data
    SESSION_USE_SIGNER = True
    # 设置session的过期时间
    PERMANENT_SESSION_LIFETIME = 3600 * 24  # 有效期为一天


class Development(Config):
    """开发模式下的配置"""
    pass


class Production(Config):
    """生产环境、线上、部署之后"""
    DEBUG = False
    SQLALCHEMY_DARABASE_URI = 'msyql://root:mysql@127.0.0.1:3306/iHome'
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 2  # 有效期为两天


class UnitTest(Config):
    """测试环境"""
    TESTING = True
    SQLALCHEMY_DARABASE_URI = 'msyql://root:mysql@127.0.0.1:3306/iHome'


# 准备工厂要使用的原材料
configs = {
    'dev': Development,
    'pro': Production,
    'test': UnitTest,
}
