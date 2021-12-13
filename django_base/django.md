# Django

#### 创建项目基本
1. Django开始一个新项目 ：django-admin startproject mysite
2. 开启Web服务：python manage.py runserver [8080]
3. 创建应用：python manage.py startapp appName
4. Django 版本：python -m django --version

## 数据库相关（模型即表的结构，更复杂一些即为数据库中数据的关系网）
	改变模型需要这三步：
		编辑 models.py 文件，改变模型。
		运行 python manage.py makemigrations 为模型的改变生成迁移文件。
		运行 python manage.py migrate 来应用数据库迁移。



### 问题：
	1. django pymysql Unable to create the django_migrations table ((1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(6) NOT NULL)' at line 1"))
	原因： django-2.1 不支持 mysql-5.5版本

