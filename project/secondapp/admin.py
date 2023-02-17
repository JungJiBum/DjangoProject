from django.contrib import admin
from .models import customer

# Register your models here.


class customerAdmin(admin.ModelAdmin):  # admin의 ModelAdmin 클래스 상속
    # pass # 상속만 받아 새로운 클래스를 생성
    list_display = ('username', 'password', 'useremail')


admin.site.register(customer, customerAdmin)  # admin 페이지에 등록
