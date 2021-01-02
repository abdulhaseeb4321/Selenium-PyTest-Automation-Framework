import os
from pathlib import Path
from datetime import date
import time
import imagehash
from PIL import Image, ImageChops


class Screenshot:

    def __init__(self, driver,browser,testcase):
        self.driver = driver
        self.browser = browser
        self.testcase = testcase
        self.step_count=0
        self.path = str(Path(__file__).parent.parent)+'/screenshot'

    def take_screenshot(self, driver, full_page=True):

        full_height = driver.execute_script(
            "var body = document.body, html = document.documentElement; return Math.max( body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight );")

        visible_height = driver.execute_script("return window.innerHeight")
        counter = 1
        temp_file_prefix = "temp_" + str(time.time()) + "_"

        for y in range(0, full_height, visible_height):
            full_height = driver.execute_script(
                "var body = document.body, html = document.documentElement; return Math.max( body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight );")
            try:
                driver.execute_script("window.scrollTo(0," + str(y) + ")")
                temp_path = temp_file_prefix + str(counter) + ".png"
                time.sleep(1)
                driver.save_screenshot(temp_path)
                counter += 1
                img = Image.open(temp_path)
                width, height = img.size
                ratio = height / visible_height
                img = img.resize((int(width / ratio), visible_height))
                img.save(temp_path)
                if driver.execute_script("return document.getElementById('masthead').style.visibility") != 'hidden':
                    driver.execute_script("document.getElementById('masthead').style.visibility = 'hidden'")
                if not full_page:
                    break
            except Exception as e:
                print(e)
        skip = full_height % visible_height
        if skip > 0:
            img = img.crop((0, img.size[1] - skip, img.size[0], visible_height))
            img.save(temp_path)

        image = Image.open(temp_file_prefix + "1.png")
        full_image = Image.new('RGB', (image.size[0], image.size[1] * (counter - 2) + img.size[1]))
        full_image.paste(im=image, box=(0, 0))
        os.remove(temp_file_prefix + "1.png")
        height_start = 0
        for i in range(2, counter):
            path = temp_file_prefix + str(i) + ".png"
            image = Image.open(path)
            height_end = height_start + visible_height
            full_image.paste(im=image, box=(0, height_end))
            height_start = height_end
            os.remove(path)
        return full_image

    def modify_screen_short(self, name, load_page=0):
        today = str(date.today())
        driver = self.driver
        browser = self.browser
        name = str(self.step_count) + '_' + name + '.png'

        dir_path_pass = (self.path + '/baseline/' + browser + '/' + self.testcase)
        dir_path_fail = (self.path + '/fail/' + today + '/' + browser + '/' + self.testcase)
        screen_shot_path = (self.path + '/baseline/' + browser + '/' + self.testcase + '/' + name)
        if load_page:
            i = 0
            while i < driver.execute_script("return document.body.scrollHeight"):
                driver.execute_script("window.scrollTo(0, " + str(i) + ")")
                time.sleep(1)
                i = i + 500
            driver.execute_script("window.scrollTo(0,0)")
            time.sleep(3)
        if os.path.exists(screen_shot_path):
            current_img = self.take_screenshot(driver)
            original_img = Image.open(screen_shot_path)
            current = imagehash.average_hash(current_img)
            original = imagehash.average_hash(original_img)

            if current == original:
                res = [name + ' PASS']
                assert True
            else:
                name = name.replace(".png", "_fail.png")
                if not os.path.exists(dir_path_fail):
                    os.makedirs(dir_path_fail)
                current_img = current_img.resize(original_img.size)
                current_img = ImageChops.difference(original_img, current_img)
                fail_img = Image.blend(current_img.convert('RGBA'), original_img.convert('RGBA'), 0.2)
                fail_img.save(dir_path_fail + '/' + name)
            assert False

        else:
            if os.path.exists(dir_path_pass):
                png = self.take_screenshot(driver)
                print(png)
                png.save(screen_shot_path)
            else:
                os.makedirs(dir_path_pass)
                png = self.take_screenshot(driver)
                print(png)
                png.save(screen_shot_path)
        self.step_count += 1
