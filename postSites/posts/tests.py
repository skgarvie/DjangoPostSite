import datetime

from django.test import TestCase
from django.utils import timezone

from posts.models import Post
# Create your tests here.
class PostMethodTests(TestCase):
	def test_was_published_recently_with_old_post(self):
		old_post = Post(pub_date=timezone.now() - datetime.timedelta(days=30))
		self.assertEqual(old_post.was_published_recently(), False)

	def test_was_published_recently_with_recent_post(self):
		recent_post = Post(pub_date=timezone.now() - datetime.timedelta(hours=1))
		self.assertEqual(recent_post.was_published_recently(), True)

	def test_was_published_recently_with_future_post(self):
		future_post = Post(pub_date=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_post.was_published_recently(), False)
