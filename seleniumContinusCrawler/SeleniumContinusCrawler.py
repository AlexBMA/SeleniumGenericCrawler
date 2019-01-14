from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from genericContinus.GenericPage import GenericPage

from helperContinus.HelperClassExtractor import HelperClassExtraction
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


class NewsCrawler:
    name = "news_spider_generic2"

    pageReq = 0
    imgReq = 0

    start_urls = [
        "https://www.thetimes.co.uk/",
        "https://www.telegraph.co.uk/",
        "https://www.theguardian.com/",
        "https://www.lesechos.fr/",
        "https://www.la-croix.com/",
        "http://www.liberation.fr/",
        "https://www.lefigaro.fr/",
        "https://www.lemonde.fr/",
        "http://www.sueddeutsche.de",
        "http://www.faz.net",
        "https://www.welt.de",
        "https://www.handelsblatt.com",
        "https://www.corriere.it/",
        "http://www.repubblica.it/",
        "http://www.lastampa.it/",
        "http://www.ilsole24ore.com",
        "https://elpais.com/",
        "http://www.elmundo.es",
        "https://www.abc.es",
        "https://www.wsj.com/",
        "https://www.washingtonpost.com/",
        "https://www.nytimes.com/",
        "https://pythontips.com/tag/python-patreon/",
        "https://www.speedtest.net/",
        "https://www.independent.co.uk/?CMP=ILC-refresh"
    ]

    allow_domain = [
        # 'edition.cnn.com'
    ]

    deny_domain = [
        'plus.google.com',
        'linkedin.com',
        'facebook.com',
        'twitter.com',
        'paypal.com',
        'instagram.com',
        'm.+.+'
    ]

    deny_list = [
        '/about',
        '/privacy',
        '/cookie',
        '/terms',
        '/newsletters'
        '/weather',
        '/profiles',
        '/accessibility',
        '/vr',
        '/video',
        '/contact',
        '/transcripts',
        '/instagram',
        '/facebook',
        '/help',
        '/twitter',
        '/copyright'
    ]

    httpPrefix = "http:"
    httpPrefix_2 = "http:/"
    httpPrefix_3 = "http://"
    httpsPrefix = "https:"
    httpsPrefix_2 = "https:/"
    httpsPrefix_3 = "https://"

    def run(self, path_adds):
        # you can revisit your portal urls in this method
        # make a link extractor

        print("HERE $$$")

        options = Options()
        options.add_argument("--headless")

        nr = 1

        extraction_helper = HelperClassExtraction(start_url=self.start_urls[0], deny_list=self.deny_list)

        path_regular_images = '/home/alex2/PycharmProjects/newscrapy/generic page/regular img/'

        duplicate_helper = HelperClass(path=path_adds)

        for url in self.start_urls:
            #print("Number:{}".format(nr))
            browser = webdriver.Firefox(firefox_options = options)
            browser.set_page_load_timeout(7)
            browser.implicitly_wait(7)

            logger.debug("Page number: {}".format(nr))
            try:
                browser.get(url)

                #set_src = extraction_helper.my_link_extractor_no_generic(browser=browser)

                self.extract_add_images_and_save_them(url=url, browser=browser, path_adds=path_adds)
                #duplicate_helper.eliminate_duplicated_saved_picture(path=path_adds)

                #self.start_urls += self.start_urls + list(set_src)
                #self.start_urls = list(set(self.start_urls))

                browser.close()
                nr += 1
            except Exception as ex:
                print("Exception {}".format(ex))

        print("HERE ###")

    def extract_add_images_and_save_them(self, url, browser, path_adds):

        logger.debug("Link where the add images are extracted: " + url)

        browser.switch_to.default_content()
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        list_iframe = []

        dim = webdriver.Firefox.get_window_size(browser)

        youtube_src = "https://youtube.com/"

        list_google_add_id =[
             "google_ads_iframe_",
             "google_decrypt_frame_",
             "utif_"
        ]

        for link in soup.find_all('iframe'):

            self.log_details_for_iframe(link)

            height = link.get('height')
            width = link.get('width')
            id_link = link.get('id')
            src = link.get('src')

            if id_link is not None:

                if self.test_id(id_link, list_google_add_id) is True:

                    if height is not None and width is not None:

                        if height.find("px") > -1:
                            height = height[0:len(height) - 2]

                        if width.find("px") > -1:
                            width = width[0:len(width) - 2]

                        if height.find("%") > -1:
                            height = dim['height']

                        if width.find("%") > -1:
                            width = dim['width']

                        if height is not "" and width is not "" and float(height) > 10.0 and float(width) > 10.0:

                            if src is not None and src.startswith(youtube_src) is False:
                                #print("here with youtube src {}".format(src))
                                list_iframe.append(link)

                            if src is None:
                                list_iframe.append(link)

        self.log_google_add_iframes(list_iframe)

        add_class = GenericPage(browser, url=url, path=path_adds, list_iframes=list_iframe)

        add_class.get_adds()

    def test_id(self, id, list_google_ids):
        #print("##")
        for item in list_google_ids:
            if id.startswith(item) is True:
                #print("{} in {}".format(item, id))
                return True
        return False

    def log_google_add_iframes(self, list_iframe):
        logger.debug("Size of list : {} ".format(len(list_iframe)))
        logger.debug("Google list:")
        for elem in list_iframe:
            logger.debug(elem)
        logger.debug("")

    def log_details_for_iframe(self, link):
        logger.debug(" ")
        logger.debug(link)
        logger.debug("{} name:{} id:{} h:{} w:{}".format("Element",
                                                  link.name,
                                                  link.get('id'),
                                                  link.get('height'),
                                                  link.get('width')))

