# Django
from django.contrib import admin

# Models
from app.models import Film

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
