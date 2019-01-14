from PIL import Image
from io import BytesIO
from random import randint

import hashlib

from helperContinus.HelperClass import HelperClass


class ZiareComAddsCategoryPage(HelperClass):

    list_add_screenshot = []

    def __init__(self, _browser, url, path):
        self.browser = _browser
        self.url = url
        HelperClass.__init__(self, path)

    def get_category_page_ads(self):

        list_ads_src = []

        self.get_top_ads(list_ads_src)

        self.get_right_add(list_ads_src)

        return self.eliminate_duplicate(list_ads_src)

    def get_right_add(self, list_adds_src):

        try:
            list_adds_src.append(self.right_scenario_1())
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_2())
        except Exception as ex:
            print("no add in scenario 2")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_3())
        except Exception as ex:
            print("no add in scenario 3")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_4())
        except Exception as ex:
            print("no add in scenario 4")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_5())
        except Exception as ex:
            print("no add in scenario 5")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_6())
        except Exception as ex:
            print("no add in scenario 6")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_7())
        except Exception as ex:
            print("no add in scenario 7")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_8())
        except Exception as ex:
            print("no add in scenario 8")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_9())
        except Exception as ex:
            print("no add in scenario 9")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_10())
        except Exception as ex:
            print("no add in scenario 10")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_11())
        except Exception as ex:
            print("no add in scenario 11")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_12())
        except Exception as ex:
            print("no add in scenario 12")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_13())
        except Exception as ex:
            print("no add in scenario 13")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_14())
        except Exception as ex:
            print("no add in scenario 14")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_15())
        except Exception as ex:
            print("no add in scenario 15")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_16())
        except Exception as ex:
            print("no add in scenario 16")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_17())
        except Exception as ex:
            print("no add in scenario 17")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_18())
        except Exception as ex:
            print("no add in scenario 18")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_19())
        except Exception as ex:
            print("no add in scenario 19")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_20())
        except Exception as ex:
            print("no add in scenario 20")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_21())
        except Exception as ex:
            print("no add in scenario 21")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_22())
        except Exception as ex:
            print("no add in scenario 22")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_23())
        except Exception as ex:
            print("no add in scenario 23")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_24())
        except Exception as ex:
            print("no add in scenario 24")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_25())
        except Exception as ex:
            print("no add in scenario 25")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_26())
        except Exception as ex:
            print("no add in scenario 26")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_27())
        except Exception as ex:
            print("no add in scenario 27")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_28())
        except Exception as ex:
            print("no add in scenario 28")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_29())
        except Exception as ex:
            print("no add in scenario 29")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_30())
        except Exception as ex:
            print("no add in scenario 30")
            print("Exception {}".format(ex))
            pass
        try:
            list_adds_src.append(self.right_scenario_31())
        except Exception as ex:
            print("no add in scenario 31")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_32())
        except Exception as ex:
            print("no add in scenario 32")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_33())
        except Exception as ex:
            print("no add in scenario 33")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_34())
        except Exception as ex:
            print("no add in scenario 34")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_35())
        except Exception as ex:
            print("no add in scenario 35")
            print("Exception {}".format(ex))
            pass
        try:
            list_adds_src.append(self.right_scenario_36())
        except Exception as ex:
            print("no add in scenario 36")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_37())
        except Exception as ex:
            print("no add in scenario 37")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_38())
        except Exception as ex:
            print("no add in scenario 38")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_39())
        except Exception as ex:
            print("no add in scenario 39")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_40())
        except Exception as ex:
            print("no add in scenario 40")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_41())
        except Exception as ex:
            print("no add in scenario 41")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_42())
        except Exception as ex:
            print("no add in scenario 42")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_43())
        except Exception as ex:
            print("no add in scenario 43")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_44())
        except Exception as ex:
            print("no add in scenario 44")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_45())
        except Exception as ex:
            print("no add in scenario 45")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_46())
        except Exception as ex:
            print("no add in scenario 46")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_47())
        except Exception as ex:
            print("no add in scenario 47")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_48())
        except Exception as ex:
            print("no add in scenario 48")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_49())
        except Exception as ex:
            print("no add in scenario 49")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_50())
        except Exception as ex:
            print("no add in scenario 50")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_51())
        except Exception as ex:
            print("no add in scenario 51")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_52())
        except Exception as ex:
            print("no add in scenario 52")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_53())
        except Exception as ex:
            print("no add in scenario 53")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_54())
        except Exception as ex:
            print("no add in scenario 54")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_55())
        except Exception as ex:
            print("no add in scenario 55")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_56())
        except Exception as ex:
            print("no add in scenario 56")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_57())
        except Exception as ex:
            print("no add in scenario 57")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_58())
        except Exception as ex:
            print("no add in scenario 58")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_59())
        except Exception as ex:
            print("no add in scenario 59")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_60())
        except Exception as ex:
            print("no add in scenario 60")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_61())
        except Exception as ex:
            print("no add in scenario 61")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_62())
        except Exception as ex:
            print("no add in scenario 62")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_63())
        except Exception as ex:
            print("no add in scenario 63")
            print("Exception {}".format(ex))
            pass
        try:
            list_adds_src.append(self.right_scenario_64())
        except Exception as ex:
            print("no add in scenario 64")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_65())
        except Exception as ex:
            print("no add in scenario 65")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.right_scenario_66())
        except Exception as ex:
            print("no add in scenario 66")
            print("Exception {}".format(ex))
            pass

    def right_scenario_1(self):
        print("Right add scenario 1")
        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4

        iframe = right_side_div.find_element_by_id("aswift_4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame5

        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame5")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = iframe_in_iframe.find_element_by_id("google_image_div")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 1")

    def right_scenario_2(self):
        print("Right add scenario 2")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_3
        iframe = right_side_div.find_element_by_id("aswift_3")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame4
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame4")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        # google_image_div

        div = self.browser.find_element_by_id("google_image_div")

        a = div.find_element_by_id("aw0")

        img = a.find_element_by_tag_name("img")

        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_3(self):

        print("Right add scenario 3")

        self.browser.switch_to.default_content()

        # class = banner_right_boom
        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        iframe = right_side_div.find_element_by_id("aswift_4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame5
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame5")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_4(self):

        print("Right add scenario 4")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_0
        iframe = right_side_div.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame10
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame10")
        self.browser.switch_to.frame(iframe_in_iframe)

        # ad-container
        div_with_add = self.browser.find_element_by_id("ad-container")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 4")

    def right_scenario_5(self):
        print("Right add scenario 5")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_6
        iframe = right_side_div.find_element_by_id("aswift_6")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame8
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame8")
        self.browser.switch_to.frame(iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("ad-container")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 5")

    def right_scenario_6(self):

        print("Right add scenario 6")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift 4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame9
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame9")
        self.browser.switch_to.frame(iframe_in_iframe)

        # ad
        div_with_add = self.browser.find_element_by_id("ad")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 6")

    def right_scenario_7(self):
        print("Right add scenario 7")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift_4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame8
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame8")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_8(self):

        print("Right add scenario 8")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_5
        iframe = right_side_div.find_element_by_id("aswift_5")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame6
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame6")
        self.browser.switch_to.frame(iframe_in_iframe)

        # ad-container
        div_with_add = self.browser.find_element_by_id("ad-container")
        self.screenshot(element=div_with_add, path=self.path)
        print("screenshot taken in scenario 8")

    def right_scenario_9(self):

        print("Right add scenario 9")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift_4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame8
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame8")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        # ad
        div_with_add = self.browser.find_element_by_id("ad")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 9")

    def right_scenario_10(self):

        print("Right add scenario 10")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift 4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame9
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame9")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adContent
        div_with_add = self.browser.find_element_by_id("adContent")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 10")

    def right_scenario_11(self):

        print("Right add scenario 11")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift 0")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame8
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame8")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_12(self):

        print("Right add scenario 12")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift_4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame5
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame5")
        self.browser.switch_to.frame(iframe_in_iframe)

        # ad-container
        div_with_add = self.browser.find_element_by_id("ad-container")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 12")

    def right_scenario_13(self):

        print("Right add scenario 13")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")
        a_tag = right_side_div.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_14(self):

        print("Right add scenario 14")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift_4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame8
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame8")
        self.browser.switch_to.frame(iframe_in_iframe)

        # ad-container
        div = self.browser.find_element_by_id("ad-container")
        self.screenshot(element=div, path=self.path)

        print("screenshot taken in scenario 14")

    def right_scenario_15(self):

        print("Right add scenario 15")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_3
        iframe = right_side_div.find_element_by_id("aswift_3")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame7
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame7")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_16(self):

        print("Right add scenario 16")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_3
        iframe = right_side_div.find_element_by_id("aswift_3")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame8
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame8")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_17(self):

        print("Right add scenario 17")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift_4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame7
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame7")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_18(self):

        print("Right add scenario 18")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_3
        iframe = right_side_div.find_element_by_id("aswift_3")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame9
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame9")
        self.browser.switch_to.frame(iframe_in_iframe)

        # au-tag au-tag-processed
        div_with_add = self.browser.find_element_by_xpath("au-tag au-tag-processed")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 18")

    def right_scenario_19(self):

        print("Right add scenario 19")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_5
        iframe = right_side_div.find_element_by_id("aswift_5")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame10
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame10")
        self.browser.switch_to.frame(iframe_in_iframe)

        # au-tag au-tag-processed
        div_with_add = self.browser.find_element_by_xpath("au-tag au-tag-processed")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 19")

    def right_scenario_20(self):

        print("Right add scenario 20")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        iframe = right_side_div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        self.screenshot(element=iframe, path=self.path)

        print("screenshot taken in scenario 20")

    def right_scenario_21(self):

        print("Right add scenario_21")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        a_tag = right_side_div.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_22(self):

        print("Right add scenario_22")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift_4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame9
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame9")
        self.browser.switch_to.frame(iframe_in_iframe)

        # ad-container
        div_with_add = self.browser.find_element_by_id("ad-container")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 22")

    def right_scenario_23(self):

        print("Right add scenario 23")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift_5")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame10
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame10")
        self.browser.switch_to.frame(iframe_in_iframe)

        # ad-container
        div_with_add = self.browser.find_element_by_id("ad-container")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 23")

    def right_scenario_24(self):

        print("Right add scenario 24")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_2
        iframe = right_side_div.find_element_by_id("aswift_2")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame9
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame9")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adContent
        div_with_add = self.browser.find_element_by_id("adContent")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 24")

    def right_scenario_25(self):

        print("Right add scenario 25")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_3
        iframe = right_side_div.find_element_by_id("aswift_3")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame7
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame7")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adContent
        div_with_add = self.browser.find_element_by_id("adContent")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 25")

    def right_scenario_26(self):

        print("Right add scenario 26")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_5
        iframe = right_side_div.find_element_by_id("aswift_5")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame9
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame9")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        # myAd
        div_with_canvas = self.browser.find_element_by_id("myAd")
        canvas = div_with_canvas.find_element_by_id("myAdCanvas")
        self.screenshot(element=canvas, path=self.path)

        print("screenshot taken in scenario 26")

    def right_scenario_27(self):

        print("Right add scenario 27")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_5
        iframe = right_side_div.find_element_by_id("aswift_5")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame9
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame9")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_28(self):

        print("Right add scenario 28")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_3
        iframe = right_side_div.find_element_by_id("aswift_3")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame9
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame9")
        self.browser.switch_to.frame(iframe_in_iframe)

        # ad-container
        div_with_add = self.browser.find_element_by_id("ad-container")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 28")

    def right_scenario_29(self):

        print("Right add scenario 29")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_6
        iframe = right_side_div.find_element_by_id("aswift_6")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame7
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame7")
        self.browser.switch_to.frame(iframe_in_iframe)

        self.screenshot(element=iframe, path=self.path)

        print("screenshot taken in scenario 29")

    def right_scenario_30(self):

        print("Right add scenario 30")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift_4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame10
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame10")
        self.browser.switch_to.frame(iframe_in_iframe)

        # au-tag au-tag-processed
        div_with_add = self.browser.find_element_by_xpath("au-tag au-tag-processed")

        iframe_in_iframe_in_iframe = div_with_add.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        # myAdButton
        a = self.browser.find_element_by_id("myAdButton")

        # myAdCanvas
        canvas = a.find_element_by_id("myAdCanvas")
        self.screenshot(element=canvas, path=self.path)

        print("screenshot taken in scenario 30")

    def right_scenario_31(self):

        print("Right add scenario 31")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_5
        iframe = right_side_div.find_element_by_id("aswift_5")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame8
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame8")
        self.browser.switch_to.frame(iframe_in_iframe)

        # ad-container
        div_with_id = self.browser.find_element_by_id("ad-container")
        self.screenshot(element=div_with_id, path=self.path)

        print("screenshot taken in scenario 31")

    def right_scenario_32(self):

        print("Right add scenario 32")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_3
        iframe = right_side_div.find_element_by_id("aswift_3")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame10
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame10")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adContent
        div_with_add = self.browser.find_element_by_id("adContent")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 32")

    def right_scenario_33(self):

        print("Right add scenario 33")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_3
        iframe = right_side_div.find_element_by_id("aswift_3")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame8
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame8")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adunit
        div_with_add = self.browser.find_element_by_id("adunit")

        # taw0
        li_with_add = div_with_add.find_element_by_id("taw0")
        self.screenshot(element=li_with_add, path=self.path)

        print("screenshot taken in scenario 33")

    def right_scenario_34(self):

        print("Right add scenario 34")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_5
        iframe = right_side_div.find_element_by_id("aswift_5")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame6
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame6")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

    def right_scenario_35(self):

        print("Right add scenario 35")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_3
        iframe = right_side_div.find_element_by_id("aswift_3")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame10
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame10")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_36(self):

        print("Right add scenario 36")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift_4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame5
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame5")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_37(self):

        print("Right add scenario 37")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_5
        iframe = right_side_div.find_element_by_id("aswift_5")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame10
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame10")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_38(self):

        print("Right add scenario 38")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_0
        iframe = right_side_div.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame9
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame9")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_39(self):

        print("Right add scenario 39")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_0
        iframe = right_side_div.find_element_by_id("aswift_5")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame8
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame8")
        self.browser.switch_to.frame(iframe_in_iframe)

        # ad-container
        div_with_add = self.browser.find_element_by_id("ad-container")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 39")

    def right_scenario_40(self):

        print("Right add scenario 40")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_5
        iframe = right_side_div.find_element_by_id("aswift_5")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame10
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame10")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adContent
        div_with_add = self.browser.find_element_by_id("adContent")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 40")

    def right_scenario_41(self):

        print("Right add scenario 41")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_6
        iframe = right_side_div.find_element_by_id("aswift_6")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame11
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame11")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_42(self):

        print("Rigth add scenario 42")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_6
        iframe = right_side_div.find_element_by_id("aswift_6")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame7
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame7")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adContent
        div_with_add = self.browser.find_element_by_id("adContent")
        self.screenshot(element=div_with_add, path=self.path)

        print("screenshot taken in scenario 42")

    def right_scenario_43(self):

        print("Right add scenario 43")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswitf 5
        iframe = right_side_div.find_element_by_id("aswift_5")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame8
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame8")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adunit
        div_with_add = self.browser.find_element_by_id("adunit")
        # taw0
        li_with_add = div_with_add.find_element_by_id("taw0")
        self.screenshot(element=li_with_add, path=self.path)

        print("screenshot taken in scenario 43")

    def right_scenario_44(self):

        print("Right add scenario 44")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift 2
        iframe = right_side_div.find_element_by_id("aswift_2")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame9
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame9")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_45(self):

        print("Right add scenario 45")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift 6
        iframe = right_side_div.find_element_by_id("aswift_6")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame7
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame7")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_46(self):

        print("Right add scenario 46")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_3
        iframe = right_side_div.find_element_by_id("aswift_3")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame9
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame9")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_47(self):

        print("Right add scenario 47")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift_4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame10
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame10")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adContent
        div_with_add = self.browser.find_element_by_id("ad-container")
        self.screenshot(element=div_with_add, path=self.path)
        print("screenshot taken in scenario 47")

    def right_scenario_48(self):

        print("Right add scenario 48")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_5
        iframe = right_side_div.find_element_by_id("aswift_5")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame8
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame8")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        # myAd
        div_with_canvas = self.browser.find_element_by_id("myAd")
        canvas = div_with_canvas.find_element_by_id("myAdCanvas")
        self.screenshot(element=canvas, path=self.path)

        print("screenshot taken in scenario 48")

    def right_scenario_49(self):

        print("Right add scenario 49")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_3
        iframe = right_side_div.find_element_by_id("aswift_3")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame10
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame10")
        self.browser.switch_to.frame(iframe_in_iframe)

        # au-tag au-tag-processed
        div_with_add = self.browser.find_element_by_xpath("//div[@Class='au-tag au-tag-processed']")
        iframe = div_with_add.find_element_by_tag_name("iframe")

        self.screenshot(element=iframe, path=self.path)
        print("screenshot taken in scenario 49")

    def right_scenario_50(self):
        print("Right add scenario 50")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_0
        iframe = right_side_div.find_element_by_id("aswift_2")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame8
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame9")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adunit
        div_with_add = self.browser.find_element_by_id("adunit")

        # taw0
        li_with_add = div_with_add.find_element_by_id("taw0")
        self.screenshot(element=li_with_add, path=self.path)
        print("screenshot taken in scenario 50")

    def right_scenario_51(self):
        print("Right add scenario 51")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_0
        iframe = right_side_div.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame8
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame8")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_52(self):
        print("scenario 56")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift_4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame10
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame10")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_53(self):
        print("scenario 57")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_6
        iframe = right_side_div.find_element_by_id("aswift_6")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame7
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame7")
        self.browser.switch_to.frame(iframe_in_iframe)

        # ad-container
        div_with_add = self.browser.find_element_by_id("ad-container")
        self.screenshot(element=div_with_add, path=self.path)
        print("screenshot taken in scenario 57")

    def right_scenario_54(self):
        print("scenario 58")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_5
        iframe = right_side_div.find_element_by_id("aswift_5")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame6
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame6")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_55(self):
        print("scenario 59")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_4
        iframe = right_side_div.find_element_by_id("aswift_4")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame5
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame5")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adunit
        div_with_add = self.browser.find_element_by_id("adunit")

        # taw0
        li_with_add = div_with_add.find_element_by_id("taw0")
        self.screenshot(element=li_with_add, path=self.path)
        print("screenshot taken in scenario 59")

    def right_scenario_56(self):
        print("Right add scenario 56")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_0
        iframe = right_side_div.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame10
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame10")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adunit
        div_with_add = self.browser.find_element_by_id("adunit")

        # taw0
        li_with_add = div_with_add.find_element_by_id("taw0")
        self.screenshot(element=li_with_add, path=self.path)

        # taw1
        li_with_add = div_with_add.find_element_by_id("taw1")
        self.screenshot(element=li_with_add, path=self.path)

        print("scrrenshot taken in scenario 56")

    def right_scenario_57(self):
        print("Right add scenario 57")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_5
        iframe = right_side_div.find_element_by_id("aswift_5")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame11
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame11")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adunit
        div_with_add = self.browser.find_element_by_id("adunit")

        # taw0
        li_with_add = div_with_add.find_element_by_id("taw0")
        self.screenshot(element=li_with_add, path=self.path)

        print("screenshot taken in scenario 57")

    def right_scenario_58(self):
        print("Right add scenario 58")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_2
        iframe = right_side_div.find_element_by_id("aswift_2")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame3
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame3")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_59(self):
        print("Right add scenario 59")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_1
        iframe = right_side_div.find_element_by_id("aswift_1")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame3
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame6")
        self.browser.switch_to.frame(iframe_in_iframe)

        body_tag_with_add = self.browser.find_element_by_tag_name("body")
        self.screenshot(element=body_tag_with_add, path=self.path)

        print("screenshot taken in scenario 59")

    def right_scenario_60(self):
        print("Right add scenario 60")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_2
        iframe = right_side_div.find_element_by_id("aswift_2")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame3
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame3")
        self.browser.switch_to.frame(iframe_in_iframe)

        # ad-container
        div_with_add = self.browser.find_element_by_id("ad-container")
        self.screenshot(element=div_with_add, path=self.path)
        print("screenshot taken in scenario 60")

    def right_scenario_61(self):
        print("Right add scenario 61")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_2
        iframe = right_side_div.find_element_by_id("aswift_2")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame5
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame5")
        self.browser.switch_to.frame(iframe_in_iframe)

        # ad-container
        div_with_add = self.browser.find_element_by_id("ad-container")
        self.screenshot(element=div_with_add, path=self.path)
        print("screenshot taken in scenario 61")

    def right_scenario_62(self):
        print("Right add scenario 62")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_1
        iframe = right_side_div.find_element_by_id("aswift_1")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame4
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame4")
        self.browser.switch_to.frame(iframe_in_iframe)

        # au-tag au-tag-processed
        div_with_frame = self.browser.find_element_by_xpath("//div[@Class='au-tag au-tag-processed']")
        iframe_in_iframe_iframe = div_with_frame.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_iframe)

        # myAd
        div_with_add = self.browser.find_element_by_id("myAd")
        a_tag = div_with_add.find_element_by_id("myAdButton")
        canvas = a_tag.find_element_by_id("myAdCanvas")
        self.screenshot(element=canvas, path=self.path)
        print("screenshot taken in scenario 62")

    def right_scenario_63(self):
        print("Right add scenario 63")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_2
        iframe = right_side_div.find_element_by_id("aswift_2")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame5
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame5")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_64(self):
        print("Right add scenario 64")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_2
        iframe = right_side_div.find_element_by_id("aswift_1")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame4
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame4")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div
        div_with_add = self.browser.find_element_by_id("google_image_div")
        a = div_with_add.find_element_by_id("aw0")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def right_scenario_65(self):
        print("Right add scenario 65")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # aswift_3
        iframe = right_side_div.find_element_by_id("aswift_3")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame4
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame4")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.screenshot(element=iframe_in_iframe_in_iframe, path=self.path)

        print("screenshot taken in scenario 65")

    def right_scenario_66(self):
        print("Right add scenario 66")

        self.browser.switch_to.default_content()

        right_side_div = self.browser.find_element_by_xpath("//div[@Class='right fright']")

        # box_image
        div = right_side_div.find_element_by_id("box_image")
        a_tag = div.find_element_by_tag_name("a_tag")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        print(src)

        return src

    def get_top_ads(self, list_adds_src):

        try:
            list_adds_src.append(self.top_add_scenario_1())
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.top_add_scenario_2())
        except Exception as ex:
            print("no add in scenario 2")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.top_add_scenario_3())
        except Exception as ex:
            print("no add in scenario 3")
            print("Exception {}".format(ex))
            pass

        try:
            list_adds_src.append(self.top_add_scenario_4())
        except Exception as ex:
            print("no add in scenario 4")
            print("Exception {}".format(ex))
            pass

    def top_add_scenario_1(self):
        print("scenario 1")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_id("branding_top_d93jgxa3")
        iframe = div.find_element_by_id("aswift_0")

        self.browser.switch_to.frame(iframe)

        # google_ads_frame1
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe)

        # adContent
        div = self.browser.find_element_by_id("adContent")
        self.screenshot(element=div, path=self.path)
        print("screenshot taken in scenario 1")

    def top_add_scenario_2(self):
        print("scenario 2")

        # branding_top_d93jgxa3
        div = self.browser.find_element_by_id("branding_top_d93jgxa3")

        iframe = div.find_element_by_tag_name("iframe")

        self.browser.switch_to.frame(iframe)

        # main-container
        div_with_add = self.browser.find_element_by_id("main-container")
        self.screenshot(element=div_with_add, path=self.path)
        print("screenshot taken in scenario 2")

    def top_add_scenario_3(self):
        print("scenario 3")

        self.browser.switch_to.default_content()

        # branding_top_d93jgxa3
        div = self.browser.find_element_by_id("branding_top_d93jgxa3")

        a = div.find_element_by_tag_name("a")
        img = a.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        print(src)

        return src

    def top_add_scenario_4(self):
        print("scenario 4")

        self.browser.switch_to.default_content()

        # branding_top_d93jgxa3
        div = self.browser.find_element_by_id("branding_top_d93jgxa3")

        iframe = div.find_element_by_tag_name("iframe")

        self.browser.switch_to.frame(iframe)
        self.screenshot(element=iframe, path=self.path)

        print("screenshot taken in scenario 4")






