import hashlib
from PIL import Image
from io import BytesIO
from random import randint
from scipy.misc import imread
import shutil
import numpy as np
import scipy
import os
import cv2
import itertools

import logging
import datetime

now = datetime.datetime.now()

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('Selenium{}.log'.format(now.date()))

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class HelperClass:

    def __init__(self, path):
        self.path = path

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = path

    def filter_images(self, images):
        images_list = []
        for image in images:
            try:
                assert imread(image).shape[2] == 4
                images_list.append(image)
                # print(len(images_list))
            except AssertionError as e:
                print(e)
        return images_list

    def img_gray2(self, image, path):
        # print("here")
        image = imread(path + image)
        # print(image.shape)
        # print(image)

        # convert 4 chanel png to 3 chanel
        imageM = image[:, :, :-1]
        # print(imageM)

        rez = np.average(imageM, weights=[0.299, 0.587, 0.114], axis=2)
        return rez

    # resize image and flatten
    def resize(self, image, height=30, width=30):
        row_res = cv2.resize(image, (height, width), interpolation=cv2.INTER_AREA).flatten()
        col_res = cv2.resize(image, (height, width), interpolation=cv2.INTER_AREA).flatten('F')
        return row_res, col_res

    def intensity_diff(self, row_res, col_res):
        difference_row = np.diff(row_res)
        difference_col = np.diff(col_res)
        difference_row = difference_row > 0
        difference_col = difference_col > 0
        return np.vstack((difference_row, difference_col)).flatten()
        # return difference_row
        # return np.vstack((difference_row, difference_col)) #str method

    def difference_score(self, image, path, height=30, width=30):
        # gray = img_gray(image, path)
        gray = self.img_gray2(image, path)
        row_res, col_res = self.resize(gray, height, width)
        difference = self.intensity_diff(row_res, col_res)

        return difference

    def difference_score_dict(self, image_list, path):
        ds_dict = {}
        duplicates = []
        for image in image_list:
            ds = self.difference_score(image, path)

            if image not in ds_dict:
                ds_dict[image] = ds
            else:
                duplicates.append((image, ds_dict[image]))

        return duplicates, ds_dict

    def hamming_distance(self, image, image2):
        score = scipy.spatial.distance.hamming(image, image2)
        return score

    def eliminate_duplicates(self, duplicates, path):
        for item in duplicates:
            print(item)
            if os.path.exists(path + item[1]):
                os.remove(path=path + item[1])

    def eliminate_duplicated_saved_picture(self, path):
        # print("here")

        

        os.chdir(path=path)
        logger.debug(os.getcwd())
        # get the file list
        files_list = os.listdir()
        logger.debug(len(files_list))

        img_files = []

        for index, filename in enumerate(os.listdir('.')):
            if os.path.isfile(filename) and filename != "geckodriver.log":
                img_files.append(filename)

        logger.debug(len(img_files))
        # print("end")

        image_files = self.filter_images(img_files)
        # print("end2")
        duplicates, ds_dict = self.difference_score_dict(image_files, path)
        # print("end3")
        for k1, k2 in itertools.combinations(ds_dict, 2):
            h_d = self.hamming_distance(ds_dict[k1], ds_dict[k2])
            # print("{} {} {}".format(k1, k2, h_d))
            if h_d < .40:
                # print("{} {} {}".format(k1, k2, h_d))
                duplicates.append((k1, k2))

        if len(duplicates) > 0:
            logger.debug(" Number of duplicates {}".format(len(duplicates)))
            self.eliminate_duplicates(duplicates, path)

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

    def convert_to_sha1_hash(self, filename):

        msg = hashlib.sha1()

        data = filename.encode()

        msg.update(data)

        newname = str(msg.hexdigest())

        return newname

    def screenshot_jpg(self, image, element, path):
        print("here in screenshot jpg function")

        y = randint(0, 100000000)

        nameFile = "screenshotFromNewsSite" + str(y)
        suffix = self.convert_to_sha1_hash(nameFile)

        with open('{dirname}/img_{suffix}.jpg'.format(dirname=path, suffix=suffix), 'wb') as out_file:
            shutil.copyfileobj(image.raw, out_file)

    def screenshot2(self, element, path, browser):
        print("here in screenshot function")
        location = element.location
        size = element.size

        print(location)
        print(size)

        if size['width'] < 50 or size['height'] < 50:
            return

        y = randint(0, 100000000)

        nameFile = "screenshotFromNewsSite" + str(y)
        location = path + self.convert_to_sha1_hash(nameFile) + ".png"

        browser.save_screenshot(location)
        print("done with save")

        # browser.close()

    def screenshot(self, element, path, browser):
        print("here in screenshot function %%")
        location = element.location
        size = element.size

        logger.debug(location)
        logger.debug(size)

        if size['width'] < 50 or size['height'] < 50:
            return

        # clone_browser = copy.deepcopy(browser)

        png = browser.get_screenshot_as_png()  # saves screenshot of entire page
        im = Image.open(BytesIO(png))  # uses PIL library to open image in memory
        # im = Image.open(png)

        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        y = randint(0, 100000000)

        nameFile = "screenshotFromNewsSite" + str(y)
        location = path + self.convert_to_sha1_hash(nameFile) + ".png"

        im = im.crop((left, top, right, bottom))  # defines crop points
        # im.thumbnail(size, Image.ANTIALIAS)
        im.save(location)  # saves new cropped image
        logger.debug(location)

        # clone_browser.close()



