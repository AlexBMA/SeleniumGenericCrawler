
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from genericContinus.ScreenshotPage import ScreenshotPage

import logging
import datetime
now = datetime.datetime.now()


logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('Selenium{}.log'.format(now.date()))


formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class HelperClassExtraction:

    def __init__(self, start_url, deny_list):
        self.start_url = start_url
        self.deny_list = deny_list

    def extract_img_from_src_list(self, list_src, path):
        for element in list_src:
            options = Options()
            options.add_argument("--headless")

            browser2 = webdriver.Firefox(firefox_options=options)
            browser2.implicitly_wait(5)
            browser2.get(element)

            add = ScreenshotPage(_browser=browser2, path=path)

            add.get_adds()

            browser2.close()

    def extract_regular_images_src_list(self, browser, http_prefix, https_prefix):

        browser.switch_to.default_content()

        soup = BeautifulSoup(browser.page_source, 'html.parser')

        list_images_src = []

        for link_img in soup.find_all('img'):
            img_link = link_img.get('src')
            if img_link is not None:

                if img_link.find('.jpg') > -1 or img_link.find('.jpeg') > -1:
                    print("Link {}".format(img_link))

                    if img_link.startswith(http_prefix) is True:
                        list_images_src.append(img_link)

                    if img_link.startswith(https_prefix) is True:
                        list_images_src.append(img_link)

                    if img_link.startswith("//") is True:
                        list_images_src.append(self.start_url+img_link)

                    if img_link.startswith("/") is True and img_link.startswith("//") is False:
                        list_images_src.append(self.start_url+img_link)

        list_images_src = set(list_images_src)

        return list_images_src

    def my_link_extractor_no_generic(self, browser):

        browser.switch_to.default_content()

        soup = BeautifulSoup(browser.page_source, 'html.parser')

        list_src = []

        for link in soup.find_all('a'):
            href = link.get('href')

            if href is not None and (href.startswith("http://www.") is True or href.startswith("https://www.") is True):
                list_src.append(href)

        set_src = list(set(list_src))

        return set_src

    def my_link_extractor(self, browser):

        browser.switch_to.default_content()

        soup = BeautifulSoup(browser.page_source, 'html.parser')

        list_src = []

        for link in soup.find_all('a'):

            href = link.get('href')

            if href is not None and href.startswith(self.start_url) is True:

                if self.check_deny_list(href) is True:
                    list_src.append(href)

        set_src = set(list_src)

        return set_src

    def check_deny_list(self, link):
        if link in self.deny_list:
            return False

        # print(link)
        return True
