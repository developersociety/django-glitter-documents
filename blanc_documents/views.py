# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from blanc_pages.mixins import BlancPageDetailMixin

from .mixins import DocumentListMixin, DocumentDetailMixin
from .models import Category


class DocumentListView(DocumentListMixin, ListView):
    paginate_by = 10


class DocumentDetailView(DocumentDetailMixin, BlancPageDetailMixin, DetailView):
    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        context['current_category'] = self.object.category
        return context


class CategoryDocumentListView(DocumentListMixin, ListView):
    template_name_suffix = '_category_list'
    paginate_by = 10

    def get_queryset(self):
        qs = super(CategoryDocumentListView, self).get_queryset()
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return qs.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryDocumentListView, self).get_context_data(**kwargs)
        context['current_category'] = self.category
        context['categories'] = Category.objects.all()
        return context



