from django.test import TestCase, Client

from blog.models import Post


class CRUDTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_show_index(self):
        assert self.client.get('/blog/').status_code == 200

    def test_delete(self):
        Post.objects.create(title='title1', text='text1', image='/image.jpg')
        self.client.get('/blog/delete/1/')
        assert Post.objects.count() == 0

    def test_add_post(self):
        response = self.client.post(
            '/blog/create/',
            data={
                "title": "title_test",
                "text": "text ad;fkasd;fkj",
                "image": "/home/image.jpg"
            }
        )
        assert response.status_code == 302
        assert Post.objects.all().exists()
