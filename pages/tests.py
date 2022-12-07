from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.
class PostModelTest(TestCase):
    # we create dummy object
    def setUp(self):
        Post.objects.create(text='Test string')
    # test content of dummy object
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'Test string')


class HomePageViewTest(TestCase): # new
    def setUp(self):
        Post.objects.create(text='this is another test')
    # testing if index page is exists at correct location
    def test_url_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    # test url by name
    def test_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    # test if view is using the correct template
    def test_view_template_correctness(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
