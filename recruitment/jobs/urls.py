from django.conf.urls import url
from django.urls import path
from django.conf import settings

from recruitment.jobs import views

# 定义urlpatterns变量
urlpatterns = [
    # 职位列表 用正则表达式匹配 url 路径
    url(r"joblist/", views.joblist, name="joblist")
]
