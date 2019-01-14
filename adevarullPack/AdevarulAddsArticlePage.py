from PIL import Image
from io import BytesIO
from random import randint

import hashlib

from helperContinus.HelperClass import HelperClass


class AdevarulAddsArticlePage(HelperClass):

    list_add_screenshot = []

    def __init__(self, _browser, path):
        self.browser = _browser

        HelperClass.__init__(self, path)

    def get_article_adds(self):

        list_add_links = []

        self.get_top_add(list_add_links)

        self.get_add_pub_top(list_add_links)

        self.get_add_article_content_clearfix(list_add_links)

        try:
            list_add_links.append(self.Mid_add_scenario_1())
        except Exception as ex:
            print("no add in scenario 1 ")
            print("exception: {}".format(ex))
            pass

        try:
            list_add_links.append(self.Mid_add_scenario_2())
        except Exception as ex:
            print("no add in scenario 2")
            print("exception: {}".format(ex))
            pass

        self.get_left_side_add(list_add_links)

        self.get_bottom_add(list_add_links)

        #self.side_bar_adds(list_add_links)

        #print(list_add_links)
        #print(self.list_add_screenshot)
        return self.eliminate_duplicate(list_add_links)

    def get_add_article_content_clearfix(self, list_add_links):
        try:
            list_add_links.append(self.add_article_content_clearfix_scenario_1())
            return
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_links.append(self.add_article_content_clearfix_scenario_2())
            return
        except Exception as ex:
            print("no add in scenario 2")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_links.append(self.add_article_content_clearfix_scenario_3())
            return
        except Exception as ex:
            print("no add in scenario 3")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_links.append(self.add_article_content_clearfix_scenario_4())
            return
        except Exception as ex:
            print("no add in scenario 4")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_links.append(self.add_article_content_clearfix_scenario_5())
            return
        except Exception as ex:
            print("no add in scenario 5")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_links.append(self.add_article_content_cleafix_scenario_6())
            return
        except Exception as ex:
            print("no add in scenario 6")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_links.append(self.add_article_content_clearfix_scenario_7())
            return
        except Exception as ex:
            print("no add in scenario 7")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_links.append(self.add_article_content_clearfix_scenario_8())
            return
        except Exception as ex:
            print("no add in scenario 8")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_links.append(self.add_article_content_cleafix_scenario_9())
            return
        except Exception as ex:
            print("no add in scenario 9")
            print("Exception {}".format(ex))
            pass

    def get_add_pub_top(self, list_add_links):
        try:
            list_add_links.append(self.add_pub_top_scenario_1())
            return
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))

        try:
            list_add_links.append(self.add_pub_top_scenario_2())
            return
        except Exception as ex:
            print("no add in scenario 2")
            print("Exception {}".format(ex))
            pass

        try:
            list_add_links.append(self.add_pub_top_scenario_3())
            return
        except Exception as ex:
            print("no add in scenario 3")
            print("Exception {}".format(ex))
            pass

    """
    def eliminate_duplicate(self, list_add_links):

        black_gif = "http://content.zontera.com/Storage/0_0/blank.gif"

        secound_add_list = []
        for elem in list_add_links:
            if elem is not None and isinstance(elem, str) and elem != black_gif:
                secound_add_list.append(elem)

        if len(secound_add_list) > 0:
            secound_add_list = set(secound_add_list)

        print(secound_add_list)
        return secound_add_list
    """
    def side_bar_adds(self, list_add_links):
        # site-sidebar
        try:
            list_add_links.append(self.scenario29_article_page())
        except Exception as ex:
            print("no add in scenario 29")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_links.append(self.scenario30_article_page())
        except Exception as ex:
            print("no add in scenario 30")
            print("Exception {}".format(ex))
            pass

    def scenario29_article_page(self):

        print("scenario 29")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_id("site-sidebar")

        img = div.find_element_by_tag_name("img")
        src = img.get_attribute("src")

        print(src)

        return src

    def scenario30_article_page(self):

        print("scenario 30")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_id("site-sidebar")

        # aswift_0
        iframe = div.find_element_by_id("aswift_0")
        self.browser.switch_in_frame(iframe)

        # google_ads_frame1
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe)

        # X1Img0B
        div_add = self.browser.find_element_by_id("X1Img0B")
        img = div_add.find_element_by_tag_name("img")

        src = img.get_attribute("src")

        print(src)

        return src

    def get_left_side_add(self, list_add_links):
        try:
            list_add_links.append(self.left_side_scenario_1())
            return
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_links.append(self.left_side_scenario_2())
            return
        except Exception as ex:
            print("no add in scenario 2")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_links.append(self.left_side_scenario_3())
            return
        except Exception as ex:
            print("no add in scenario 3")
            print("Exception {}".format(ex))
            pass

    def left_side_scenario_1(self):

        print("Left side scenario 1")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_id("adh_sideAdvert")
        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        iframe_in_iframe = self.browser.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("google_image_div")
        a_tag = div_with_add.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def left_side_scenario_2(self):

        print("Left side scenario 2")

        self.browse.switch_to.default_content()

        div =  self.browse.find_element_by_id("adh_sideAdvert")
        iframe = div.find_element_by_tag_name("aswift_0")
        self.browse.switch_to.frame(iframe)

        iframe_in_iframe = self.browse.find_element_by_id("google_ads_frame1")
        self.browse.switch_to.frame(iframe_in_iframe)

        div_with_add = self.browse.find_element_by_id("google_image_div")
        a_tag = div_with_add.find_element_by_id("aw0")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)
        return src

    def left_side_scenario_3(self):

        print("Left side scenario 3")

        self.browse.switch_to.default_content()

        # adh_sideAdvert
        div = self.browse.find_element_by_id("adh_sideAdvert")

        # aswift_0
        iframe_in_iframe = div.find_element_by_id("aswift_0")
        self.browse.switch_to.frame(iframe_in_iframe)

        # google_ads_frame1
        iframe_in_iframe_in_iframe = self.browse.find_element_by_id("google_ads_frame1")
        self.browse.switch_to.frame(iframe_in_iframe_in_iframe)

        # google_image_div
        iframe_in_iframe_in_iframe_in_iframe = self.browse.switch_to.frame("google_image_div")
        self.browse.switch_to.frame(iframe_in_iframe_in_iframe_in_iframe)

        # aw0
        a_tag = self.browse.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)
        return src

    def get_bottom_add(self, list_add_links):

        self.get_bottom_add_google_add_frame_3(list_add_links)

        self.get_bottom_add_google_add_frame_6(list_add_links)

        try:
            list_add_links.append(self.bottom_add_scenario_1())
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))

    def get_bottom_add_google_add_frame_3(self, list_add_links):
        try:
            list_add_links.append(self.bottom_add_frame_3_scenario_1())
            return
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_links.append(self.bottom_add_frame_3_scenario_2())
            return
        except Exception as ex:
            print("no add in scenario 2")
            print("Exception {}".format(ex))
        try:
            list_add_links.append(self.bottom_add_frame_3_scenario_3())
            return
        except Exception as ex:
            print("no add in scenario 3")
            print("Exception {}".format(ex))

    def get_bottom_add_google_add_frame_6(self, list_add_links):
        try:
            list_add_links.append(self.bottom_add_frame_6_scenario_1())
            return
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))
        try:
            list_add_links.append(self.bottom_add_frame_6_scenario_2())
            return
        except Exception as ex:
            print("no add in scenario 2")
            print("Exception {}".format(ex))
            pass

    def bottom_add_scenario_1(self):

        print("Bottom add scenario 1")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_id("tab-articol")

        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe)

        # ad
        div_with_add = self.browser.find_element_by_id("ad")

        self.screenshot(element=div_with_add, path=self.path, browser=self.browser)

        print("screenshot taken in scenario 1")


    def bottom_add_frame_6_scenario_1(self):

        print("Bottom add frame 6 scenario 1")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_id("tab-articol")

        iframe = div.find_element_by_id("aswift_3")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame6
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame6")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_image_div

        div_with_add = self.browser.find_element_by_id("google_image_div")

        # aw0
        a_href = div_with_add.find_element_by_id("aw0")
        img = a_href.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)
        return src


    def bottom_add_frame_3_scenario_3(self):

        print("scenario 26")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_id("tab-articol")

        iframe_in_div = div.find_element_by_id("aswift_2")
        self.browser.switch_to.frame(iframe_in_div)

        iframe_in_iframe = self.browser.switch_to.frame("google_ads_frame3")
        self.browser.switch_to.frame(iframe_in_iframe)

        div_wtih_add = self.browser.find_element_by_id("ads")

        li_with_add = div_wtih_add.find_element_by_id("taw0")

        self.screenshot(element=li_with_add, path=self.path, browser=self.browser)

        print("screenshot taken in scenario 26")


    def bottom_add_frame_3_scenario_2(self):

        print("scenario 25")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_id("tab-articol")

        iframe_in_div = div.find_element_by_id("aswift_2")
        self.browser.switch_to.frame(iframe_in_div)

        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame3")
        self.browser.switch_to.frame(iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("adunit")

        li_with_add = div_with_add.find_element_by_id("taw0")

        self.screenshot(element=li_with_add, path=self.path, browser=self.browser)

        print("screenshot taken in scenario 25")


    def bottom_add_frame_6_scenario_2(self):

        print("Bottom add frame 6 scenario 2")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_id("tab-articol")

        iframe = div.find_element_by_id("aswift_3")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame6
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame6")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        # ad
        div_with_ad = self.browser.find_element_by_id("ad")

        self.screenshot(element=div_with_ad, path=self.path, browser=self.browser)

        print("screenshot taken in scenario 2")


    def bottom_add_frame_3_scenario_1(self):

        print("Bottom add frame scenario 1")

        self.browser.switch_to.default_content()

        # tab-articol

        div = self.browser.find_element_by_id("tab-articol")

        iframe_in_div = div.find_element_by_id("aswift_2")
        self.browser.switch_to.frame(iframe_in_div)

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

    def get_top_add(self, list_add_links):
        try:
            list_add_links.append(self.top_add_scenario_1())
        except Exception as ex:
            print("no add in scenario 1")
            print("Exception {}".format(ex))
            pass
        try:
            list_add_links.append(self.top_add_scenario_2())
        except Exception as ex:
            print("no add in scenario 2")
            print("Exception {}".format(ex))
            pass

        """
        try:
            list_add_links.append(self.scenario7_article_page())
        except Exception:
            print("no add in scenario 7")
            pass
        """

        try:
            list_add_links.append(self.top_add_scenario_3())
        except Exception as ex:
            print("no add in scenario 3")
            print("Exception {}".format(ex))
            pass

    def top_add_scenario_1(self):
        print("Top add scenario 1")

        self.browser.switch_to.default_content()

        header_with_add = self.browser.find_element_by_id("top")
        # iframe -> iframe id = aswift_0 -> iframe -id = google_ads_frame1 > div id = google_image_div -> img

        iframe = header_with_add.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        iframe_in_iframe = self.browser.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe_in_iframe)
        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("google_image_div")
        print("here in scenario 4")
        img = div_with_add.find_element_by_tag_name("img")

        src = img.get_attribute("src")
        print(src)

        return src

    def add_article_content_clearfix_scenario_3(self):

        print("Add article scenario 3")

        self.browser.switch_to.default_content()

        header_with_add = self.browser.find_element_by_id("pagina-articol")
        div_in_div = header_with_add.find_element_by_xpath("//div[@Class='article-content clearfix']")
        # iframe -> iframe id = aswift_0 -> iframe -id = google_ads_frame1 > div id = google_image_div -> img

        iframe = div_in_div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        iframe_in_iframe = self.browser.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("google_image_div")
        img = div_with_add.find_element_by_tag_name("img")

        src = img.get_attribute("src")
        print(src)

        return src

    def top_add_scenario_2(self):
        print("Top add scenario 2")

        self.browser.switch_to.default_content()

        header_with_add = self.browser.find_element_by_id("top")
        # iframe -> iframe id = aswift_0 -> iframe id = google_ads_frame1 -> div id = X1Img0B-> img

        iframe = header_with_add.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        iframe_in_iframe = self.browser.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("X1Img0B")
        print("here in scenario 6")
        img = div_with_add.find_element_by_tag_name("img")

        src = img.get_attribute("src")
        print(src)

        return src

    def top_add_scenario_3(self):

        print("Top add scenario 3")

        self.browser.switch_to.default_content()

        header_with_add = self.browser.find_element_by_id("top")
        # iframe -> iframe id = aswift_0 -> iframe id = google_ads_frame1 -> iframe -> svg  id = A

        iframe = header_with_add.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        iframe_in_iframe = self.browser.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        iframe_in_iframe_in_iframe_in_frame = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe_in_frame)

        print("here in scenario 8")
        svg = self.browser.find_element_by_tag_name("svg")
        self.screenshot(element=svg, path=self.path, browser=self.browser)
        print("screenshot taken in scenario 8")

    def add_pub_top_scenario_1(self):

        print("Add pub scenario 1")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_class_name("pub_top")
        sub_div = div.find_element_by_tag_name("div")
        sub_div_div = sub_div.find_element_by_class_name("div")
        img = sub_div_div.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def add_pub_top_scenario_2(self):

        print("Add pub scenario 2")

        self.browser.switch_to.default_content()

        div_with_add = self.browser.find_element_by_class_name("pub_top")
        iframe = div_with_add.find_element_by_tag_name(div_with_add)
        self.browser.switch_to.frame(iframe)

        iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("page1")
        self.screenshot(element=div_with_add, path=self.path, browser=self.browser)

        print("screenshot taken in scenario 2")

    def add_pub_top_scenario_3(self):

        print("Add pub scenario 3")

        self.browser.switch_to.default_content()

        # div -> iframe -> div -> a -> img

        div_with_add = self.browser.find_element_by_class_name("pub_top")
        iframe = div_with_add.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        div = self.browser.find_element_by_tag_name("div")
        a_tag = div.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def Mid_add_scenario_2(self):
        print("Mid add scenario 2")

        self.browser.switch_to.default_content()
        # div with id = ZTRHtml2B -> a -> img

        div_with_add = self.browser.find_element_by_id("ZTRHtml2B")
        a_tag = div_with_add.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def add_article_content_clearfix_scenario_1(self):

        print("Add article scenario 1")

        self.browser.switch_to.default_content()
        # iframe -> iframe -> iframe -> div id = google_image_div -> a -> img

        div = self.browser.find_element_by_id("pagina-articol")

        # article-content clearfix
        div_in_div = div.find_element_by_xpath("//div[@Class='article-content clearfix']")

        iframe = div_in_div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        # google_image_div
        div_google = self.browser.find_element_by_id("google_image_div")
        a_tag = div_google.find_element_by_tag_name("a")
        img = a_tag.find_element_by_tag_name("img")
        src = img.get_attribute("src")
        print(src)

        return src

    def add_article_content_clearfix_scenario_2(self):

        print("Add article scenario 2 ")

        self.browser.switch_to.default_content()
        # iframe -> iframe -> iframe -> div id = adContent

        div_with_add = self.browser.find_element_by_id("pagina-articol")

        div_in_div = div_with_add.find_element_by_xpath("//div[@Class='article-content clearfix']")

        iframe = div_in_div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        # adContent
        div_google_variant = self.browser.find_element_by_id("adContent")

        self.screenshot(element=div_google_variant, path=self.path, browser=self.browser)

        print("screenshot taken in scenario 2")


    def scenario5_article_page(self):
        print("scenario 5")

        self.browser.switch_to.default_content()

        header_with_add = self.browser.find_element_by_id("pagina-articol")
        div_in_div = header_with_add.find_element_by_xpath("//div[@Class='article-content clearfix']")
        # iframe -> iframe id = aswift_0 -> iframe -id = google_ads_frame1 > div id = google_image_div -> img

        iframe = div_in_div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        iframe_in_iframe = self.browser.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("google_image_div")
        img = div_with_add.find_element_by_tag_name("img")

        src = img.get_attribute("src")
        print(src)

        return src

    def add_article_content_clearfix_scenario_4(self):

        print("Add article content scenario 4")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_xpath("//div[@Class='article-content clearfix']")
        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        iframe_in_iframe = self.browser.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_2 = self.browser.find_element_by_id("root_template_div")
        iframe_in_iframe_in_iframe_in_iframe = div_2.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe_in_iframe)

        div_with = self.browser.find_element_by_id("page1")

        self.screenshot(element=div_with, path=self.path, browser=self.browser)

        print("screenshot taken in scenario 4")

    def add_article_content_clearfix_scenario_5(self):

        print("Add article content scenario 5")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_xpath("//div[@Class='article-content clearfix']")
        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        iframe_in_iframe = self.browser.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("adContent")
        self.screenshot(element=div_with_add, path=self.path, browser=self.browser)

        print("screenshot taken in scenario 5")

    def add_article_content_cleafix_scenario_6(self):

        print("Add article content scenario 6")

        self.browser.switch_to.default_content()
        div = self.browser.find_element_by_xpath("//div[@Class='article-content clearfix']")

        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        iframe_in_iframe = self.browser.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_with_add = self.browser.find_element_by_tag_name("div")
        self.screenshot(element=div_with_add, path=self.path, browser=self.browser)

        print("screenshot taken in scenario 6")


    def Mid_add_scenario_1(self):

        print("Mid add scenario 1")

        self.browser.switch_to.default_content()

        # ZTRInReadVideo1D

        div = self.browser.find_element_by_id("ZTRInReadVideo1D")
        video = div.find_element_by_tag_name("video")

        self.screenshot(element=video, path=self.path,browser=self.browser)

        print("screenshot in article 1")


    def add_article_content_clearfix_scenario_7(self):

        print("Add article content scenario 7")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_xpath("//div[@Class='article-content clearfix']")

        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        # aswift_0
        iframe_in_iframe = self.browser.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_ads_frame1
        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_2 = self.browser.find_element_by_tag_name("div")
        iframe_in_iframe_in_iframe_in_iframe = div_2.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe_in_iframe)

        # awc_content
        div_add_2 = self.browser.find_element_by_class_name("awc_content")
        self.screenshot(element=div_add_2, path=self.path, browser=self.browser)

        print("screenshot in article 7")

    def add_article_content_clearfix_scenario_8(self):

        print("Add article content scenario 8")

        self.browser.switch_to.default_content()

        div = self.browser.find_element_by_xpath("//div[@Class='article-content clearfix']")
        iframe = div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        # aswift_0
        iframe_in_iframe = self.browser.find_element_by_id("aswift_0")
        self.browser.switch_to.frame(iframe_in_iframe)

        # google_ads_frame1
        iframe_in_iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_2 = self.browser.find_element_by_tag_name("div")
        iframe_in_iframe_in_iframe_in_iframe = div_2.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe_in_iframe)

        div_3 = self.browser.find_element_by_id("id")
        self.screenshot(element=div_3, path=self.path, browser=self.browser)

        print("screenshot in article 8")

    def add_article_content_cleafix_scenario_9(self):

        print("Add article content scenario 9")

        self.browser.switch_to.default_content()

        # pagina-articol
        div = self.browser.find_element_by_id("pagina-articol")
        div_in_div = div.find_element_by_xpath("//div[@Class='article-content clearfix']")

        iframe = div_in_div.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe)

        # google_ads_frame1
        iframe_in_iframe = self.browser.find_element_by_id("google_ads_frame1")
        self.browser.switch_to.frame(iframe_in_iframe)

        iframe_in_iframe_in_iframe = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to.frame(iframe_in_iframe_in_iframe)

        div_with_add = self.browser.find_element_by_id("ad")

        self.screenshot(element=div_with_add, path=self.path, browser=self.browser)

        print("screenshot taken in scenario 9")








