# -*- coding: utf-8 -*-

from .models import Document, Category


class DocumentDetailMixin(object):
    model = Document

    def get_context_data(self, **kwargs):
        context = super(DocumentDetailMixin, self).get_context_data(**kwargs)
        context['documents_categories'] = True
        context['categories'] = Category.objects.all()
        return context


class DocumentListMixin(DocumentDetailMixin):
    def get_queryset(self):
        return self.model.objects.filter(published=True).exclude(current_version=None)

