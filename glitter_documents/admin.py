# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

    def render_change_form(self, request, context, *args, **kwargs):
        if 'original' in context and context['original']:
            qs = context['adminform'].form.fields['parent_category'].queryset
            # To restrict to a simple 2 level dependencies we do the following:
            # - If this category is a parent, it can't have a parent, so no
            #   entries are listed.
            if context['original'].category_set.all().exists():
                qs = context['original'].__class__.objects.none()
            else:
                # - Exclude itself, you can't be your own parent.
                qs = qs.exclude(pk=context['original'].pk)
                # - Categories that have a parent can't be a parent, so filter
                #   out these categories.
                qs = qs.filter(parent_category__isnull=True)
            
            context['adminform'].form.fields['parent_category'].queryset = qs

        returns = super().render_change_form(request, context, *args, **kwargs)
        return returns


@admin.register(Document)
class DocumentAdmin(GlitterAdminMixin, admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('title', 'category', 'document_format', 'file_size', 'is_published')
    list_filter = ('category',)
    prepopulated_fields = {
        'slug': ('title',)
    }

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
