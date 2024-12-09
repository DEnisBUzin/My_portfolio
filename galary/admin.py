from django.contrib import admin

from galary.models import Project


@admin.register(Project)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'title',
                    'date_create',
                    'date_update',
                    'slug',
                    'link_of_git']
    list_filter = ['date_create']
    prepopulated_fields = {'slug': ('name',)}