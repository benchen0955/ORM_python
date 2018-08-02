# ORM_python
數據庫進階-對像關係映射（ORM）的使用

pip install flask-sqlalchemy
pip install PyMySQL
from flask.ext.salalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:SQLac931014@localhost/test' #+pymysql


 in python
db 連線
db.create_all() 建立資料庫

u = User("name","password")
u.add()
e = Entry("message","name")
e.add()
l = getAllEntry()
for each in l :
    print each.content

主程式import mdoel 有問題所以將model code 搬到主程式

pip freeze 查套件
asn1crypto==0.24.0
astroid==1.6.3
certifi==2018.1.18
cffi==1.11.5
chardet==3.0.4
click==6.7
colorama==0.3.9
comtypes==1.1.4
cryptography==2.2.2
et-xmlfile==1.0.1
Flask==1.0.2
Flask-SQLAlchemy==2.3.2
Flask-WTF==0.14.2
idna==2.6
isort==4.3.4
itsdangerous==0.24
jdcal==1.4
Jinja2==2.10
lazy-object-proxy==1.3.1
MarkupSafe==1.0
mccabe==0.6.1
mysql-connector-python==8.0.11
mysqlclient==1.3.12
openpyxl==2.5.3
protobuf==3.5.2.post1
pycparser==2.18
pylint==1.8.4
PyMySQL==0.9.0
PyPDF2==1.26.0
requests==2.18.4
six==1.11.0
SQLAlchemy==1.2.9
urllib3==1.22
Werkzeug==0.14.1
wrapt==1.10.11
WTForms==2.1
xlwings==0.11.7
