# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.db.models import Q

from ..models import Category, Document


register = template.Library()


@register.assignment_tag
def get_latest_documents(count=5, category=None):
    """ Accepts category or category slug. """

    document_list = Document.objects.published()

    # Optional filter by category, can be either a sub or parent category
    if category is not None:
        if not isinstance(category, Category):
            category = Category.objects.get(slug=category)

        query = Q(pk=category.pk) | Q(parent_category=category)
        categories = Category.objects.filter(query)
        document_list = document_list.filter(category__in=categories)

    return document_list[:count]
