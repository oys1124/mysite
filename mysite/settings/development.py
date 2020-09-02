from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$+1j%_(44v=&)y05z#g_!+_-g)osqw3x$vxkbn2*eg((*_-&lq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME':'mysite_db',
    'USER': 'oys',
    'PASSWORD': 'oss11241209',
    'HOST': 'localhost',
    'PORT': 3306,
    }
}

# 发送邮件设置
# https://docs.djangoproject.com/en/2.0/ref/settings/#email
# https://docs.djangoproject.com/en/2.0/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '1144166030@qq.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']  # 授权码
EMAIL_SUBJECT_PREFIX = '[欧衍生的博客] '
EMAIL_USE_TLS = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)