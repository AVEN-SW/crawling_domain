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
        

    def crawling(self):
        driver = wb.Safari()
        driver.get('https://www.instagram.com/')
        driver.maximize_window()

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

        time.sleep(3)
        profile_btn_list = driver.find_elements(By.CLASS_NAME,'x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft')

        for i in profile_btn_list:
            if i.text == '프로필':
                profile_btn = i

        profile_btn.click()

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
                thumb_img = thumb_img_list[i]
                thumb_img.click()
                time.sleep(2)  # 적절한 대기 시간을 설정하세요.

                article = driver.find_element(By.CSS_SELECTOR,'article._aatb._aate._aatg._aati')

                try:
                    while driver.find_element(By.CSS_SELECTOR,'button._afxw._al46._al47'):
                        next_btn = driver.find_element(By.CSS_SELECTOR,'button._afxw._al46._al47')
                        try:
                            video = driver.find_element(By.TAG_NAME, 'video').get_attribute('src')
                            self.video_url.append(video)

                        except:
                            img = driver.find_element(By.TAG_NAME, 'img').get_attribute('src')
                            self.img_url.append(img)

                        next_btn.click()
                        time.sleep(1)

                    driver.back()

                except:
                    pass

                try:
                    video = driver.find_element(By.TAG_NAME, 'video').get_attribute('src')
                    self.video_url.append(video)

                except:
                    img = driver.find_element(By.TAG_NAME, 'img').get_attribute('src')
                    self.img_url.append(img)

                time.sleep(2)
                driver.back()

        driver.quit()
        return self.img_url, self.video_url

        