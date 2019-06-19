from django.contrib import admin
from .models import *

# Admin interface just for debug and usability

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'descr')

class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)
admin.site.register(Tag, TagAdmin)