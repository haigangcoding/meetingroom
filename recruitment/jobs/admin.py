from django.contrib import admin
from jobs.models import Job
# Register your models here.

# 引入管理类的参数
class JobAdmin(admin.ModelAdmin):
    # 隐藏创建人 创建时间 修改时间
    exclude = ('creator', 'created_date', 'modified_date')
    # 列表展示的参数
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date')
    # 利益 ModelAdmin 这个父类里面定义的方法
    def save_model(self, request, obj, form, change):

        # 把职位的创建人设置为当前的用户, 就可以把当前登录的用户设置成这个 Model 的创建人
        obj.creator = request.user
        # 调用 父类的方法来保存我们的对象
        super().save_model(request, obj, form, change)



admin.site.register(Job, JobAdmin)
