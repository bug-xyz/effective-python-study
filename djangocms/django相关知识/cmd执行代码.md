## cmd执行代码

- ##### 创建项目和apps

  ```python
  django-admin startproject cms
  python manage.py startapp apps
  ```

- ##### 启动django

  ```python
  python manage.py runserver 0.0.0.0:8000
  ```

- ##### 数据库迁移

  在项目目录下执行（和 manage.py 文件同级）

  ```python
  python manage.py makemigrations
  python manage.py migrate
  ```

- #####  apidoc生成接口文档

  在 apidoc.json 同级下执行

  ```python
  apidoc -i ../cms/apps -o ../cms/static/apidoc
  ```

- ##### 利用mysql数据库来缓存，需要创建相应的表

  ```python
  python manage.py createcachetable
  ```

