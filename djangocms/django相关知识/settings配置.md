## settings配置

- ##### redis缓存配置

  1. 安装django-redis

     ```python
     pip install django-redis
     ```

  2. settions增加配置

     ```python
     REDIS_URI = redis://:password@host:port/db		# 有密码
     # REDIS_URI = redis://host:port/db	# 无密码
     # redis://:JXh6jtPtAN@r-2zee71e834c4pd.redis.rds.aliyuncs.com:6390/0  例子
     CACHES = {
         'default': {
             'BACKEND': 'django_redis.cache.RedisCache',
             'LOCATION': REDIS_URI,
             'TIMEOUT': 86400,  # 1 day,0缓存将失效,None永不过期
             'OPTIONS': {
                 "CLIENT_CLASS": "django_redis.client.DefaultClient",
                 'MAX_ENTRIES': 1000,
                 'CULL_FREQUENCY': 3,
             },
             "KEY_PREFIX": "gk_sx_api"
         }
     }
     ```

     

