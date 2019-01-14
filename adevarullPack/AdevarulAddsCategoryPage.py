from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import copy
from PIL import Image
from io import BytesIO
from random import randint

import hashlib
import time

from helperContinus.HelperClass import HelperClass


class AdevarulAddsCategoryPage(HelperClass):

    def __init__(self, _browser, path):
        self.browser = _browser

        HelperClass.__init__(path)

    def get_category_adds(self):

        list_add_src = []

        self.get_top_add_category_page(list_add_src)

        print(list_add_src)

        return self.eliminate_duplicate(list_add_src)

    def get_middle_add(self, list_add_src):
        try:
            list_add_src.append(self.scenario12_category_page())
        except Exception as ex:
            print("no add in scenario 12")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.scenario13_category_page())
        except Exception as ex:
            print("no add in scenario 13")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.scenario14_category_page())
        except Exception as ex:
            print("no add in scenario 14")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.scenario15_category_page())
        except Exception as ex:
            print("no add in scenario 15")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.scenario18_category_page())
        except Exception as ex:
            print("no add in scenario 18")
            print("Exception {}".format(ex))
            pass

    def get_top_add_category_page(self, list_add_src):

        try:
            list_add_src.append(self.top_add_scenario_1())
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_2())
        except Exception as ex:
            print("no add in scenario 2")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_3())
        except Exception as ex:
            print("no add in scenario 3")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_4())
        except Exception as ex:
            print("no add in scenario 4")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_5())
        except Exception as ex:
            print("no add in scenario 5")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_6())
        except Exception as ex:
            print("no add in scenario 6")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_7())
        except Exception as ex:
            print("no add in scenario 7")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_8())
        except Exception as ex:
            print("no add in scenario 8")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_9())
        except Exception as ex:
            print("no add in scenario 9")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_10())
        except Exception as ex:
            print("no add in scenario 10")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_11())
        except Exception as ex:
            print("no add in scenario 11")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_12())
        except Exception as ex:
            print("no add in scenario 12")
            print("Exception {}".format(ex))
            pass

    def top_add_scenario_1(self):

        print("Top add scenario 1")

        # class = pub_top
        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_class_name("pub_top")
        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        # id aswift 0
        iframe_in_iframe = self.browser.find_element_by_id("aswift 0")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_ads_frame1
        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        # adContent
        div_add = self.browser.find_element_by_id("adContent")
        self.screenshot(element=div_add, path=self.path, browser=self.browser)

        print("screenshot taken in scenario 1")

    def top_add_scenario_2(self):

        # z_adevarul_educatie_top_branding

        print("Top add scenario 2")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_class_name("pub_top")
        iframe = div.find_element_by_tag_name("iframe")

        self.screenshot(element=iframe, path=self.path,browser=self.browser)

        print("screenshot taken in scenario 2")


    def top_add_scenario_3(self):

        print("Top add scenario 3")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_class_name("pub_top")
        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        # id aswift 0
        iframe_in_iframe = self.browser.find_element_by_id("aswift 0")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_ads_frame1
        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_2 = self.browser.find_element_by_id("X1FIF0B")
        iframe_in_iframe_in_iframe_in_iframe = div_2.find_element_by_tag_name("iframe")

        self.browser.switch_to.frame(iframe_in_iframe_in_iframe_in_iframe)

        a_tag = self.browser.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def top_add_scenario_4(self):

        print("Top add scenario 4")

        self.browser.switch_to.default_content()

        # ZTRHtml1B

        div_with_add = self.browser.find_element_by_id("ZTRHtml1B")
        a_tag = div_with_add.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def top_add_scenario_5(self):

        print("Top add scenario 5")

        self.browser.switch_to.default_content()

        # pub_top

        div = self.browser.find_element_by_class_name("pub_top")
        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)


        # id aswift 0
        iframe_in_iframe = self.browser.find_element_by_id("aswift 0")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("google_image_div")

        a_tag = div_with_add.find_element_by_id("aw0")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def top_add_scenario_6(self):

        print("Top add scenario 6")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_class_name("pub_top")
        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        a_tag = self.browser.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def top_add_scenario_7(self):

        print("Top add scenario 7")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_class_name("pub_top")
        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("page1")
        self.screenshot(element=div_with_add, path=self.path,browser=self.browser)

        print("screenshot taken in scenario 7")

    def scenario8_category_page(self):

        print("scenario 8")

        self.browser.switch_to.default_content()

        # pub_top

        div = self.browser.find_element_by_class_name("pub_top")
        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        # id aswift 0
        iframe_in_iframe = self.browser.find_element_by_id("aswift 0")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_ads_frame1
        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)


    def top_add_scenario_11(self):

        print("Top add scenario 11")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_class_name("pub_top")
        img = div.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        print(src)

        return src

    def top_add_scenario_8(self):

        print("Top add scenario 8")

        self.browser.switch_to.default_content()

        # ZtrLTRBra1TB
        # ZtrLTRBra1LB
        # ZtrLTRBra1RB

        div_with = self.browser.find_element_by_id("ZtrLTRBra1TB")
        ins = div_with.find_element_by_tag_name("ins")
        a_tag = ins.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src


    def top_add_scenario_9(self):

        print("Top add scenario 9")

        self.browser.switch_to.default_content()

        # ZtrLTRBra1LB

        div_with = self.browser.find_element_by_id("ZtrLTRBra1LB")
        ins = div_with.find_element_by_tag_name("ins")
        a_tag = ins.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def top_add_scenario_10(self):

        print("Top add scenario 10")

        self.browser.switch_to.default_content()

        # ZtrLTRBra1RB

        div_with = self.browser.find_element_by_id("ZtrLTRBra1RB")
        ins = div_with.find_element_by_tag_name("ins")
        a_tag = ins.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def top_add_scenario_12(self):

        print("Top add scenario 12")

        self.browser.switch_to.default_content()

        #ZTRHtml1B
        div_with = self.browser.find_element_by_id("ZtrLTRBra1LB")
        iframe = div_with.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        div_with_add = self.browser.find_element_by_id("animation_container")
        canvas = div_with_add.find_element_by_id("canvas")

        self.screenshot(element=canvas, path=self.path, browser=self.browser)

        print("screenshot in scenario 17")

    def scenario12_category_page(self):

        print("scenario 12")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_id("main-content")
        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        # id aswift 0
        iframe_in_iframe = self.browser.find_element_by_id("aswift 0")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_ads_frame1
        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("google_image_div")

        a_tag = div_with_add.find_element_by_id("aw0")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        print(src)
        return src

    def scenario13_category_page(self):

        print("scenario 13")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_id("main-content")
        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        # id aswift 0
        iframe_in_iframe = self.browser.find_element_by_id("aswift 0")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_ads_frame1
        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("google_image_div")

        self.screenshot(element=div_with_add, path=self.path, browser=self.browser)

    def scenario14_category_page(self):

        print("scenario 14")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_id("main-content")
        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        # id aswift 0
        iframe_in_iframe = self.browser.find_element_by_id("aswift 0")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_ads_frame1
        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        # id X1FIF0B
        div_2 = self.browser.find_element_by_id("X1FIF0B")
        iframe_in_iframe_in_iframe_in_iframe = div_2.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe_in_iframe)

        iframe_in_iframe_in_iframe_in_iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe_in_iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("Stage")
        self.screenshot(element=div_with_add, path=self.path, browser=self.browser)

        print("screenshot taken in scenario 14")

    def scenario15_category_page(self):

        print("scenario 15")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_id("main-content")
        div_in_div = div.find_element_by_xpath("//div[@Class='wrap clearfix']")

        iframe = div_in_div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        # id aswift 0
        iframe_in_iframe = self.browser.find_element_by_id("aswift 0")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_ads_frame1
        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_2 = self.browser.find_element_by_id("X1FIF0B")
        img = div_2.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        return src

    def scenario18_category_page(self):

        print("scenario 18")

        self.browser.switch_to.default_content()
        #X1Img0B

        div = self.browser.find_element_by_id("main-content")
        div_in_div = div.find_element_by_xpath("//div[@Class='wrap clearfix']")

        iframe = div_in_div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        # id aswift 0
        iframe_in_iframe = self.browser.find_element_by_id("aswift 0")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_ads_frame1
        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_2 = self.browser.find_element_by_id("X1Img0B")
        img = div_2.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        return src

    def scenario19_category_page(self):

        print("scenario 19")

        self.browser.switch_to.default_content()
        # column-med sidebar sidebar-section
        aside = self.browser.find_element_by_class_name("column-med sidebar sidebar-section")

        # zc_adevarul_educatie_rectangle_articol_1
        # zc_adevarul_educatie_rectangle_articol_2

        # element = aside.find_element_by_xpath("//div[contains(text(), 'rectangle_articol')]")
        # aside.find_elements_by_xpath()

        iframe = aside.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        # id aswift 0
        iframe_in_iframe = self.browser.find_element_by_id("aswift 0")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_ads_frame1
        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_2 = self.browser.find_element_by_id("X1FIF0B")
        iframe_in_iframe_in_iframe_in_iframe = div_2.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe_in_iframe)

        a_tag = self.browser.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        print(src)
        return src

    def scenario20_category_page(self):

        print("scenario 20")

        self.browser.switch_to.default_content()

        aside = self.browser.find_element_by_class_name("column-med sidebar sidebar-section")

        iframe = aside.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        div = self.browser.find_element_by_tag_name("div")
        a_tag = div.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        return src



