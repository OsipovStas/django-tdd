from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	
	def tearDown(self):
		self.browser.quit()

	def test_that_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')
		
		self.assertIn('To See', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Your Watch list', header_text)

		#Now it's possible to enter movie to see
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), "Enter a movie name")
		
		#User types Watchmen into text box
		inputbox.send_keys('Watchmen')
		#Hit the enter
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('movie_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Watchmen' for row in rows),
			"New must-see movie did not appear in table")



		self.fail('Fail!')

if __name__ == '__main__':
	unittest.main(warnings = 'ignore')




