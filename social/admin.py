from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', 'created')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ('updated', 'created', 'key', 'name')
        else:
            return ('updated', 'created')


# Register your models here.
admin.site.register(Link, LinkAdmin)
