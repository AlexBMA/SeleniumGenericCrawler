from PIL import Image
from io import BytesIO
from random import randint

import hashlib

from helperContinus.HelperClass import HelperClass


class AdevarulAddsHomePage(HelperClass):
    """Class for getting adds from adevarul site"""

    def __init__(self, path):
        HelperClass.__init__(self, path)

    def get_home_page_ads(self, browser):

        list_add_src = []

        self.get_top_add_2(browser, list_add_src)

        self.get_mid_add_zc_homepage_rectangle_1(browser, list_add_src)

        self.get_mid_add_z_homepage_top_branding(browser, list_add_src)

        try:
            list_add_src.append(self.mid_add_scenario_1(browser))
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.mid_add_scenario_2(browser))
        except Exception as ex:
            print("no add in scenario 2")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.mid_add_scenario_3(browser))
        except Exception as ex:
            print("no add in scenario 3")
            print("Exception {}".format(ex))
            pass

        print(list_add_src)

        return self.eliminate_duplicate(list_add_src)

    def get_mid_add_z_homepage_top_branding(self, browser, list_add_src):
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_1(browser))
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_2(browser))
        except Exception as ex:
            print("no add in scenario 2")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_3(browser))
        except Exception as ex:
            print("no add in scenario 3")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_4(browser))
        except Exception as ex:
            print("no add in scenario 4")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_5(browser))
        except Exception as ex:
            print("no add in scenario 5")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_6(browser))
        except Exception as ex:
            print("no add in scenario 6")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_7(browser))
        except Exception as ex:
            print("no add in scenario 7")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_8(browser))
        except Exception as ex:
            print("no add in scenario 8")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_9(browser))
        except Exception as ex:
            print("no add in scenario 9")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_10(browser))
        except Exception as ex:
            print("no add in scenario 10")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_11(browser))
        except Exception as ex:
            print("no add in scenario 11")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_12(browser))
        except Exception as ex:
            print("no add in scenario 12")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_13(browser))
        except Exception as ex:
            print("no add in scenario 13")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_14(browser))
        except Exception as ex:
            print("no add in scenario 14")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_15(browser))
        except Exception as ex:
            print("no add in scenario 15")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_z_homepage_scenario_16(browser))
        except Exception as ex:
            print("no add in scenario 16")
            print("Exception {}".format(ex))
            pass

    def get_mid_add_zc_homepage_rectangle_1(self, browser, list_add_src):
        try:
            list_add_src.append(self.mid_add_zc_homepage_scenario_1(browser))
            return
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_zc_homepage_scenario_2(browser))
            return
        except Exception as ex:
            print("no add in scenario 2")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_zc_homeapage_scenario_3(browser))
            return
        except Exception as ex:
            print("no add in scenario 3")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_src.append(self.mid_add_zc_homepage_scenario_4(browser))
            return
        except Exception as ex:
            print("no add in scenario 4")
            print("Exception {}".format(ex))
            pass

    def mid_add_zc_homepage_scenario_1(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_with_side_add = div_main_content.find_element_by_id("zc_homepage_rectangle_1")

        print("scenario 9 mid add ")

        img = div_with_side_add.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def mid_add_zc_homepage_scenario_2(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_with_side_add = div_main_content.find_element_by_id("zc_homepage_rectangle_1")
        frame_inside_div_aside = div_with_side_add.find_element_by_tag_name("iframe")

        #print("scenario 10 mid add ")

        browser.switch_to.frame(frame_inside_div_aside)
        canvas_insdie_iframe = browser.find_element_by_id("canvas")

        self.screenshot(element=canvas_insdie_iframe, path=self.path, browser=browser)
        print("screenshoot taken in scenario 2")

    def mid_add_zc_homeapage_scenario_3(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_with_side_add = div_main_content.find_element_by_id("zc_homepage_rectangle_1")
        frame_inside_div_aside = div_with_side_add.find_element_by_tag_name("iframe")
        browser.switch_to.frame(frame_inside_div_aside)

        #print("scenario 11 mid add")

        img = browser.find_element_by_tag("img")
        src = img.get_attribute("src")

        print(src)
        return src

    def mid_add_zc_homepage_scenario_4(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_with_side_add = div_main_content.find_element_by_id("zc_homepage_rectangle_1")
        frame_inside_div_aside = div_with_side_add.find_element_by_tag_name("iframe")

        browser.switch_to.frame(frame_inside_div_aside)

        #print("scenario 12 mid add")

        img = browser.find_element_by_tag("img")
        src = img.get_attribute("src")

        print(src)
        return src

    def mid_add_z_homepage_scenario_1(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_with_side_add = div_main_content.find_element_by_id("zc_homepage_rectangle_1")

        frame_inside_div_aside = div_with_side_add.find_element_by_tag_name("iframe")

        print("scenario 13 mid add")

        browser.switch_to.frame(frame_inside_div_aside)

        img = browser.find_element_by_tag("img")
        src = img.get_attribute("src")

        print(src)
        return src

    def mid_add_z_homepage_scenario_2(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        frame_inside_div = div_that_contains_iframe.find_element_by_tag_name("iframe")

        print("scenario 14 mid add")

        browser.switch_to.frame(frame_inside_div)

        div_in_iframe = browser.find_element_by_tag_name("div")
        div_in_div_in_iframe = div_in_iframe.find_element_by_tag_name("div")
        div_in_div_in_div_in_iframe = div_in_div_in_iframe.find_element_by_tag_name("div")
        self.screenshot(element=div_in_div_in_div_in_iframe, path=self.path ,browser=browser)

        print("screenshot taken scenario 14")

    def mid_add_z_homepage_scenario_3(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        frame_in_div = div_that_contains_iframe.find_element_by_tag_name("iframe")
        browser.switch_to.frame(frame_in_div)

        print("scenario 15 mid add")

        iframe_in_iframe = browser.switch_to.frame("google_ads_frame1")
        browser.switch_to.frame(iframe_in_iframe)

        div_wtih_add = browser.find_element_by_id("adContent")
        self.screenshot(element=div_wtih_add, path=self.path, browser=browser)

        print("screenshot taken in scenario 15")

    def mid_add_z_homepage_scenario_4(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        frame_inside_div = div_that_contains_iframe.find_element_by_tag_name("iframe")
        browser.switch_to.frame(frame_inside_div)

        print("scenario 16 mid add")

        iframe_inside_iframe = browser.switch_to.frame("google_ads_frame1")
        browser.switch_to.frame(iframe_inside_iframe)

        # X1Img0B
        div_with_img = browser.find_element_by_id("X1Img0B")
        img = div_with_img.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        print(src)
        return src

    def mid_add_z_homepage_scenario_5(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        frame_inside_div = div_that_contains_iframe.find_element_by_tag_name("iframe")
        browser.switch_to.frame(frame_inside_div)

        print("scenario 17 mid add")

        div_with_frame = browser.find_element_by_id("X1Img0B")
        iframe_in_the_iframe2 = div_with_frame.find_element_by_tag_name("iframe")

        # au-tag au-tag-processed
        browser.switch_to.frame(iframe_in_the_iframe2)
        div_important = browser.find_element_by_class_name("au-tag au-tag-processed")

        div_in_div = div_important.find_element("div")
        div_in_div_in_div = div_in_div.find_element_by_tag_name("div")
        iframe_in_div_in_div_in_div = div_in_div_in_div.find_element_by_tag_name("iframe")

        browser.switch_to.frame(iframe_in_div_in_div_in_div)
        div_with_canvas = browser.find_element_by_tag_name("animation_container")
        self.screenshot(element=div_with_canvas, path=self.path, browser=browser)

        print("screenshoot taken in 17 mid add")

    def mid_add_z_homepage_scenario_6(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        iframe_in_div = div_that_contains_iframe.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_div)

        print("scenario 18 mid add")

        iframe_in_the_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_the_iframe)

        div_with_canvas = browser.find_element_by_tag_name("animation_container")
        self.screenshot(element=div_with_canvas, path=self.path, browser=browser)

        print("screenshot taken in 18 mid add")

    def mid_add_z_homepage_scenario_7(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        frame_inside_div = div_that_contains_iframe.find_element_by_tag_name("iframe")
        browser.switch_to.frame(frame_inside_div)

        print("scenario 19 mid add")

        a_tag_with_img = browser.find_element_by_tag_name("a")

        img = a_tag_with_img.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        print(src)
        return src

    def mid_add_z_homepage_scenario_8(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        frame_inside_div = div_that_contains_iframe.find_element_by_tag_name("iframe")
        browser.switch_to.frame(frame_inside_div)

        iframe_inside_the_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_inside_the_iframe)

        print("scenario 20 mid add")

        a_tag_with_img = browser.find_element_by_tag_name("a")

        img = a_tag_with_img.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        print(src)
        return src

    def mid_add_z_homepage_scenario_9(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        frame_inside_div = div_that_contains_iframe.find_element_by_tag_name("iframe")
        browser.switch_to.frame(frame_inside_div)

        iframe_inside_the_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_inside_the_iframe)

        print("scenario 21 mid add")

        #print("here in gwt scenario")
        div = browser.find_element_by_id("page1")
        div_gwt = div.find_element_by_tag_name("div")
        self.screenshot(element=div_gwt, path=self.path, browser=browser)

        print("screenshot taken scenario 21")

    def mid_add_z_homepage_scenario_10(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        frame_in_div = div_that_contains_iframe.find_element_by_tag_name("iframe")
        browser.switch_to.frame(frame_in_div)

        print("scenario 22 mid add")

        iframe_in_the_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_the_iframe)

        iframe_in_iframe_in_frame = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_iframe_in_frame)

        my_add_canvas = browser.find_element_by_id("myAdCanvas")
        self.screenshot(element=my_add_canvas, path=self.path, browser=browser)

        print("screenshot taken scenario 22")

    def mid_add_z_homepage_scenario_11(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        frame_in_div = div_that_contains_iframe.find_element_by_tag_name("iframe")
        browser.switch_to.frame(frame_in_div)

        print("scenario 23 mid add")

        iframe_in_the_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_the_iframe)

        iframe_in_iframe_in_frame = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_iframe_in_frame)

        browser.switch_to.frame(iframe_in_iframe_in_frame)

        img = browser.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)
        return src

    def mid_add_z_homepage_scenario_12(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        frame_in_div = div_that_contains_iframe.find_element_by_tag_name("iframe")

        print("scenario 24 mid add")

        self.screenshot(element=frame_in_div, path=self.path,browser=browser)

        print("screenshot taken in scenario 24")


    def mid_add_z_homepage_scenario_13(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        div_in_div = div_that_contains_iframe.find_element_by_tag_name("div")

        print("scenario 25  mid add")

        img = div_in_div.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        print(src)
        return src

    def mid_add_z_homepage_scenario_14(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        div_in_div = div_that_contains_iframe.find_element_by_tag_name("div")

        print("scenario 26 mid add")

        img = div_in_div.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        print(src)
        return src

    def mid_add_z_homepage_scenario_15(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        div_in_div = div_that_contains_iframe.find_element_by_tag_name("div")

        print("scenario 27 mid add")

        img = div_in_div.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)
        return src

    def mid_add_z_homepage_scenario_16(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        print("scenario 28 mid add")

        img = div_that_contains_iframe.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)
        return src

    def mid_add_scenario_1(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")


    def mid_add_scenario_2(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        print("scenario 30 mid add")

        # ZTRHtml2B div id
        div_that_contains_link = browser.find_element_by_id("ZTRHtml2B")
        a_tag = div_that_contains_link.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src2 = img.get_attribute("src")


        # img_list = div_that_contains_img.find_elements_by_tag_name("img")
        # print("size list:")
        # print(len(img_list))
        print(src2)
        return src2

    def mid_add_scenario_3(self, browser):

        browser.switch_to.default_content()

        div_main_content = browser.find_element_by_id("main-content")

        div_with_iframe2 = div_main_content.find_element_by_id("ZtrLTRBra2TB")
        iframe22 = div_with_iframe2.find_element_by_tag_name("iframe")

        print("scenario 31 mid add")

        browser.switch_to.frame(iframe22)
        canvas = browser.find_element_by_tag_name("canvas")

        self.screenshot(element=canvas, path=self.path, browser=browser)

        print("screenshot taken in scenario 31")

    def get_top_add_2(self, browser, list_add_src):

        try:
            list_add_src.append(self.top_add_scenario_1(browser))
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_2(browser))
        except Exception as ex:
            print("no add in scenario 2")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_3(browser))
        except Exception as ex:
            print("no add in scenario 3")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_4(browser))
        except Exception as ex:
            print("no add in scenario 4")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_5(browser))
        except Exception as ex:
            print("no add in scenario 5")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_6(browser))
        except Exception as ex:
            print("no add in scenario 6")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_7(browser))
        except Exception as ex:
            print("no add in scenario 7")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_src.append(self.top_add_scenario_8(browser))
        except Exception as ex:
            print("no add in scenario 8")
            print("Exception {}".format(ex))
            pass

        return list_add_src

    def top_add_scenario_8(self, browser):

        browser.switch_to.default_content()

        header = browser.find_element_by_id("top")

        div_of_the_top_iframe = header.find_element_by_id("z_homepage_top")

        print("scenario 8 top add")

        iframe_in_top_div = div_of_the_top_iframe.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_top_div)

        iframe_in_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_iframe)

        div_in_2th_iframe = browser.find_element_by_tag_name("div")

        self.screenshot(element=div_in_2th_iframe, path=self.path, browser=browser)

        print("screenshot taken in scenario 8")

    def top_add_scenario_7(self, browser):

        browser.switch_to.default_content()

        header = browser.find_element_by_id("top")

        div_of_the_top_iframe = header.find_element_by_id("z_homepage_top")

        print("scenario 7 top add")

        iframe_in_top_div = div_of_the_top_iframe.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_top_div)

        iframe_in_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_iframe_in_iframe)

        iframe_in_iframe_in_iframe_in_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_iframe_in_iframe_in_iframe)

        iframe_in_iframe_in_iframe_in_iframe_in_iframe = browser.find_element_by_tag_name("iframe")

        browser.switch_to.frame(iframe_in_iframe_in_iframe_in_iframe_in_iframe)
        div_in_5th_iframe = browser.find_element_by_tag_name("div")

        self.screenshot(element=div_in_5th_iframe, path=self.path, browser=browser)

        print("screenshot taken in scenario 7")


    def top_add_scenario_6(self, browser):

        browser.switch_to.default_content()

        header = browser.find_element_by_id("top")

        div_Of_The_Top_Iframe = header.find_element_by_id("z_homepage_top")

        print("Scenario 6 top add")

        iframe_in_div = div_Of_The_Top_Iframe.find_element_by_tag_name("iframe")

        browser.switch_to.frame(iframe_in_div)

        div_with_add = browser.find_element_by_id("stage")

        print("div that contains add")

        self.screenshot(element=div_with_add, path=self.path, browser=browser)

    def top_add_scenario_5(self, browser):

        browser.switch_to.default_content()

        header = browser.find_element_by_id("top")

        div_Of_The_Top_Iframe = header.find_element_by_id("z_homepage_top")

        print("Scenario 5 top add")

        img_child_of_elem = div_Of_The_Top_Iframe.find_element_by_tag_name("img")
        src = img_child_of_elem.get_attribute("src")

        print(src)

        return src

    def top_add_scenario_4(self, browser):

        browser.switch_to.default_content()

        header = browser.find_element_by_id("top")

        div = header.find_element_by_id("z_homepage_top")

        iframe_child_of_elem = div.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_child_of_elem)

        frame_in_frame = browser.find_element_by_id("aswift_0")
        browser.switch_to.frame(frame_in_frame)

        frame_in_frame_in_frame = browser.find_element_by_id("google_ads_frame1")
        browser.switch_to.frame(frame_in_frame_in_frame)

        print("Scenario 4 top  add")
        div_of_iframe = browser.find_element_by_id("root_template_div")
        self.screenshot(element=div_of_iframe, path=self.path, browser=browser)

        print("screenshot taken in scenario 4")

    def top_add_scenario_3(self, browser):

        browser.switch_to.default_content()

        header = browser.find_element_by_id("top")

        div = header.find_element_by_id("z_homepage_top")

        iframe_child_of_elem = div.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_child_of_elem)

        frame_in_frame = browser.find_element_by_id("aswift_0")
        browser.switch_to.frame(frame_in_frame)

        frame_in_frame_in_frame = browser.find_element_by_id("google_ads_frame1")
        browser.switch_to.frame(frame_in_frame_in_frame)

        print("Scenario 3 top add")
        img_by_class = browser.find_element_by_class_name("img_ad")
        src_2 = img_by_class.get_attribute("src")
        print(img_by_class.tag_name)
        return src_2

    def top_add_scenario_2(self, browser):

        browser.switch_to.default_content()

        header = browser.find_element_by_id("top")

        div = header.find_element_by_id("z_homepage_top")

        iframe_child_of_elem = div.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_child_of_elem)

        frame_inside_frame = browser.find_element_by_id("aswift_0")
        browser.switch_to.frame(frame_inside_frame)

        frame_inside_frame_inside_frame = browser.find_element_by_id("google_ads_frame1")
        browser.switch_to.frame(frame_inside_frame_inside_frame)

        print("Scenario 2 top add")
        div_tag_img = browser.find_element_by_tag_name("div")
        img_child_of_elem = div_tag_img.find_element_by_tag_name("img")

        src = img_child_of_elem.get_attribute("src")

        print(src)
        return src

    def top_add_scenario_1(self, browser):

        browser.switch_to.default_content()

        header = browser.find_element_by_id("top")

        div = header.find_element_by_id("z_homepage_top")

        iframe_child_of_elem = div.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_child_of_elem)

        frame_inside_frame = browser.find_element_by_id("aswift_0")
        browser.switch_to.frame(frame_inside_frame)

        frame_inside_frame_inside_frame = browser.find_element_by_id("google_ads_frame1")
        browser.switch_to.frame(frame_inside_frame_inside_frame)

        print("Scenario 1 top add")

        a_tag = browser.find_element_by_tag_name("a")
        img_add = a_tag.find_element_by_tag_name("img")
        src = img_add.get_attribute("src")
        # print(img_add.tag_name)
        print(src)
        return src

    def get_top_add(self, browser):

        #print(browser.page_source)

        header = browser.find_element_by_id("top")
        div_of_the_top_iframe = header.find_element_by_id("z_homepage_top")

        rez = "#"

        try:
            rez = self.check_if_child_iframe_exists(browser, div_of_the_top_iframe)
            return rez
        except Exception as ex:
            print("No iframe found")
            print("Exception {}".format(ex))
            pass

        try:
            rez = self.add_scenario5_top_add_home_page(browser, div_of_the_top_iframe)
            return rez
        except Exception as ex:
            print("No img found")
            print("Exception {}".format(ex))
            pass

        try:
            self.add_scenario6_top_add_home_page(browser, div_of_the_top_iframe)
            return rez
        except Exception as ex:
            print("No div with id = stage")
            print("Exception {}".format(ex))
            pass

        try:
            self.add_scenario7_top_add_home_page(browser, div_of_the_top_iframe)
        except Exception as ex:
            print("No div in iframe -> iframe -> iframe -> iframe -> iframe")
            print("Exception {}".format(ex))

        try:
            self.add_scenario8_top_add_home_page(browser,div_of_the_top_iframe)
        except Exception as ex:
            print("No div in iframe -> iframe")
            print("Exception {}".format(ex))

        print(rez)

    def add_scenario8_top_add_home_page(self, browser, div_of_the_top_iframe):
        print("scenario 8 top add")
        iframe_in_top_div = div_of_the_top_iframe.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_top_div)
        iframe_in_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_iframe)
        div_in_2th_iframe = browser.find_element_by_tag_name("div")
        self.screenshot(element=div_in_2th_iframe, path=self.path, browser=browser)

    def add_scenario7_top_add_home_page(self, browser, div_Of_the_top_iframe):
        print("scenario 7 top add")
        iframe_in_top_div = div_Of_the_top_iframe.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_top_div)
        iframe_in_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_iframe)
        iframe_in_iframe_in_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_iframe_in_iframe)
        iframe_in_iframe_in_iframe_in_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_iframe_in_iframe_in_iframe)
        iframe_in_iframe_in_iframe_in_iframe_in_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_iframe_in_iframe_in_iframe_in_iframe)
        div_in_5th_iframe = browser.find_element_by_tag_name("div")
        self.screenshot(element=div_in_5th_iframe, path=self.path, browser=browser)


    def check_if_child_iframe_exists(self, browser, div_Of_The_Top_Iframe):
        iframe_child_of_elem = div_Of_The_Top_Iframe.find_element_by_tag_name("iframe")
        # print(div_Of_The_Top_Iframe.tag_name)
        # print(iframe_child_of_elem.tag_name)
        # print("Here in the function")

        # aswift_0 the id of the frame
        browser.switch_to.frame(iframe_child_of_elem)
        frame_inside_frame = browser.find_element_by_id("aswift_0")
        browser.switch_to.frame(frame_inside_frame)
        # print("Here found  aswift_0")

        frame_inside_frame_inside_frame = browser.find_element_by_id("google_ads_frame1")
        browser.switch_to.frame(frame_inside_frame_inside_frame)

        # print("Here found google_ads_frame1")

        try:
            return self.add_scenario1_top_add_home_page(browser)
        except Exception as ex:
            print("a tag not found")
            print("Exception {}".format(ex))
            pass
        try:
            return self.add_scenario2_top_add_home_page(browser)
        except Exception as ex:
            print("div not found | img not found")
            print("Exception {}".format(ex))
            pass
        try:
            return self.add_scenario3_top_add_home_page(browser)
        except Exception as ex:
            print("no img with calss img_ad")
            print("Exception {}".format(ex))
            pass
        try:
            self.add_scenario4_top_add_home_page(browser)
        except Exception as ex:
            print("no svg add")
            print("Exception {}".format(ex))
            pass

    def add_scenario1_top_add_home_page(self, browser):
        print("Scenario 1 top add")
        global src
        a_tag = browser.find_element_by_tag_name("a")
        img_add = a_tag.find_element_by_tag_name("img")
        src = img_add.get_attribute("src")
        # print(img_add.tag_name)
        print(src)
        return src

    def add_scenario2_top_add_home_page(self, browser):
        print("Scenario 2 top add")
        global src
        div_tag_img = browser.find_element_by_tag_name("div")
        img_child_of_elem = div_tag_img.find_element_by_tag_name("img")
        src = img_child_of_elem.get_attribute("src")
        # print(div_tag_img.tag_name)
        # print(img_child_of_elem.tag_name)
        print(src)
        return src

    def add_scenario3_top_add_home_page(self, browser):
        print("Scenario 3 top add")
        img_by_class = browser.find_element_by_class_name("img_ad")
        src_2 = img_by_class.get_attribute("src")
        print(img_by_class.tag_name)
        return src_2

    def add_scenario4_top_add_home_page(self, browser):
        print("Scenario 4 top  add")
        div_of_iframe = browser.find_element_by_id("root_template_div")
        self.screenshot(element=div_of_iframe, path=self.path, browser=browser)
        #print(div_of_iframe.location)
        #print(div_of_iframe.size)
        #print(div_of_iframe.text)
        # png_shot = div_of_iframe.screenshot_as_png
        # print(png_shot)

    def add_scenario5_top_add_home_page(self, broswer, div_Of_The_Top_Iframe):
        print("Scenario 5 top add")
        img_child_of_elem = div_Of_The_Top_Iframe.find_element_by_tag_name("img")
        src = img_child_of_elem.get_attribute("src")
        # print(img_child_of_elem.tag_name)
        print(src)
        return src

    def add_scenario6_top_add_home_page(self, browser, div_Of_The_Top_Iframe):
        print("Scenario 6 top add")
        iframe_in_div = div_Of_The_Top_Iframe.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_div)
        div_with_add = browser.find_element_by_id("stage")
        print("div that contains add")
        self.screenshot(element=div_with_add, path=self.path, browser=browser)



    def add_scenario4_main_content(self, div_with_side_add):
        img = div_with_side_add.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)
        return src

    def add_scenario1_main_content(self,browser):
        # google_ads_frame1
        # iframe_inside_iframe = browser2.switch_to.frame("google_ads_frame1")

        # adContent
        div_wtih_add = browser.find_element_by_id("adContent")

    def add_scenario2_main_content(self, browser):
        # google_ads_frame1
        # iframe_inside_iframe = browser2.switch_to.frame("google_ads_frame1")

        # X1Img0B
        div_with_img = browser.find_element_by_id("X1Img0B")
        img = div_with_img.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)
        return src

    def add_scenario3_main_content(self, browser):

        div_with_frame = browser.find_element_by_id("X1Img0B")
        iframe_inside_the_iframe2 = div_with_frame.find_element_by_tag_name("iframe")

        # au-tag au-tag-processed
        browser.switch_to.frame(iframe_inside_the_iframe2)
        div_important = browser.find_element_by_class_name("au-tag au-tag-processed")
        div_inside_div = div_important.find_element("div")
        div_inside_div_inside_div = div_inside_div.find_element_by_tag_name("div")
        iframe_inside_div_inside_div_inside_div = div_inside_div_inside_div.find_element_by_tag_name("iframe")

        browser.switch_to.frame(iframe_inside_div_inside_div_inside_div)
        div_with_canvas = browser.find_element_by_tag_name("animation_container")
        self.screenshot(element=div_with_canvas, path=self.path, browser=browser)
        print("got the div with the canvas long chain")

    def get_mid_add(self, browser):
        # elem = browser.find_element_by_xpath("..")
        # print(elem.tag_name)

        browser.switch_to.default_content()

        # print(browser2.page_source)
        print(browser.current_url)
        # print(browser.page_source)

        div_main_content = browser.find_element_by_id("main-content")

        div_with_side_add = browser.find_element_by_id("zc_homepage_rectangle_1")

        try:
            self.add_scenario4_main_content(div_with_side_add)
        except Exception as ex:
            print("no side add")
            print("Exception {}".format(ex))
            pass

        try:
            frame_in_div_aside = div_with_side_add.find_element_by_tag_name("iframe")
            browser.switch_to.frame(frame_in_div_aside)
            canvas_insdie_iframe = browser.find_element_by_id("canvas")
            self.screenshot(element=canvas_insdie_iframe, path=self.path, browser=browser)
        except Exception:
            print("no side add in canvas")
            print("Exception {}".format(ex))
            pass

        try:
            frame_in_div_aside = div_with_side_add.find_element_by_tag_name("iframe")
            browser.switch_to.frame(frame_in_div_aside)
            img = browser.find_element_by_tag("img")
            src = img.get_attribute("src")
            print(src)
            return src
        except Exception:
            print("no side add in a tag with img tag")
            print("Exception {}".format(ex))
            pass


        browser.switch_to.default_content()
        div_that_contains_iframe = div_main_content.find_element_by_id("z_homepage_top_branding")

        try:
            frame_inside_div = div_that_contains_iframe.find_element_by_tag_name("iframe")
            browser.switch_to.frame(frame_inside_div)

            try:
                self.div_div_div_scenario(browser)
            except Exception as ex:
                print("no add in iframe -> div -> div -> div")
                print("Exception {}".format(ex))
                pass

            try:
                self.google_ads_frame1_scenario(browser)
            except Exception as ex:
                print("no iframe with google_ads_frame1")
                print("Exception {}".format(ex))
                pass

            try:
                self.animation_container_scenario(browser)
                print("got the div with the canvas")
            except Exception as ex:
                print("no add on a canvas ")
                print("Exception {}".format(ex))
                pass

            try:
                a_tag_with_img = browser.find_element_by_tag_name("a")
                return self.add_scenario4_main_content(a_tag_with_img)
            except Exception as ex:
                print("no a tag with img tag inside")
                print("Exception {}".format(ex))
                pass

            try:
                iframe_inside_the_iframe = browser.find_element_by_tag_name("iframe")
                browser.switch_to.frame(iframe_inside_the_iframe)

                a_tag_with_img = browser.find_element_by_tag_name("a")
                return self.add_scenario4_main_content(a_tag_with_img)
            except Exception as ex:
                print("no a tag with img tag")
                print("Exception {}".format(ex))
                pass



            try:
                iframe_inside_the_iframe = browser.find_element_by_tag_name("iframe")
                browser.switch_to.frame(iframe_inside_the_iframe)

                # print(browser.page_source)
                try:
                    print("here in gwt scenario")
                    div = browser.find_element_by_id("page1")
                    div_gwt = div.find_element_by_tag_name("div")
                    self.screenshot(element=div_gwt, path=self.path, browser=browser)
                except Exception as ex:
                    print("no gwt img")
                    print("Exception {}".format(ex))
                    pass

                iframe_in_iframe_in_frame = browser.find_element_by_tag_name("iframe")

                try:
                    browser.switch_to.frame(iframe_in_iframe_in_frame)
                    my_add_canvas = browser.find_element_by_id("myAdCanvas")
                    self.screenshot(element=my_add_canvas, path=self.path, browser= browser)
                except Exception as ex:
                    print("no canvas in iframe -> iframe -> iframe")
                    print("Exception {}".format(ex))
                    pass

                try:
                    browser.switch_to.frame(iframe_in_iframe_in_frame)
                    img = browser.find_element_by_tag_name("img")
                    src = img.get_attribute("src")
                    print(src)
                    return src
                except Exception as ex:
                    print("no img in iframe -> iframe -> iframe")
                    print("Exception {}".format(ex))
                    pass

            except Exception as ex:
                print("$$$$%%%")
                print("Exception {}".format(ex))
                pass

            self.screenshot(element=frame_inside_div, path=self.path, browser=browser)

        except Exception as ex:
            print("no iframe in the div with z_homepage_top_branding")
            print("Exception {}".format(ex))
            pass

        try:
            div_inside_div = div_that_contains_iframe.find_element_by_tag_name("div")
            print("here")
            return self.add_scenario4_main_content(div_inside_div)
        except Exception as ex:
            print("no div inside the div with z_homepage_top_branding")
            print("Exception {}".format(ex))

        try:
            return self.add_scenario4_main_content(div_that_contains_iframe)
        except Exception as ex:
            print("no img found")
            print("Exception {}".format(ex))

        try:

            # ZTRHtml2B div id
            div_that_contains_link = browser.find_element_by_id("ZTRHtml2B")
            a_tag = div_that_contains_link.find_element_by_tag_name("a")
            img = a_tag.find_element_by_tag_name("img")
            src2 = img.get_attribute("src")

            # img_list = div_that_contains_img.find_elements_by_tag_name("img")
            # print("size list:")
            # print(len(img_list))
            print(src2)
            return src2
        except Exception as ex:
            print("no img in the  div with id ZTRHtml2B")
            print("Exception {}".format(ex))

        try:
            # ZtrLTRBra2TB
            div_with_iframe2 = browser.find_element_by_id("ZtrLTRBra2TB")
            iframe22 = div_with_iframe2.find_element_by_tag_name("iframe")
            browser.switch_to.frame(iframe22)
            canvas = browser.find_element_by_tag_name("canvas")
            self.screenshot(element=canvas, path=self.path, browser=browser)
        except Exception as ex:
            print("no id tag with id ZtrLTRBra2TB")
            print("Exception {}".format(ex))

        print("here")

        return ""

    def animation_container_scenario(self, browser):
        print("here")
        iframe_in_the_iframe = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(iframe_in_the_iframe)
        div_with_canvas = browser.find_element_by_tag_name("animation_container")
        self.screenshot(element=div_with_canvas, path=self.path, browser=browser)

    def div_div_div_scenario(self, browser):
        div_in_iframe = browser.find_element_by_tag_name("div")
        div_in_div_in_iframe = div_in_iframe.find_element_by_tag_name("div")
        div_in_div_in_div_in_iframe = div_in_div_in_iframe.find_element_by_tag_name("div")
        self.screenshot(element=div_in_div_in_div_in_iframe, path=self.path, browser=browser)

    def google_ads_frame1_scenario(self, browser):
        iframe_in_iframe = browser.switch_to.frame("google_ads_frame1")
        browser.switch_to.frame(iframe_in_iframe)
        self.add_scenario1_main_content(browser)
        self.add_scenario2_main_content(browser)
        self.add_scenario3_main_content(browser)


