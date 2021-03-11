### 基础配置

在 Django 项目中用于管理路由的叫做 URLConf 模块，在 myweb/settings.py 文件中 ROOT_URLCONF 字段用来设置它：
```
ROOT_URLCONF = 'myweb.urls'
```

### 从URL中提取数据

* 支持的converter如下:
```
1.str,匹配除了路径分隔符（/）之外的非空字符串，这是默认的形式
2.int,匹配正整数，包含0。
3.slug,匹配字母、数字以及横杠、下划线组成的字符串。
4.uuid,匹配格式化的uuid，如 075194d3-6885-417e-a8a8-6c931e272f00。
5.path,匹配任何非空字符串，包含了路径分隔符。
```

### 路由匹配

路由匹配支持精确匹配和正则匹配，同时支持动态参数匹配

```
from django.urls import path,re_path
from myApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('index1/<slug:name>/<int:age>',index1), 动态参数
    re_path(r'^test.*/$',index) 正则匹配
    正则表达式的开始使用“^”表示。
    正则表达式的结束使用“$”表示
]
```

### 路由转发

不同于Flask的蓝图，在 Django 中实际上做得更彻底，就是将项目中各个功能分类，创建不同的应用以实现它们。
现在我们的 myweb 项目中只有 learn 应用，后面可能会有 user 、admin 、auth 等各种应用。就路由管理而言，把每个应用提供的视图函数都写到 myweb/urls.py 文件中，肯定是混乱的。
如何做到 Flask Blueprint 那样分门别类呢？答案就是在每个应用中创建一个 urls.py 文件。

```
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('index/', index),
    path('index1/<slug:name>/<int:age>', index1),
    re_path(r'^test.*$', index)
]
```

```
from django.contrib import admin
from django.urls import path, re_path, include
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myApp.urls'))
]
```
