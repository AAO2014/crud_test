from django.test import TestCase, Client

from blog.models import Post


class CRUDTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_post(self):
        response = self.client.post(
            'blog/',
            data={
                "title":"title_test",
                "text": "text ad;fkasd;fkj",
                "image": "/home/image.jpg"
            }
        )
        assert Post.objects.first()