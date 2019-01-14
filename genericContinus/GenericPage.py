from helperContinus.HelperClass import HelperClass

import logging
import datetime

now = datetime.datetime.now()

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('Selenium{}.log'.format(now.date()))

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class GenericPage(HelperClass):

    def __init__(self, _browser, url, path, list_iframes=[]):
        self.browser = _browser
        self.url = url
        self.list_iframe_ids = list_iframes

        HelperClass.__init__(self, path)

    def get_adds(self):

        for element in self.list_iframe_ids:
            try:
                self.get_add(element)
            except Exception as ex:
                logger.debug("exception in the process {}".format(element.get('id')))
                logger.debug("exception details: {}".format(ex))

    def get_add(self, element):
        self.browser.switch_to.default_content()

        logger.debug("element width: {}".format(element.get('width')))
        logger.debug("element height: {}".format(element.get('height')))

        iframe = self.browser.find_element_by_tag_name(element.name)
        print("# {}".format(element.name))


        if element.get('id') is not None:
            self.browser.switch_to.default_content()
            iframe = self.browser.find_element_by_id("{}".format(element.get('id')))

        self.browser.switch_to.frame(iframe)
        # print(self.browser.page_source)


        body = self.browser.find_element_by_tag_name('body')
        print("^^ {}".format(len(body.text)))

        # google_image_div
        # ad-container
        # adContent

        # str_for_xpath = "//*[@style='width:{};height:{};']".format(element.get('width'), element.get('height'))
        # print(str_for_xpath)
        # adContent

        logger.debug("Before screenshot {} ".format(element.get('id')))

        self.screenshot(body, self.path, self.browser)
        logger.debug("screenshot taken {}".format(element.get('id')))







