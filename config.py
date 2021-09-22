import configparser
from datetime import timedelta

cfg = configparser.ConfigParser()
cfg.read('.env')

class Config() :
    SQLALCHEMY_DATABASE_URI = '%s+%s://%s:%s@%s:3306/%s' % (
        cfg['database']['default_connection'],
        cfg['mysql']['driver'],
        cfg['mysql']['user'],
        cfg['mysql']['password'],
        cfg['mysql']['host'],
        cfg['mysql']['db']
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST = cfg['app']['host']
    PORT = cfg['app']['port']
    JWT_SECRET_KEY = cfg['jwt']['key']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=int(cfg['jwt']['time_live']))
    IPSTACK_KEY = cfg['ipstack']['key']
    IPSTACK_URL = cfg['ipstack']['url']

    ORATOR_DATABASES = {
        'default' : 'mysql',
        'mysql' : {
            'driver' : 'mysql',
            'host': cfg['mysql']['host'],
            'port': 3306,
            'database': cfg['mysql']['db'],
            'user': cfg['mysql']['user'],
            'password': cfg['mysql']['password']
        }
    }

    APP_KEY = cfg['app']['key']

class DevelopmentConfig(Config) :
    APP_DEBUG =True
    DEBUG = True


class ProductionConfig(Config) :
    APP_DEBUG = False
    DEBUG = False

class TestingConfig(Config) :
    APP_DEBUG = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = '%s+%s://%s:%s@%s:3306/%s_testing' % (
        cfg['database']['default_connection'],
        cfg['mysql']['driver'],
        cfg['mysql']['user'],
        cfg['mysql']['password'],
        cfg['mysql']['host'],
        cfg['mysql']['db']
    )