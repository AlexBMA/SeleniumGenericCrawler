from PIL import Image
from io import BytesIO
from random import randint
from selenium import webdriver
import random

import hashlib

from helperContinus.HelperClass import HelperClass


class AdevarulAddPhotoPage(HelperClass):

    list_add_screenshot = []

    def __init__(self, _browser, path):
        self.browser = _browser

        HelperClass.__init__(self, path)

    def get_adds(self):

        list_adds_src = []

        self.top_add(list_adds_src)

        #mid_add(list_adds_src)

        return self.eliminate_duplicate(list_adds_src)

    def top_add(self, list_adds_src):

        try:
            list_adds_src.append(self.top_add_scenario_1())
            return
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.top_add_scenario_2())
            return
        except Exception as ex:
            print("no add in scenario 2")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.top_add_scenario_3())
            return
        except Exception as ex:
            print("no add in scenario 3")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.top_add_scenario_4())
            return
        except Exception as ex:
            print("no add in scenario 4")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.top_add_scenario_5())
            return
        except Exception as ex:
            print("no add in scenario 5")
            print("Exception {}".format(ex))
            pass

    def top_add_scenario_1(self):

        print("scenario 1")

        self.browser.switch_to.default_content()

        # browser.find_element_by_xpath("//div[@Class='pub_top'")
        div = self.browser.find_element_by_xpath("//div[@Class='pub_top']")
        iframe_in_div = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_div)

        # aswift_0
        iframe_in_iframe = self.browser.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_ads_frame1
        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        # X1Img0B
        div_with_img = self.browser.find_element_by_id("X1Img0B")
        img = div_with_img.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        print(src)

        return src

    def top_add_scenario_2(self):

        print("scenario 2")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_xpath("//div[@Class='pub_top']")
        img = div.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        print(src)

        return src

    def top_add_scenario_3(self):

        print("scenario 3")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_xpath("//div[@Class='pub_top']")
        iframe_in_div = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_div)

        iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("myAd")
        self.screenshot(element=div_with_add, path=self.path, browser=self.browser)

        print("screenshot take in scenario 3")

    def top_add_scenario_4(self):

        print("scenario 4")

        self.browser.switch_to.default_content()
        # ZTRHtml1B

        div = self.browser.find_element_by_id("ZTRHtml1B")

        a_tag = div.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def top_add_scenario_5(self):

        print("scenario 5")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_xpath("//div[@Class='pub_top']")
        iframe_in_div = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_div)

        iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe)

        # animation_container
        div_with_add = self.browser.find_element_by_id("animation_container")
        self.screenshot(element=div_with_add, path=self.path, browser=self.browser)

        print("screenshot taken in scenario 5")



