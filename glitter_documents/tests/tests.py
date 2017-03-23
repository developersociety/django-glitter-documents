from django.test import TestCase

from django.contrib.admin.sites import AdminSite
from django.test import modify_settings
from django.test.client import RequestFactory

from glitter.reminders.admin import ReminderInline
from glitter_documents.admin import DocumentAdmin
from glitter_documents.models import Document


class MockSuperUser(object):
    def has_perm(self, perm):
        return True

    def has_module_perms(self, module):
        return True

    def is_active(self):
        return True

    def is_staff(self):
        return True


class DocumentAdminTestCase(TestCase):
    def setUp(self):
        self.request = RequestFactory().request()
        self.request.user = MockSuperUser()

    @modify_settings(INSTALLED_APPS={
        'remove': 'glitter.reminders',
    })
    def test_the_inline_not_appears(self):
        """ Test to make sure inline is not set if the settings variable is not set. """
        DocumentAdmin.inlines = []
        document_admin = DocumentAdmin(model=Document, admin_site=AdminSite())
        document_admin.get_inline_instances(self.request)
        self.assertNotIn(ReminderInline, document_admin.inlines)

    @modify_settings(INSTALLED_APPS={
        'append': 'glitter.reminders',
    })
    def test_the_inline_appears(self):
        """ Test to make sure inline is not set if the settings variable is not set. """
        DocumentAdmin.inlines = []
        document_admin = DocumentAdmin(model=Document, admin_site=AdminSite())
        document_admin.get_inline_instances(self.request)
        self.assertIn(ReminderInline, document_admin.inlines)
