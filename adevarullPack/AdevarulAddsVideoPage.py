from PIL import Image
from io import BytesIO
from random import randint
from selenium import webdriver
import random

import hashlib

from helperContinus.HelperClass import HelperClass


class AdevarulAddVideoPage(HelperClass):

    list_add_screenshot = []

    def __init__(self, _browser, path):
        self.browser = _browser

        HelperClass.__init__(self, path)

    def get_adds(self):

        list_adds_src = []

        try:
            list_adds_src.append(self.scenario1())
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))
            pass

    def scenario1(self):

        print("scenario 1")

        # googleAdSense

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_xpath("//div[@Class='adGoogleAdSenseVideoEnd']")

        # aswift_0
        iframe_in_div = div.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe_in_div)

        # google_ads_frame1
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adContent
        div = self.browser.find_element_by_id("adContent")
        self.screenshot(element=div, path=self.path, browser=self.browser)

        print("screenshot in scenario 1 taken")
