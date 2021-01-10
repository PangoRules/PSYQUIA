from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.

admin.site.site_header='PSYCHIA'
admin.site.site_title='PSYCHIA'
admin.site.index_title="PSYCHIA - Panel de Administración"
admin.site.unregister(Group)