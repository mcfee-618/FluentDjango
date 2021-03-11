from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('index/', index),
    path('index1/<slug:name>/<int:age>', index1),
    re_path(r'^test.*$', index)
]