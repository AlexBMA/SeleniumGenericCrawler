from helperContinus.HelperClass import HelperClass
import requests


class ScreenshotPage(HelperClass):

    def __init__(self, _browser, path):
        self.browser = _browser

        HelperClass.__init__(self, path)

    def get_adds(self):

        try:
            self.get_add()
        except Exception as ex:
            print("exception details: {}".format(ex))

        try:
            self.get_add_2()
        except Exception as ex:
            print("exception details ## : {}".format(ex))

    def get_add_2(self):

        print(self.browser.current_url)
        self.browser.switch_to.default_content()

        img = self.browser.find_element_by_tag_name("img")

        src = img.get_attribute("src")

        response = requests.get(src, stream=True)

        print(response)

        self.screenshot_jpg(response, element=None, path=self.path)

        del response

        print("screenshot taken ")

    def get_add(self):

        print(self.browser.current_url)
        self.browser.switch_to.default_content()

        img = self.browser.find_element_by_tag_name("img")

        self.screenshot(element=img, path=self.path, browser=self.browser)
        print("regular img screenshot taken")


