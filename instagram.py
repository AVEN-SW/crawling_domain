from bs4 import BeautifulSoup as bs
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



class InstaCrawling:
    
    def __init__(self):
        self.insta_id = 'cementkpu@gmail.com'
        self.pw = '@tkaruqtkf92'
        self.video_url = []
        self.img_url = []
        self.video_date = []
        self.img_date = []
        self.writer = []

    def crawling(self):
        driver = wb.Safari()
        driver.get('https://www.instagram.com/')
        driver.maximize_window()

        # 로그인
        time.sleep(1)
        input_id = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        input_pw = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')

        input_id.send_keys(self.insta_id)
        input_pw.send_keys(self.pw)

        login_btn = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        login_btn.click()
        time.sleep(6)

        save_info_btn = driver.find_element(By.CLASS_NAME, '_acan._acap._acas._aj1-')
        save_info_btn.click()

        time.sleep(3)
        alert_set = driver.find_element(By.CLASS_NAME,'_a9--._a9_1')
        alert_set.click()

        # 프로필 접근
        time.sleep(3)
        profile_btn_list = driver.find_elements(By.CLASS_NAME,'x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft')

        for i in profile_btn_list:
            if i.text == '프로필':
                profile_btn = i

        profile_btn.click()

        # 태그된 게시물 접근
        time.sleep(5)
        taged_btn_list = driver.find_elements(By.CLASS_NAME,'x6umtig.x1b1mbwd.xaqea5y.xav7gou.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mnrxsn.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x11njtxf')

        for i in taged_btn_list:
            if i.text == '태그됨':
                taged_btn = i
        time.sleep(4)

        taged_btn.click()        

        time.sleep(2)
        div_content = driver.find_elements(By.CLASS_NAME,'_ac7v._al3n')

        for j in range(len(div_content)):
            thumb_img_list = div_content[j].find_elements(By.CSS_SELECTOR, 'article > div > div > div > div > a > div._aagu')



            for i in range(len(thumb_img_list)):

                # 썸네일 클릭
                thumb_img = thumb_img_list[i]
                thumb_img.click()
                time.sleep(2)


                # 모달창 엘리먼트 가져오기
                article = driver.find_element(By.CSS_SELECTOR,'article._aatb._aate._aatg._aati')

                # 피드에 사진이나 영상이 하나 이상일때(다음을 나타내는 화살표 버튼이 있을때) 영상이나 이미지 url 가져오기
                try:
                    while driver.find_element(By.CSS_SELECTOR,'button._afxw._al46._al47'):
                        next_btn = driver.find_element(By.CSS_SELECTOR,'button._afxw._al46._al47')
                        try:
                            video = driver.find_element(By.TAG_NAME, 'video').get_attribute('src')
                            self.video_url.append(video)

                            date = driver.find_element(By.CLASS_NAME, '_aaqe').get_attribute('title')
                            self.video_date.append(date)

                            writer_id = driver.find_element(By.CLASS_NAME, '/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/span/div/div/a').text
                            self.writer.append(writer_id)
                        except:
                            img = driver.find_element(By.TAG_NAME, 'img').get_attribute('src')
                            self.img_url.append(img)

                            date = driver.find_element(By.CLASS_NAME, '_aaqe').get_attribute('title')
                            self.img_date.append(date)

                            writer_id = driver.find_element(By.CLASS_NAME, '/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/span/div/div/a').text
                            self.writer.append(writer_id)
                        next_btn.click()
                        time.sleep(1)

                    driver.back()

                except:
                    pass

                # 영상이나 이미지가 하나만 존재하는 피드일때 url 가져오기
                try:
                    video = driver.find_element(By.TAG_NAME, 'video').get_attribute('src')
                    self.video_url.append(video)

                    date = driver.find_element(By.CLASS_NAME, '_aaqe').get_attribute('title')
                    self.video_date.append(date)

                    writer_id = driver.find_element(By.CLASS_NAME,'/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/span/div/div/a').text
                    self.writer.append(writer_id)
                except:
                    img = driver.find_element(By.TAG_NAME, 'img').get_attribute('src')
                    self.img_url.append(img)

                    date = driver.find_element(By.CLASS_NAME, '_aaqe').get_attribute('title')
                    self.img_date.append(date)

                    writer_id = driver.find_element(By.CLASS_NAME,'/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/span/div/div/a').text
                    self.writer.append(writer_id)
                time.sleep(2)
                driver.back()

        driver.quit()

        return self.img_url, self.video_url, self.img_date, self.video_date, self.writer

        