from django.urls import reverse
import tempfile
from django.test import TestCase
from studentWorksPlatform import factories, models
from django.core.files import File
from PIL import Image
import os



# Create your tests here.
class StudentUsersPlatformTestCase(TestCase):

    def setUp(self):
        self.user = factories.UserFactory()

    def test_get_user_list(self):
        url = reverse('user_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['users'].count(), models.User.objects.count())




class StudentWorksPlatformTestCase(TestCase):

    def setUp(self):
        self.work = factories.WorkFactory()

    def test_get_work_list(self):
        url = reverse('work_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['works'].count(), models.Work.objects.count())

    def test_get_work_detail(self):
        url = reverse('work_detail', kwargs={'pk': self.work.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_work(self):
        url = reverse('work_edit', kwargs={'pk': self.work.pk})
        old_title = self.work.title
        old_description = self.work.description

        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp_file:
            temp_file.write(b'TMP')
            temp_file.seek(0)
            test_file_path = temp_file.name

        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_image:
            img = Image.new('RGB', (100, 100), color='red')
            img.save(temp_image.name)
            test_image_path = temp_image.name

        with open(test_file_path, 'rb') as test_file:
            with open(test_image_path, 'rb') as test_image:
                response = self.client.post(url, {
                    'title': 'new_title',
                    'description': 'new_description',
                    'subject': self.work.subject.id,
                    'file': test_file,
                    'image': test_image,
                    'price': self.work.price,
                    'author': self.work.author.id,
                    'status': self.work.status,
                    'is_unique': self.work.is_unique,
                })

        self.work.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.work.title, 'new_title')
        self.assertNotEqual(self.work.description, old_description)

        os.remove(test_file_path)
        os.remove(test_image_path)


    def test_delete_work(self):
        url = reverse('work_delete', kwargs={'pk': self.work.pk})
        old_work_count = models.Work.objects.count()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertGreater(old_work_count, models.Work.objects.count())
        print(old_work_count, models.Work.objects.count())

    def test_create_work(self):
        url = reverse('add_work')
        old_work_count = models.Work.objects.count()
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp_file:
            temp_file.write(b'TMP')
            temp_file.seek(0)
            test_file_path = temp_file.name

        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_image:
            img = Image.new('RGB', (100, 100), color='red')
            img.save(temp_image.name)
            test_image_path = temp_image.name

        with open(test_file_path, 'rb') as test_file:
            with open(test_image_path, 'rb') as test_image:
                response = self.client.post(url, {
                    'title': 'TMP',
                    'description': 'TMP',
                    'subject': self.work.subject.id,
                    'file': test_file,
                    'image': test_image,
                    'price': 1000,
                    'author': self.work.author.id,
                    'status': '1',
                    'is_unique': False,
                })

        self.assertEqual(response.status_code, 302)

        self.assertGreater(models.Work.objects.count(), old_work_count)
        new_work = models.Work.objects.first()
        self.assertEqual(new_work.title, 'TMP')
        self.assertEqual(new_work.description, 'TMP')

        print(old_work_count, models.Work.objects.count())

        os.remove(test_file_path)
        os.remove(test_image_path)