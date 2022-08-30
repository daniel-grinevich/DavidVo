from django.contrib import admin
from .models import Page
from adminsortable2.admin import SortableAdminMixin


class PageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title','navigation_title', 'is_in_navigation')
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Page, PageAdmin)
