from __future__ import unicode_literals

from waffle.models import Flag, Switch
from waffle.tests.base import TestCase


class MixinsTests(TestCase):
    def test_flag_must_be_active(self):
        resp = self.client.get('/cbv/flag-on')
        self.assertEqual(404, resp.status_code)
        Flag.objects.create(name='foo', everyone=True)
        resp = self.client.get('/cbv/flag-on')
        self.assertEqual(200, resp.status_code)

    def test_flag_must_be_inactive(self):
        resp = self.client.get('/cbv/flag-off')
        self.assertEqual(200, resp.status_code)
        Flag.objects.create(name='foo', everyone=True)
        resp = self.client.get('/cbv/flag-off')
        self.assertEqual(404, resp.status_code)

    def test_switch_must_be_active(self):
        resp = self.client.get('/cbv/switch-on')
        self.assertEqual(404, resp.status_code)
        Switch.objects.create(name='foo', active=True)
        resp = self.client.get('/cbv/switch-on')
        self.assertEqual(200, resp.status_code)

    def test_switch_must_be_inactive(self):
        resp = self.client.get('/cbv/switch-off')
        self.assertEqual(200, resp.status_code)
        Switch.objects.create(name='foo', active=True)
        resp = self.client.get('/cbv/switch-off')
        self.assertEqual(404, resp.status_code)

    def test_switch_must_be_inactive_and_redirect_to_named_view(self):
        resp = self.client.get('/cbv/switched_view_with_valid_url_name')
        self.assertEqual(302, resp.status_code)
        Switch.objects.create(name='foo', active=True)
        resp = self.client.get('/cbv/switched_view_with_valid_url_name')
        self.assertEqual(200, resp.status_code)

    def test_switch_must_be_inactive_and_redirect_to_named_view_with_args(self):
        resp = self.client.get(
            '/cbv/switched_view_with_args_with_valid_url_name/1/')
        self.assertRedirects(resp, '/foo_view_with_args/1/')
        Switch.objects.create(name='foo', active=True)
        resp = self.client.get(
            '/cbv/switched_view_with_args_with_valid_url_name/1/')
        self.assertEqual(200, resp.status_code)

    def test_switch_must_be_inactive_and_not_redirect(self):
        resp = self.client.get('/cbv/switched_view_with_invalid_redirect')
        self.assertEqual(404, resp.status_code)
        Switch.objects.create(name='foo', active=True)
        resp = self.client.get('/cbv/switched_view_with_invalid_redirect')
        self.assertEqual(200, resp.status_code)

    def test_flag_must_be_inactive_and_redirect_to_named_view(self):
        resp = self.client.get('/cbv/flagged_view_with_valid_url_name')
        self.assertEqual(302, resp.status_code)
        Flag.objects.create(name='foo', everyone=True)
        resp = self.client.get('/cbv/flagged_view_with_valid_url_name')
        self.assertEqual(200, resp.status_code)

    def test_flag_must_be_inactive_and_redirect_to_named_view_with_args(self):
        resp = self.client.get(
            '/cbv/flagged_view_with_args_with_valid_url_name/1/')
        self.assertRedirects(resp, '/foo_view_with_args/1/')
        Flag.objects.create(name='foo', everyone=True)
        resp = self.client.get(
            '/cbv/flagged_view_with_args_with_valid_url_name/1/')
        self.assertEqual(200, resp.status_code)

    def test_flag_must_be_inactive_and_not_redirect(self):
        resp = self.client.get('/cbv/flagged_view_with_invalid_redirect')
        self.assertEqual(404, resp.status_code)
        Flag.objects.create(name='foo', everyone=True)
        resp = self.client.get('/cbv/flagged_view_with_invalid_redirect')
        self.assertEqual(200, resp.status_code)
