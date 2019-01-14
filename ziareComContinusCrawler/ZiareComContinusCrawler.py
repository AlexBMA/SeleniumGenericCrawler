from selenium.webdriver.firefox.options import Options
from selenium import webdriver

from ziareComPack.ziareComAddCategoryPage import ZiareComAddsCategoryPage
from ziareComPack.ziareComAddHomePage import ZiareComAddsHomePage
from ziareComPack.ziareComAddArticlePage import ZaireComAddsArticlePage

from helperContinus.HelperClassExtractor import HelperClassExtraction


class ZiarulComCrawler:
    name = "news_ziareCom"

    pageReq = 0
    imgReq = 0
    start_urls = [
        'http://www.ziare.com'
     ]
    start_url = "http://www.ziare.com"

    list_category_ziare_com = ["http://www.ziare.com/politic/",
                               "http://www.ziare.com/business/",
                               "http://www.ziare.com/sport/",
                               "http://www.ziare.com/lifeshow/"
                               ]

    allow_domains = [
        "ziare.com"
    ]
    deny = [
        "/sitemap",
        "/politica-cookies",
        "/codul-jurnalistului",
        "/termeni-si-conditii",
        "/contact",
        "http://www.ziare.com/index.php?module=AmvcPopup&action=justLogin&opt=semnaleazaComNelogat&message_id=935616"
    ]

    deny_list =[
        "http://www.ziare.com/politica-cookies/",
        "http://www.ziare.com/regulament",
        "http://www.ziare.com/termeni-si-conditii",
        "http://www.ziare.com/contact",
        "http://www.ziare.com/codul-jurnalistului",
        "http://www.ziare.com/comunitate/login",
        "http://www.ziare.com/sitemap"
    ]

    httpPrefix = "http:"
    httpsPrefix = "https:"

    def run(self, path, path_normal_img):
        # you can revisit your portal urls in this method
        print("HERE $$$")

        extraction_helper = HelperClassExtraction(start_url=self.start_url, deny_list=self.deny_list)

        options = Options()
        options.add_argument("--headless")

        #path = '/home/alex2/PycharmProjects/newscrapy/ziareCom ads test'
        #path_normal_img = '/home/alex2/PycharmProjects/newscrapy/ziareCom ads test/regular/'

        nr = 0
        for url in self.start_urls:
            print("Number:{}".format(nr))
            browser = webdriver.Firefox(firefox_options=options)
            browser.implicitly_wait(7)

            try:
                browser.get(url)

                set_src = extraction_helper.my_link_extractor(browser=browser)
                normal_img_src_list = extraction_helper.extract_regular_images_src_list(browser=browser,http_prefix=self.httpPrefix,https_prefix=self.httpsPrefix)
                extraction_helper.extract_img_from_src_list(list_src=normal_img_src_list, path=path_normal_img)

                rez = self.extract_add_images_and_save(url=url, browser=browser, path=path)
                extraction_helper.extract_img_from_src_list(list_src=rez, path=path)

                self.start_urls += self.start_urls + list(set_src)
                self.start_urls = list(set(self.start_urls))

                browser.close()
                nr += 1

            except Exception as ex:
                print("Exception {}".format(ex))

        print("HERE ###")

    def extract_add_images_and_save(self, url, browser, path):

        if self.start_urls[0] == url:
            print("here in ads home page")
            homePageAds = ZiareComAddsHomePage(_browser=browser, url=url, path=path)
            return homePageAds.get_home_page_ads()

        if url in self.list_category_ziare_com:
            print("here in ads category pages")
            categoryAds = ZiareComAddsCategoryPage(_browser=browser, url=url, path=path)
            return categoryAds.get_category_page_ads()

        else:
            articleAds = ZaireComAddsArticlePage(_browser=browser, url=url, path=path)
            return articleAds.get_article_ads()

