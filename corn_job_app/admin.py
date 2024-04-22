from django.contrib import admin
from .models import *

# Register your models here.


class WidgetAdmin(admin.ModelAdmin):
    list_display = ['id','name','font_size']
admin.site.register(Widget, WidgetAdmin)