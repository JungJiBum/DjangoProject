from django.contrib import admin
from .models import webtoonData

# Register your models here.


class crawAdmin(admin.ModelAdmin):  # admin의 ModelAdmin 클래스 상속
    list_display = ('title', 'week')


admin.site.register(webtoonData, crawAdmin)
