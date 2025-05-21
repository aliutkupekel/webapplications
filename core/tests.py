from django.test import TestCase
from core.models import Post
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class PostModelTest(TestCase):
    def test_create_post(self):
        post = Post.objects.create(
            title="Test title",
            content="this is a test content."
        )
        self.assertEqual(post.title, "Test title")
        self.assertEqual(post.content, "this is a test content.")
        self.assertIsNotNone(post.created_at)

class PostAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='utku', password='123456')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_post_via_api(self):
        data = {
            'title': 'API Test Post',
            'content': 'content that created by API'
        }
        response = self.client.post('/api/posts/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'API Test Post')

    def test_get_posts(self):
        Post.objects.create(title='VISIBLE Post', content='Content')
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)
