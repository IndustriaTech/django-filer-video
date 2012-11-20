from django.contrib import admin
from filer.admin.fileadmin import FileAdmin

from .models import Video

admin.site.register(Video, FileAdmin)  # use the standard FileAdmin
