from django.contrib import admin
from .models import Serie,Capitulo,Pelicula
# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Serie)
admin.site.register(Capitulo)