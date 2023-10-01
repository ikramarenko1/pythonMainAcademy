# admin test1337

from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('createdate',)  # Поля, которые можно только "читать"


admin.site.register(Todo, TodoAdmin)
