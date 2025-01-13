from django.contrib import admin
from .models import Page

# Register your models here.
admin.site.register(Page)

# Configuración del panel
title = "Blog Django"
subtitle = "Panel de gestión"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle