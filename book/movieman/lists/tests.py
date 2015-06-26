from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


class HomePageTest(TestCase):

	def test_that_root_url_resolves_to_home_page(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_that_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertIn("Your Watch list", response.content.decode())

	def test_that_home_page_only_saves_movies_when_necessary(self):
		request = HttpRequest()
		home_page(request)
		self.assertEqual(Item.objects.count(), 0)

	def test_that_home_page_can_save_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['movie_name'] = "A new movie title"

		response = home_page(request)

		self.assertEqual(Item.objects.count(), 1)
		new_movie = Item.objects.first()
		self.assertEqual(new_movie.text, "A new movie title")

	def test_that_home_page_redirects_after_POST(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['movie_name'] = "A new movie title"

		response = home_page(request)

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_that_home_page_displays_all_movies(self):
   		Item.objects.create(text = "Movie 1")
   		Item.objects.create(text = "Movie 2")

   		request = HttpRequest()
   		response = home_page(request)
   		self.assertIn("Movie 1", response.content.decode())
   		self.assertIn("Movie 2", response.content.decode())

from lists.models import Item

class ItemModelTest(TestCase):

	def test_that_saving_and_retrieving_items_working(self):
		first = Item()
		first.text = 'The first ever item'
		first.save()

		second = Item()
		second.text = "Second item"
		second.save()

		saved = Item.objects.all()
		self.assertEqual(saved.count(), 2)

		first_saved = saved[0]
		second_saved = saved[1]
		self.assertEqual(first_saved.text, 'The first ever item')
		self.assertEqual(second_saved.text, "Second item")




		

