__author__ = 'mushahidalam'

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys

import unittest, time, re

class Sel(unittest.TestCase):
    def setUp(self):
        chromedriver = "/usr/local/opt/chromedriver/bin/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.rottentomatoes.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_sel(self):
        driver = self.driver
        delay = 3
        driver.get(self.base_url + "/browse/dvd-all/?services=amazon;amazon_prime;flixster;hbo_go;itunes;netflix_iw;vudu&genres=1")
        #driver.find_element_by_link_text("All").click()
        for i in range(1,191):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element_by_class_name("mb-load-btn").click()
            time.sleep(4)
        html_source = driver.page_source
        filename = 'rottantomato_more'+'.html'
        data = html_source.encode('utf-8')
        with open(filename, 'wb') as f:
            f.write(data)


if __name__ == "__main__":
    unittest.main()