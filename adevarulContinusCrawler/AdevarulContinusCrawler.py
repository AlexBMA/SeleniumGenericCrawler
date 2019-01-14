
from selenium.webdriver.firefox.options import Options
import re
from urllib.parse import urljoin
import os
import shutil
from selenium import webdriver
from bs4 import BeautifulSoup

from adevarullPack.AdevarulAddsArticlePage import AdevarulAddsArticlePage
from adevarullPack.AdevarulAddsCategoryPage import AdevarulAddsCategoryPage
from adevarullPack.AdevarulAddsHomePage import AdevarulAddsHomePage
from adevarullPack.AdevarulAddsPhotoPage import AdevarulAddPhotoPage
from adevarullPack.AdevarulAddsVideoPage import AdevarulAddVideoPage

from helperContinus.HelperClassExtractor import HelperClassExtraction


class AdevarulCrawler:
    name = "news_adevarul"

    pageReq = 0
    imgReq = 0
    start_urls = [
        'http://adevarul.ro/'
     ]
    start_url = "http://adevarul.ro/"

    list_category_adevarul = ["http://adevarul.ro/news/",
                              "http://adevarul.ro/economie/",
                              "http://adevarul.ro/eveniment/",
                              "http://adevarul.ro/politica/",
                              "http://adevarul.ro/societate/",
                              "http://adevarul.ro/sport/",
                              "http://adevarul.ro/international/",
                              "http://adevarul.ro/educatie/",
                              "http://adevarul.ro/tech/",
                              "http://adevarul.ro/life&style/",
                              "http://adevarul.ro/sanatate/",
                              "http://adevarul.ro/cultura/",
                              "http://adevarul.ro/entertainment/",
                              "http://adevarul.ro/locale/iasi/",
                              "http://adevarul.ro/locale/botosani/",
                              "http://adevarul.ro/locale/vaslui/",
                              "http://adevarul.ro/locale/suceava/",
                              "http://adevarul.ro/locale/piatra-neamt/",
                              "http://adevarul.ro/locale/bacau/",
                              "http://adevarul.ro/moldova/",
                              "http://adevarul.ro/locale/bistrita/",
                              "http://adevarul.ro/locale/cluj-napoca/",
                              "http://adevarul.ro/locale/baia-mare/",
                              "http://adevarul.ro/locale/zalau/",
                              "http://adevarul.ro/locale/satu-mare/",
                              "http://adevarul.ro/locale/oradea/",
                              "http://adevarul.ro/locale/arad/",
                              "http://adevarul.ro/locale/timisoara/",
                              "http://adevarul.ro/locale/alba-iulia/",
                              "http://adevarul.ro/locale/hunedoara/",
                              "http://adevarul.ro/locale/resita/",
                              "http://adevarul.ro/locale/targu-mures/",
                              "http://adevarul.ro/locale/sibiu/",
                              "http://adevarul.ro/locale/brasov/",
                              "http://adevarul.ro/locale/targu-jiu/",
                              "http://adevarul.ro/locale/turnu-severin/",
                              "http://adevarul.ro/locale/ramnicu-valcea/",
                              "http://adevarul.ro/locale/craiova/",
                              "http://adevarul.ro/locale/slatina/",
                              "http://adevarul.ro/locale/targoviste/",
                              "http://adevarul.ro/locale/pitesti/",
                              "http://adevarul.ro/locale/ploiesti/",
                              "http://adevarul.ro/locale/alexandria/",
                              "http://adevarul.ro/locale/giurgiu/",
                              "http://adevarul.ro/news/bucuresti/",
                              "http://adevarul.ro/locale/calarasi/",
                              "http://adevarul.ro/locale/focsani/",
                              "http://adevarul.ro/locale/buzau/",
                              "http://adevarul.ro/locale/galati/",
                              "http://adevarul.ro/locale/braila/",
                              "http://adevarul.ro/locale/slobozia/",
                              "http://adevarul.ro/locale/tulcea/",
                              "http://adevarul.ro/locale/constanta/",
                              "http://adevarul.ro/news/eveniment/",
                              "http://adevarul.ro/news/politica/",
                              "http://adevarul.ro/news/societate/",
                              "http://adevarul.ro/news/sport/",
                              "http://adevarul.ro/news/bucuresti/",
                              "http://adevarul.ro/news/stiri-ciudate/",
                              "http://adevarul.ro/news/festivalul-george-enescu/",
                              "http://adevarul.ro/continut/stiri/adevarul-despre-romania",
                              "http://adevarul.ro/economie/stiri-economice/",
                              "http://adevarul.ro/economie/bani/",
                              "http://adevarul.ro/economie/afaceri/",
                              "http://adevarul.ro/economie/business-international/",
                              "http://adevarul.ro/economie/imobiliare/",
                              "http://adevarul.ro/economie/investitii/",
                              "http://adevarul.ro/continut/stiri/banii-tai",
                              "http://adevarul.ro/international/europa/",
                              "http://adevarul.ro/international/in-lume/",
                              "http://adevarul.ro/international/asia/",
                              "http://adevarul.ro/international/statele-unite/",
                              "http://adevarul.ro/international/rusia/",
                              "http://adevarul.ro/international/foreign-policy/",
                              "http://adevarul.ro/educatie/prescolar/",
                              "http://adevarul.ro/educatie/scoala/",
                              "http://adevarul.ro/educatie/universitar/",
                              "http://adevarul.ro/educatie/studii-in-strainatate/",
                              "http://adevarul.ro/tech/stiinta/",
                              "http://adevarul.ro/tech/mobile/",
                              "http://adevarul.ro/tech/gadget/",
                              "http://adevarul.ro/tech/internet/",
                              "http://adevarul.ro/tech/retele-sociale/",
                              "http://adevarul.ro/tech/gaming/",
                              "http://adevarul.ro/tech/black-friday/",
                              "http://adevarul.ro/life-style/stil-de-viata/",
                              "http://adevarul.ro/life-style/bucatarie/",
                              "http://adevarul.ro/life-style/travel/",
                              "http://adevarul.ro/life-style/moda/",
                              "http://adevarul.ro/life-style/parinti/",
                              "http://adevarul.ro/life-style/dragoste-si-sex/",
                              "http://adevarul.ro/life-style/auto/",
                              "http://adevarul.ro/sanatate/medicina/",
                              "http://adevarul.ro/sanatate/dieta-fitness/",
                              "http://adevarul.ro/sanatate/medicina-naturista/",
                              "http://adevarul.ro/sanatate/minte-sanatoasa/",
                              "http://adevarul.ro/sanatate/dormit/",
                              "http://adevarul.ro/sanatate/politici-bani/",
                              "http://adevarul.ro/cultura/arte/",
                              "http://adevarul.ro/cultura/carti/",
                              "http://adevarul.ro/cultura/teatru/",
                              "http://adevarul.ro/cultura/istorie/",
                              "http://adevarul.ro/cultura/spiritualitate/",
                              "http://adevarul.ro/cultura/patrimoniu/",
                              "http://adevarul.ro/entertainment/celebritati/",
                              "http://adevarul.ro/entertainment/muzica/",
                              "http://adevarul.ro/entertainment/film/",
                              "http://adevarul.ro/entertainment/tv/",
                              "http://adevarul.ro/entertainment/comedy/"
                              ]

    photoPage = False
    videoPage = False

    adevarulPhotoCenterUrl ="http://adevarul.ro/foto-center/"
    adevarulVideoCenterUrl ="http://adevarul.ro/video-center/"

    httpPrefix = "http:"
    httpsPrefix = "https:"

    deny_list = [
        'http://adevarul.ro/intrebari-frecvente',
        'http://adevarul.ro/profil',
        'http://adevarul.ro/politica-cookies',
        'http://adevarul.ro/intrebari-frecvente',
        'http://adevarul.ro/blogs'
        'http://adevarul.ro/continut',
        'http://adevarul.ro/jobs',
        'http://adevarul.ro/politica-confidentialitate',
        'http://adevarul.ro/codul-deontologic',
        'http://adevarul.ro/termeni-si-conditii'
    ]

    deny_domains_list = [
        'm.adevarul.ro',
        'abonamente.adevarul.ro'
    ]

    allow_domains_list = [
        'adevarul.ro'
    ]

    def run(self, path, path_normal_img):
        # you can revisit your portal urls in this method
        print("HERE $$$")

        options = Options()
        options.add_argument("--headless")

        extraction_helper = HelperClassExtraction(start_url=self.start_url, deny_list=self.deny_list)

        for url in self.start_urls:

            browser = webdriver.Firefox(firefox_options=options)
            browser.implicitly_wait(7)

            try:
                browser.get(url)

                set_src = extraction_helper.my_link_extractor(browser=browser)

                normal_img_src_list = extraction_helper.extract_regular_images_src_list(browser=browser,
                                                                                        http_prefix=self.httpPrefix,
                                                                                        https_prefix=self.httpsPrefix)
                extraction_helper.extract_img_from_src_list(list_src=normal_img_src_list, path=path_normal_img)

                rez_adds = self.extract_images_and_save(url=url, browser=browser, path=path)
                extraction_helper.extract_img_from_src_list(list_src=rez_adds, path=path)

                self.start_urls += self.start_urls + list(set_src)
                self.start_urls = list(set(self.start_urls))

                browser.close()

            except Exception as ex:
                print("Exception {}".format(ex))

        print("HERE ###")

    def extract_images_and_save(self, url, browser, path):

        if self.start_urls[0] == url:
            print("here in ads home page")
            home_page_ads = AdevarulAddsHomePage(path=path)
            return home_page_ads.get_home_page_ads(browser)

        if url in self.list_category_adevarul:
            print("here in ads category pages")
            category_ads = AdevarulAddsCategoryPage(browser, path=path)
            return category_ads.get_category_adds()

        if url == self.adevarulPhotoCenterUrl:
            print("here in ads photo pages")
            photo_ads = AdevarulAddPhotoPage(browser, path=path)
            return photo_ads.get_adds()

        if url == self.adevarulVideoCenterUrl:
            print("here in ads video pages")
            video_ads = AdevarulAddVideoPage(browser, path=path)
            return video_ads.get_adds()
        else:
            article_ads = AdevarulAddsArticlePage(browser, path=path)
            return article_ads.get_article_adds()






