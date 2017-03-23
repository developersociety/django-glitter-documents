# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import apps
from django.conf import settings
from django.contrib import admin

from glitter import block_admin
from glitter.admin import GlitterAdminMixin

from .models import Category, Document, Format, LatestDocumentsBlock


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
class DocumentAdmin(GlitterAdminMixin, admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('title', 'category', 'document_format', 'file_size', 'is_published')
    list_filter = ('category',)
    prepopulated_fields = {
        'slug': ('title',)
    }

    def get_inline_instances(self, request, obj=None):
        if apps.is_installed('glitter.reminders'):
            # Import here to prevent migrations on the glitter level.
            from glitter.reminders.admin import ReminderInline
            if ReminderInline not in self.inlines:
                self.inlines.append(ReminderInline)
        return super(DocumentAdmin, self).get_inline_instances(request, obj)

    def get_fieldsets(self, request, obj=None):
        advanced_options = ['tags', 'slug']
        if not getattr(settings, 'GLITTER_DOCUMENTS_TAGS', False):
            advanced_options.remove('tags')

        fieldsets = (
            ('Document', {
                'fields': (
                    'title', 'category', 'author', 'document', 'document_format', 'summary',
                )
            }),
            ('Advanced options', {
                'fields': advanced_options
            }),
        )
        return fieldsets


block_admin.site.register(LatestDocumentsBlock)
block_admin.site.register_block(LatestDocumentsBlock, 'App Blocks')
