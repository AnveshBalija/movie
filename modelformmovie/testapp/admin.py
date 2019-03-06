from django.contrib import admin
from testapp.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['redate','moviename','hero','heroine','rating']
admin.site.register(Movie,MovieAdmin)
