# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from recruitment.jobs.models import Job
from recruitment.jobs.models import Cities, JobTypes

# Django 视图 有几种方法： 可以用函数去定义，可以用视图的类去定义
# 用函数去定义在 views 层里面

def joblist(request):
    job_list = Job.objects.order_by('job_type')
    # 加载模板 等于用 loader 模板的加载器来加载 get_template('joblist.html')
    template = loader.get_template('joblist.html')
    # 定义上下文
    context = {'job_list': job_list}

    # 遍历职位列表
    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.job_type = JobTypes[job.job_type][1]

    return HttpResponse(template.render(context))