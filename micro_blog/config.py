CSRF_ENABLED = True # 激活 跨站点请求伪造 保护

SECRET_KEY = 'shi-yan-lou' # 仅当 CSRF 激活时需要，用来建立加密令牌以验证一个表单

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')