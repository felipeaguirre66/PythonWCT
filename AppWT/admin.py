from django.contrib import admin
from .models import Posts, thumbnail
from Acceso.models import Avatar
# Register your models here.

admin.site.register(Posts)
admin.site.register(Avatar)
admin.site.register(thumbnail)
