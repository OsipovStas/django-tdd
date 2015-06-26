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


	def test_that_home_page_can_save_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['movie_name'] = "A new movie title"

		response = home_page(request)

		expected = render_to_string(
			'home.html',
			{'new_movie_name': "A new movie title"})
		self.assertEqual(response.content.decode(), expected)


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




		

