# -*- coding: utf-8 -*-

from django.contrib import admin
from django.core.urlresolvers import reverse

from blanc_pages.admin import BlancPageAdminMixin

from .models import Format, Category, Document


@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Document)
class DocumentAdmin(BlancPageAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('Document', {
            'fields': (
                'title', 'category', 'author', 'document', 'document_format', 'summary',
            )
        }),
        ('Advanced options', {
            'fields': ('slug',)
        }),
    )
    date_hierarchy = 'created_at'
    list_display = ('title', 'category', 'document_format', 'file_size',)
    list_filter = ('category__title',)
    prepopulated_fields = {
        'slug': ('title',)
    }

    def admin_url(self, obj):
        info = self.model._meta.app_label, self.model._meta.model_name
        redirect_url = reverse('admin:%s_%s_redirect' % info, kwargs={'object_id': obj.id})
        return '<a href="%s">%s</a>' % (redirect_url, 'URL')
    admin_url.short_description = 'URL'
    admin_url.allow_tags = True
