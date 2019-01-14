from seleniumContinusCrawler.SeleniumContinusCrawler import NewsCrawler
from helperContinus.HelperClass import HelperClass


def main():
    print("HERE")

    crawler = NewsCrawler()
    path_adds = 'C:\\Users\\User\\Desktop\\add\\'

    i = 1

    while i > 0:
        print("HERE ##")
        crawler.run(path_adds)
        duplicate_helper = HelperClass(path=path_adds)
        duplicate_helper.eliminate_duplicated_saved_picture(path=path_adds)
        i = -1


def main2():
    print("Just the img duplicate checker")
    path_adds = 'E:\\DatasetForImgNet\\add\\'

    duplicate_helper = HelperClass(path=path_adds)
    duplicate_helper.eliminate_duplicated_saved_picture(path=path_adds)

main2()
