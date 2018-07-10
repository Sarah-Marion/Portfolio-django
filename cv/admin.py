from django.contrib import admin
from .models import Project, Cv, Technique, Info

# Register your models here.
admin.site.register(Project)
admin.site.register(Cv)
admin.site.register(Technique)
admin.site.register(Info)