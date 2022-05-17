import os

class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY')
    QUOTE_BASE_URL=os.environ.get('QUOTE_BASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    
    # email configs
    MAIL_SERVER='smtp.googlemail.com' 
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    FLASKY_ADMIN=os.environ.get('BLOGGY_ADMIN')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Blog]'
    FLASKY_MAIL_SENDER='Bloggy Admin <bloggy@gmail.com>'

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql://moringa:oa2exWako@localhost/bloggy'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://pfwxgletgmzxvl:7b88ccaca66cd11252eb6791652e09a3e155006981b4d5a7b1a580294423aead@ec2-44-195-169-163.compute-1.amazonaws.com:5432/d50c0cjh4bjm6s'

class TestingConfig(Config):
    TESTING = True
    pass 

config_options={
    'development' :DevConfig,
    'production' :ProdConfig,
    'testing':TestingConfig,
    'default':DevConfig
}