### 请求处理相关
* 使用@require_http_methods装饰器限定请求method类型
```
from django.shortcuts import render,HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(['POST','GET'])
def index(request):
    return HttpResponse("123")
```

* Django中CSRF中间件的工作原理及form表单提交需要添加{% csrf_token %} 
```
django.middleware.csrf.CsrfViewMiddleware
```

### cookie和seesion

* cookie浏览器存储
```
request  -> Cookie: csrftoken=2spaotqXpzI7T5QdpXXAHRnMomgquF9O0p7l8V7BJhAXlbYUD65kGAaK67o6NtIB; name=fei
response -> Set-Cookie: name=fei; Path=/
```

* session:利用django_session存储
```
@require_http_methods(['GET'])
def index(request):
    name = request.session['name']
    password = request.session['password']
    return HttpResponse("{0},{1} login success".format(name,password))


def login(request):
    if request.method == 'GET':
        return render(request, template_name='login.html')
    else:
        name = request.POST['name']
        password = request.POST['password']
        if name == "fei" and password == "123":
            response = HttpResponse("hello {0}".format(name))
            request.session['name'] = name
            request.session['password'] = password
            return redirect("/index")
        else:
            return redirect(reverse(viewname='login'))
```
在 Django 中，该数据被存到数据库的 django_session 数据表中。
```
django_session | CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
```

### 自定义错误

```
def page_not_found(request):
    return render(request, '404.html')

def page_error(request):
    return render(request, '500.html')

def permission_denied(request):
    return render(request, '403.html')

# 定义错误跳转页面urls.py
handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error
```

注：若是DEBUG=True，有些情况下则不会生效

### 相关链接

* request-response:https://docs.djangoproject.com/en/3.1/ref/request-response/