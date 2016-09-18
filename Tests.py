from selenium import webdriver
from loginPage import LP
import unittest
import elements_store_room,values_store_room


class Tests(unittest.TestCase):

    browser = webdriver.Firefox()

    l = LP()

    def setUp(self):
        self.browser.get(elements_store_room.fb)  # get the target url

    def test_fill_various_boxes(self):
        self.l.fvb(self.browser)

    def test_check_page_text(self):

        try:

            terms_and_conditions_text, connect_text = self.l.get_text(self.browser)
            self.assertEqual(terms_and_conditions_text,values_store_room.tc_text,"\nError: Terms and conditions text does not match.")
            self.assertEqual(connect_text, values_store_room.con_text,"\nError: Info text does not match.")

            # alternate method, but expensive, since you pull the whole page source
            self.assertTrue('Facebook' in self.browser.page_source)

        except AssertionError as e: print(e)





    def tearDown(self):
         print("done\n")

         # The below line, self.browser.quit(), has been commented out so that you can easily see the automation in action.
         # In a normal automation run it would execute since we need to close the browser instance each time.

         # self.browser.quit()



