from ziareComContinusCrawler.ZiareComContinusCrawler import ZiarulComCrawler


def main():
    print("HERE")

    crawler = ZiarulComCrawler()

    i = 1

    # need to be updated with right path
    path = 'C:\\Users\\User\\Desktop\\add\\'
    path_normal_img = 'C:\\Users\\User\\Desktop\\RegularImgs\\'

    while i > 0:
        print("HERE ##")
        crawler.run(path=path, path_normal_img=path_normal_img)


main()
