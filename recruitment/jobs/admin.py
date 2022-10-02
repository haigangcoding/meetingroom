from django.contrib import admin
from jobs.models import Job
# Register your models here.

# 引入管理类的参数
class JobAdmin(admin.ModelAdmin):
    # 隐藏创建人 创建时间

    # 列表展示的参数
    list_display = ('job_name', 'job_type', 'job_city', 'created_date', 'modified_date')
    pass


admin.site.register(Job)
