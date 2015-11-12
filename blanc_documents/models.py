# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

from blanc_pages.mixins import GlitterMixin


@python_2_unicode_compatible
class Format(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blanc-documents:category-list', args=(self.slug,))


@python_2_unicode_compatible
class Document(GlitterMixin):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category)
    document = models.FileField(max_length=200, upload_to='documents/document/%Y/%m')
    author = models.CharField(blank=True, max_length=32)
    file_size = models.PositiveIntegerField(default=0, editable=False)
    document_format = models.ForeignKey(Format)
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(GlitterMixin.Meta):
        get_latest_by = 'created_at'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blanc-documents:detail', args=(self.slug,))

    def save(self, *args, **kwargs):
        # Avoid doing file size requests constantly
        self.file_size = self.document.size

        super(Document, self).save(*args, **kwargs)
