### 相关使用

* 创建管理员账号
```
python3 manage.py createsuperuser 
```

* 注册站点
```
from .models import Book
admin.site.register(Book)
```