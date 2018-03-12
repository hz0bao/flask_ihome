# -*- coding: utf-8 -*-


# -*- coding:utf-8 -*-

import redis


class Config:
    """基本配置参数"""
    SECRET_KEY = "TQ6uZxn+SLqiLgVimX838/VplIsLbEP5jV7vvZ+Ohqw="

    # flask-sqlalchemy使用的参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:hz0bao@127.0.0.1:3306/ihome"  # 数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 追踪数据库的修改行为

    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    SESSION_TYPE='redis'
    SESSION_USE_SIGNER=True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用的redis实例

    PERMANENT_SESSION_LIFETIME = 86400

class DevelopmentConfig(Config):
    """开发模式的配置参数"""
    DEBUG = True

    # 支付宝
    ALIPAY_APPID = "2016091100489495"
    ALIPAY_URL = "https://openapi.alipaydev.com/gateway.do"


class ProductionConfig(Config):
    """生产环境的配置参数"""
    pass


config = {
    "development": DevelopmentConfig,  # 开发模式
    "production": ProductionConfig  # 生产/线上模式
}
