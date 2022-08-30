from django.contrib import admin
from .models import Project, Credit, Asset
from adminsortable2.admin import SortableInlineAdminMixin,SortableAdminBase


class CreditAdmin(SortableInlineAdminMixin, admin.StackedInline):
    list_display = ('role','name')
    model = Credit

class AssetAdmin(SortableInlineAdminMixin, admin.StackedInline):
     list_display = ('caption','image')
     model = Asset


class ProjectAdmin(SortableAdminBase,admin.ModelAdmin):
    list_display = ('title','url')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        CreditAdmin,
        AssetAdmin
    ]



# Register your models here.
admin.site.register(Project, ProjectAdmin)
