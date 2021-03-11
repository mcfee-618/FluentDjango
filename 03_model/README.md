### docker 环境安装
```
docker run --name mysql5.7 -p 3306:3306 -v /usr/local/mysql/data:/var/lib/mysql -v /usr/local/mysql/conf.d:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=rootroot -d mysql:5.7.23
mysql -uroot -h0.0.0.0 -p --skip-ssl
```

### model层相关api

* Field
```
class Book(models.Model):
    name = models.CharField(max_length=400,null=False,primary_key=True)
    author = models.CharField(max_length=100)
    pub_house = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
```

* Model相关操作

1.save:要将对象保存回数据库，调用 save()，支持插入和更新

```
save:The keyword arguments are the names of the fields you’ve defined on your model. Note that instantiating a model in no way touches your database; for that, you need to save().
>>> b3 = Blog(id=3, name='Cheddar Talk', tagline='Thoughts on cheese.')
>>> b3.id     # Returns 3.
>>> b3.save()
>>> b3.id     # Returns 3. 自增id
```
2.save如何区分插入和更新?

```
如果对象的主键属性被设置为值为 True （即，一个不是 None 或空字符串的值），Django 会执行 UPDATE。
如果对象的主键属性没有设置，或者 UPDATE 没有更新任何东西（例如主键被设置为数据库中不存在的值），Django 会执行 INSERT。
```

3.delete:删除对象
```
Model.delete(using=DEFAULT_DB_ALIAS, keep_parents=False)
```
4.查询对象集：filter、all

```
>>> all_entries = Entry.objects.all() # The all() method returns a QuerySet of all the objects in the database.
filter(**kwargs)：返回一个新的 QuerySet，包含的对象满足给定查询参数，每次精炼一个QuerySet，你就会获得一个全新的QuerySet。
>>> Entry.objects.filter(
...     headline__startswith='What'
... ).exclude(
...     pub_date__gte=datetime.date.today()
... ).filter(
...     pub_date__gte=datetime.date(2005, 1, 30)
... )
```
QuerySet 是惰性的 —— 创建 QuerySet 并不会引发任何数据库活动。你可以将一整天的过滤器都堆积在一起，Django 只会在 QuerySet 被 计算 时执行查询操作。

```
>>> Entry.objects.filter(id__gt=4)
>>> Book.objects.filter(name__contains='2')
```


5.查询单个对象：get方法

```
Book.objects.get(name__contains='2')
```
如果 get() 没有找到任何对象，它会引发一个 Model.DoesNotExist 异常：
Entry.objects.get(id=-999) # raises Entry.DoesNotExist
如果 get() 发现多个对象，会引发一个 Model.MultipleObjectsReturned 异常：

### 相关链接

* 查询相关：https://docs.djangoproject.com/zh-hans/3.1/ref/models/querysets/#lt