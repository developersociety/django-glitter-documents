# -*- coding: utf-8 -*-

from .models import Document, Category


def _sort_key(category):
    return category.title


class DocumentMixin(object):
    model = Document

    def get_context_data(self, **kwargs):
        context = super(DocumentMixin, self).get_context_data(**kwargs)
        context['documents_categories'] = True
        categories = Category.objects.filter(parent_category__isnull=True)
        context['categories'] = categories
        return context
