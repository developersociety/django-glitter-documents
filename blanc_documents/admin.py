# -*- coding: utf-8 -*-

from django.contrib import admin

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
