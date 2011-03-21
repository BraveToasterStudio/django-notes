from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client

from django_notes.models import Note


class SimpleTests(TestCase):
    def setUp(self):
        # Add a test user
        self.test_user = User.objects.create_user('test', 'test@example.com', 'secret')

        self.client.login(username='test', password='secret')
        self.unauthed_client = Client()

    def test_login_required(self):
        response = self.unauthed_client.get(reverse('django_notes.views.list'))
        self.assertEqual(response.status_code, 302)

        response = self.unauthed_client.get(reverse('django_notes.views.create'))
        self.assertEqual(response.status_code, 302)
        
        response = self.unauthed_client.get(reverse('django_notes.views.update', args=[1]))
        self.assertEqual(response.status_code, 302)
        
        response = self.unauthed_client.get(reverse('django_notes.views.delete', args=[1]))
        self.assertEqual(response.status_code, 302)

        response = self.unauthed_client.get(reverse('django_notes.views.details', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_create_note(self):
        response = self.client.get(reverse('django_notes.views.create'))
        self.assertEqual(response.status_code, 200)

        resp = self.client.post(
            reverse('django_notes.views.create'), {'title':'Test Note', 'content':'Foo'},
            follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Note.objects.get(title='Test Note'))

    def test_list_notes(self):
        resp = self.client.get(reverse('django_notes.views.list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_note(self):
        note_id = Note.objects.all()[0].pk
        resp = self.client.get(reverse('django_notes.views.details', args=[note_id]))
        self.assertEqual(resp.status_code, 200)

    def test_update_note(self):
        note_id = Note.objects.all()[0].pk
        response = self.client.get(reverse('django_notes.views.update', args=[note_id]))
        self.assertEqual(response.status_code, 200)

        resp = self.client.post(
            reverse('django_notes.views.update', args=[note_id]),
            {'title':'Another Test Note', 'content':'Foo'}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Note.objects.get(title='Another Test Note'))

    def test_delete_note(self):
        note_id = Note.objects.all()[0].pk
        note_title = Note.objects.all()[0].title
        response = self.client.get(reverse('django_notes.views.delete', args=[note_id]))
        self.assertEqual(response.status_code, 200)

        resp = self.client.post(
            reverse('django_notes.views.delete', args=[note_id]), follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Note.objects.filter(title=note_title).count(), 0)

    def test_delete_multiple(self):
        notes_count = Note.objects.count()
        notes_pks  = Note.objects.values_list('pk', flat=True)
        post_data = {
            'action': 'delete',
            'form-TOTAL_FORMS': notes_count,
            'form-INITIAL_FORMS': notes_count,
            'form-MAX_NUM_FORMS': '',
            }
        for i, pk in enumerate(notes_pks):
            post_data.update({
                    'form-%s-id' % i: pk,
                    'form-%s-is_checked' % i: 'on'})

        resp = self.client.post(
            reverse('django_notes.views.list'), post_data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Note.objects.count(), 0)
