from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

# This page contains all the methods that are being used in every page within the project
# and are not specific to a single page
# All the pages will inherit this page.

class BasePage(Browser, unittest.TestCase):

    def wait_for_elem(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))


