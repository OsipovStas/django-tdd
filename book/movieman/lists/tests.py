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
		expected = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected)

		

