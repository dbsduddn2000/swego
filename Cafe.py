from http.client import CONTINUE
from pprint import pprint
import os
import urllib.request
from json import load
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time
import pyperclip
import chromedriver_autoinstaller
import subprocess
import autoit
from selenium.webdriver.common.alert import Alert
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot, QObject, pyqtSignal
from PIL import Image
import re
from tkinter.filedialog import askopenfilename, askdirectory
import natsort
import shutil
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import multiprocessing
import emoji
first_upload = 0
photo_data_exist = 1
def operate_chrome():
    chrome_op = Options()

    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인

    
    chrome_op.add_argument('headless')
    chrome_op.add_argument('--disable-gpu')
    chrome_op.add_argument('--window-size=1920,1080')
    chrome_op.add_argument('--no-sandbox')
    chrome_op.add_argument('--start-maximized')
    chrome_op.add_argument('--disable-setuid-sandbox')

    # 맥버전용 코드
    try:
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe ', options = chrome_op)   
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe ', options = chrome_op)

    driver.implicitly_wait(3)
    driver.set_window_size(1300, 1000)

    return driver

def operate_chrome2():
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')

    chrome_op = Options()

    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인

    chrome_op.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    try:
        driver2 = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe ', options = chrome_op)   
    except:
        chromedriver_autoinstaller.install(True)
        driver2 = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe ', options = chrome_op)

    driver2.implicitly_wait(3)
    driver2.set_window_size(1300, 1000)
    
    return driver2

def clear_photo():
    try:
        file_list = os.listdir('C:\\CafeData\\Photo')
        file_list_result = [file for file in file_list if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")]

        for i in file_list_result:
            os.remove('C:\\CafeData\\Photo\\' + i)
    except:
        print('error')

    try:
        os.remove('C:\\CafeData\\photo_cnt.txt')
    except:
        print('error')

class cafe24posting(QThread):
    signal = pyqtSignal(int)
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        try:
            global first_upload
            global driver2
            idstr3 = self.parent.lineEdit_29.text()
            pwstr3 = self.parent.lineEdit_30.text()
            usrid = idstr3
            usrpw = pwstr3

            if first_upload == 0:
                try:
                    driver2.set_window_size(1300, 1000)
                    driver2.get('https://eclogin.cafe24.com/Shop/?url=Init&login_mode=1')
                except:
                    driver2 = operate_chrome2()
                    driver2.set_window_size(1300, 1000)
                    driver2.get('https://eclogin.cafe24.com/Shop/?url=Init&login_mode=1')
                
                f = open('C:\\CafeData\\idps.txt', 'w', encoding='utf-8')
                f.write(usrid)
                f.write('\n')
                f.write(usrpw)
                f.write('\n')
                f.close()

                idpart = driver2.find_element_by_xpath('/html/body/div[2]/div/section/div/form/div/div[1]/div/div[1]/div/input')
                idpart.clear()
                idpart.send_keys(usrid)

                pwpart = driver2.find_element_by_xpath('/html/body/div[2]/div/section/div/form/div/div[1]/div/div[2]/div/input')
                pwpart.clear()
                pwpart.send_keys(usrpw)

                driver2.find_element_by_xpath('/html/body/div[2]/div/section/div/form/div/div[3]/button').click()

                time.sleep(1)

                try:
                    driver2.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[4]/a[2]').click()
                    time.sleep(1)
                except:
                    pass

                first_upload = 1
            
            try:
                driver2.set_window_size(1300, 1000)
                driver2.get('http://' + usrid + '.cafe24.com/disp/admin/shop1/product/productregister')
            except:
                driver2 = operate_chrome2()
                driver2.set_window_size(1300, 1000)
                driver2.get('https://eclogin.cafe24.com/Shop/?url=Init&login_mode=1')
                f = open('C:\\CafeData\\idps.txt', 'w', encoding='utf-8')
                f.write(usrid)
                f.write('\n')
                f.write(usrpw)
                f.write('\n')
                f.close()

                idpart = driver2.find_element_by_xpath('/html/body/div[2]/div/section/div/form/div/div[1]/div/div[1]/div/input')
                idpart.clear()
                idpart.send_keys(usrid)

                pwpart = driver2.find_element_by_xpath('/html/body/div[2]/div/section/div/form/div/div[1]/div/div[2]/div/input')
                pwpart.clear()
                pwpart.send_keys(usrpw)

                driver2.find_element_by_xpath('/html/body/div[2]/div/section/div/form/div/div[3]/button').click()

                time.sleep(1)

                try:
                    driver2.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[4]/a[2]').click()
                    time.sleep(1)
                except:
                    pass

                driver2.get('http://' + usrid + '.cafe24.com/disp/admin/shop1/product/productregister')
        
            #진열상태 체크 부분
            driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[1]/div[2]/div/table/tbody/tr[1]/td/label[1]/input').click()
            driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[1]/div[2]/div/table/tbody/tr[2]/td/label[1]/input').click()

            #상품 제목 설정 부분
            theme_data = self.parent.lineEdit_2.text()
            brand = self.parent.lineEdit_28.text()
            trend = self.parent.lineEdit_6.text()
            send_result = brand + ' ' + theme_data.replace('amp;', '') + ' ' + trend
            
            theme_send = theme_data.replace('amp;', '')
            theme_in = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[4]/div[2]/div/table[1]/tbody/tr[1]/td/div/div[1]/input[1]')
            theme_in.send_keys(theme_send)
            time.sleep(0.3)
            #모델명 설정 부분
            pyperclip.copy(send_result)
            model_name_in = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[4]/div[2]/div/table[1]/tbody/tr[5]/td/div/input')
            model_name_in.send_keys(send_result)
            time.sleep(0.3)
            #자체 상품코드 기입
            code_data = self.parent.lineEdit_31.text()
            pyperclip.copy(code_data)
            code_in = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[4]/div[2]/div/table[1]/tbody/tr[7]/td/input')
            
            code_in.send_keys(code_data)
            time.sleep(0.3)
            #요약 설명
            word = self.parent.lineEdit_3.text()
            pyperclip.copy(word)
            code_in = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[4]/div[2]/div/table[1]/tbody/tr[9]/td/div/input')
            code_in.send_keys(word)
            time.sleep(0.3)
            #상품상세설명
            try:
                driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[4]/div[2]/div/table[1]/tbody/tr[11]/td/div/div[1]/ul/li[2]/a').click()
            except:
                driver2.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/div[4]/div[2]/div/table[1]/tbody/tr[11]/td/div/div[1]/ul/li[2]/a').click()
            
            real_content = self.parent.plainTextEdit.toPlainText()
            detail_content = str(real_content).replace('amp;', '') + '\n\n\n'
            pyperclip.copy(detail_content)
            driver2.switch_to.frame('product_description_IFRAME')
            body = driver2.find_element_by_xpath('/html/body')
            body.send_keys(Keys.CONTROL + 'v')
            driver2.switch_to.default_content()
            time.sleep(0.5)

            try:
                img_cnt_txt = open('C:\\CafeData\\photo_cnt.txt', 'r' , encoding='utf-8')
                img_cnt = img_cnt_txt.readline()
                img_cnt_txt.close()

                img_cnt = int(img_cnt.replace('\n', ''))
            except:
                img_cnt = 0

            img_final_path = ''

            upimage = self.parent.lineEdit_8.text()

            if upimage != '':
                f = open('C:\\CafeData\\upimage.txt', 'r', encoding='utf-8')
                upimage = f.readline()
                f.close()

                img_final_path = img_final_path + upimage + '\n'

            file_list = os.listdir('C:\\CafeData\\Photo')
            file_list_result2 = [file for file in file_list if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")]
            file_list_result = natsort.natsorted(file_list_result2)
            

            for k in range(len(file_list_result)):
                if k == (len(file_list_result) - 1):
                    img_final_path = img_final_path + 'C:\\CafeData\\Photo\\' + file_list_result[k]
                else:
                    img_final_path = img_final_path + 'C:\\CafeData\\Photo\\' + file_list_result[k] + '\n'

            downimage = self.parent.lineEdit_10.text()

            if downimage != '':
                f = open('C:\\CafeData\\downimage.txt', 'r', encoding='utf-8')
                downimage = f.readline()
                f.close()

                downimage = downimage.replace('\n', '')

                downimage = '\n' + downimage

                img_final_path = img_final_path + downimage
            
            #사진 파트
            time.sleep(0.5)
            driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[4]/div[2]/div/table[1]/tbody/tr[11]/td/div/div[3]/div/div/div[1]/div[3]/button[2]').click()
            
            temp_cnt = 7       
            files = driver2.find_element_by_xpath(f'/html/body/div[1]/div[2]/div[2]/form/div[4]/div[2]/div/table[1]/tbody/tr[11]/td/div/div[3]/div/div/div[1]/div[{temp_cnt}]/div[2]/div/div[2]/input')
            print(f'/html/body/div[1]/div[2]/div[2]/form/div[4]/div[2]/div/table[1]/tbody/tr[11]/td/div/div[3]/div/div/div[1]/div[{temp_cnt}]/div[2]/div/div[2]/input')

            files.send_keys(img_final_path)
            
            for k in range(len(file_list_result)):
                temp_value = k + 1
                print(temp_value)
                whilevalue = True
                while(whilevalue):
                    try:
                        tempbtn = driver2.find_element_by_xpath(f'/html/body/div[1]/div[2]/div[2]/form/div[4]/div[2]/div/table[1]/tbody/tr[11]/td/div/div[3]/div/div/div[1]/div[{temp_cnt}]/div[5]/div[2]/div[{temp_value}]/div[2]/div[1]/span')
                        
                        whilevalue = False
                    except Exception as e:
                        print(e)
        
            driver2.find_element_by_xpath(f'/html/body/div[1]/div[2]/div[2]/form/div[4]/div[2]/div/table[1]/tbody/tr[11]/td/div/div[3]/div/div/div[1]/div[{temp_cnt}]/div[1]/span/button[1]').click()
            driver2.find_element_by_xpath(f'/html/body/div[1]/div[2]/div[2]/form/div[4]/div[2]/div/table[1]/tbody/tr[11]/td/div/div[3]/div/div/div[1]/div[{temp_cnt}]/div[1]/span/button[3]').click()

            #가격 설정 부분
            price_data = self.parent.lineEdit_4.text()
            pyperclip.copy(price_data)
            #공급가
            #price_in = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[7]/div[2]/div/table/tbody/tr[2]/td/input[1]')
            #price_in.clear()
            #price_in.send_keys(Keys.CONTROL, 'v')
            #time.sleep(1)

            #과세구분
            driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[7]/div[2]/div/table/tbody/tr[3]/td/div/label[3]/input').click()
            #판매가
            try:
                price_in = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[7]/div[2]/div/table/tbody/tr[5]/td/div/table/tbody/tr/td[1]/input')
                price_in.clear()
                price_in.send_keys(price_data)
                
            except:
                price_in = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[7]/div[2]/div/table/tbody/tr[4]/td/div/table/tbody/tr/td[1]/input')
                price_in.clear()
                price_in.send_keys(price_data)
                

            #대표이미지 업로드
            img = Image.open('C:\\CafeData\\Photoex\\k.jpg')
            img_resize = img.resize((300,300))
            img_resize.save('C:\\CafeData\\Photoex\\m.jpg')

            driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[16]/div[2]/div/table/tbody/tr[1]/td/div/div/div/div[1]/div/ul/li[1]/span[4]/a[1]').click()
            
            autoit.win_wait_active("열기", 2)

            best_img_path = 'C:\\CafeData\\Photoex\\m.jpg'
            autoit.send(best_img_path)
            time.sleep(1)
            autoit.send('{ENTER}')

            #옵션파트
            op1 = self.parent.lineEdit_11.text()
            op2 = self.parent.lineEdit_12.text()
            op3 = self.parent.lineEdit_13.text()

            opL1 = self.parent.lineEdit_14.text()
            opL2 = self.parent.lineEdit_15.text()
            opL3 = self.parent.lineEdit_16.text()
            
            exit_op = 0

            if op1 != '':
                exit_op = 1
                print('a')
                driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[9]/div[2]/div/table[1]/tbody/tr/td/label[1]/input').click()
                time.sleep(1)
                driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[9]/div[2]/div/table[2]/tbody/tr/td/label[2]/input').click()
                time.sleep(1)
                driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[9]/div[2]/div/table[5]/tbody/tr/td/label[3]/input').click()

                try:
                    driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[9]/div[2]/div/table[7]/tbody/tr/td/div[2]/table/tbody/tr[3]/td[4]/div/div/div[2]/button[1]').click()
                except:
                    print('none 2')

                in1 = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[9]/div[2]/div/table[7]/tbody/tr/td/div[2]/table/tbody/tr[2]/td[3]/input')

                in1.clear()
                pyperclip.copy(op1)
                in1.send_keys(Keys.CONTROL, 'v')
                
                in2 = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[9]/div[2]/div/table[7]/tbody/tr/td/div[2]/table/tbody/tr[2]/td[4]/div/div/div[1]/ul/li/span/input')
                in2.click()
                in2.send_keys(opL1)
                    

            if op2 != '':
                exit_op = 1
                print('a')
                try:
                    driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[9]/div[2]/div/table[7]/tbody/tr/td/div[2]/table/tbody/tr[2]/td[4]/div/div/div[2]/button[2]').click()
                except:
                    print('exist')

                in1 = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[9]/div[2]/div/table[7]/tbody/tr/td/div[2]/table/tbody/tr[3]/td[3]/input')
                
                in1.clear()
                pyperclip.copy(op2)
                in1.send_keys(Keys.CONTROL, 'v')

                in2 = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[9]/div[2]/div/table[7]/tbody/tr/td/div[2]/table/tbody/tr[3]/td[4]/div/div/div[1]/ul/li/span/input')
                
                in2.click()
                in2.send_keys(opL2)

            if op3 != '':
                exit_op = 1
                print('a')
                try:
                    driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[9]/div[2]/div/table[7]/tbody/tr/td/div[2]/table/tbody/tr[3]/td[4]/div/div/div[2]/button[2]').click()
                except:
                    print('exist')
                

                in1 = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[9]/div[2]/div/table[7]/tbody/tr/td/div[2]/table/tbody/tr[4]/td[3]/input')
                in1.clear()
                pyperclip.copy(op3)
                in1.send_keys(Keys.CONTROL, 'v')

                in2 = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[9]/div[2]/div/table[7]/tbody/tr/td/div[2]/table/tbody/tr[4]/td[4]/div/div/div[1]/ul/li/span/input')
                in2.click()
                in2.send_keys(opL3)

            if exit_op == 1:
                for i in range(5):
                    action = ActionChains(driver2)
                    wantbtn = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[9]/div[2]/div/table[7]/tbody/tr/td/div[3]/div/a')
                    action.move_to_element(wantbtn).click().perform()
                #driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[9]/div[2]/div/table[7]/tbody/tr/td/div[3]/div/a').click()
                #driver2.execute_script('arguments[0].click();', add_btn)

            
            #제작정보
            action = ActionChains(driver2)
            
            add_btn = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[1]/div/span/button')
            driver2.execute_script('arguments[0].click();', add_btn)
            cate = self.parent.lineEdit_5.text()
            trend = self.parent.lineEdit_6.text()
            brand = self.parent.lineEdit_28.text()
            from_data = self.parent.lineEdit_7.text()
            
            target_element = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[3]/td/div/a')
            action.move_to_element(target_element).click().perform()
            action.move_to_element(target_element).click().perform()
            time.sleep(1)
            while(True):
                
                try:
                    time.sleep(0.5)
                    tm = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[3]/td/div/div/ul/li').text
                    print(tm)
                    
                    if '연결' in tm or '로딩' in tm:
                        print('대기중')
                        continue
                    else:
                        break
                except:
                    run_cnt += 1
                    continue
            time.sleep(1)
            brand_in = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[3]/td/div/div/div/input[2]')
            pyperclip.copy(brand)
            brand_in.send_keys(Keys.CONTROL, 'v')
            run_cnt = 0
            while(True):
                
                try:
                    time.sleep(0.5)
                    tm = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[3]/td/div/div/ul/li').text
                    print(tm)
                    
                    if '연결' in tm or '로딩' in tm:
                        print('대기중')
                    else:
                        break
                except:
                    run_cnt += 1
                    continue
            time.sleep(1)
            brand_in.send_keys(Keys.ENTER)

            time.sleep(0.5)
            ditect_str = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[3]/td/div/a/span').text
            if ditect_str != brand:
                driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[3]/td/a').click()
                time.sleep(0.5)
                driver2.find_element_by_xpath('/html/body/form[5]/div[1]/div[1]/div[2]/table/tbody/tr/td/input').send_keys(brand)
                driver2.find_element_by_xpath('/html/body/form[5]/div[1]/div[2]/a[1]').click()
                time.sleep(0.5)
                try:
                    Alert(driver2).dismiss()
                except:
                    print("no alert")

            target_element = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[2]/td/div/a')
            action.move_to_element(target_element).click().perform()
            while(True):
                
                try:
                    time.sleep(0.5)
                    tm = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[2]/td/div/div/ul/li').text
                    print(tm)
                    
                    if '연결' in tm or '로딩' in tm:
                        print('대기중')
                    else:
                        break
                except:
                    run_cnt += 1
                    continue
            time.sleep(1)
            from_in = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[2]/td/div/div/div/input[2]')
            pyperclip.copy(from_data)
            from_in.send_keys(Keys.CONTROL, 'v')
            run_cnt = 0
            while(True):
                
                try:
                    time.sleep(0.5)
                    tm = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[2]/td/div/div/ul/li').text
                    if '연결' in tm or '로딩' in tm:
                        print('대기중')
                    else:
                        break
                except:
                    run_cnt += 1
                    continue
            time.sleep(1)
            from_in.send_keys(Keys.ENTER)

            time.sleep(1)
            ditect_str = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[2]/td/div/a/span').text
            if ditect_str != from_data:
                driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[2]/td/a').click()
                time.sleep(0.5)
                driver2.find_element_by_xpath('/html/body/form[4]/div[1]/div[1]/div[2]/table/tbody/tr[1]/td/input').send_keys(from_data)
                
                driver2.find_element_by_xpath('/html/body/form[4]/div[1]/div[2]/a[1]').click()
                time.sleep(0.5)
                try:
                    Alert(driver2).dismiss()
                except:
                    print("no alert")
            
            target_element = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[4]/td/div/a')
            action.move_to_element(target_element).click().perform()
            while(True):
                
                try:
                    time.sleep(0.5)
                    tm = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[4]/td/div/div/ul/li').text
                    print(tm)
                    
                    if '연결' in tm or '로딩' in tm:
                        print('대기중')
                    else:
                        break
                except:
                    run_cnt += 1
                    continue
            time.sleep(1)
            trend_in = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[4]/td/div/div/div/input[2]')
            pyperclip.copy(trend)
            trend_in.send_keys(Keys.CONTROL, 'v')
            run_cnt = 0
            while(True):
                try:
                    time.sleep(0.5)
                    tm = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[4]/td/div/div/ul/li').text
                    if '연결' in tm or '로딩' in tm:
                        print('대기중')
                    else:
                        break
                except:
                    run_cnt += 1
                    continue
            time.sleep(1)
            trend_in.send_keys(Keys.ENTER)

            time.sleep(1)
            ditect_str = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[4]/td/div/a/span').text
            if ditect_str != trend:
                driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[4]/td/a').click()
                time.sleep(0.5)
                driver2.find_element_by_xpath('/html/body/form[6]/div[1]/div[1]/div[2]/table/tbody/tr/td/input').send_keys(trend)
                
                driver2.find_element_by_xpath('/html/body/form[6]/div[1]/div[2]/a[1]').click()
                time.sleep(0.5)
                try:
                    Alert(driver2).dismiss()
                except:
                    print("no alert")
            
            target_element = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[5]/td/div/a')
            action.move_to_element(target_element).click().perform()
            time.sleep(0.5)
            while(True):
                
                try:
                    time.sleep(0.5)
                    tm = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[5]/td/div/div/ul/li').text
                    print(tm)
                    
                    if '연결' in tm:
                        continue
                    else:
                        break
                except:
                    run_cnt += 1
                    continue
            cate_in = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[5]/td/div/div/div/input[2]')
            pyperclip.copy(cate)
            cate_in.send_keys(Keys.CONTROL, 'v')
            run_cnt = 0
            while(True):
                try:
                    time.sleep(0.5)
                    tm = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[5]/td/div/div/ul/li').text
                    
                    if '연결' in tm or '로딩' in tm:
                        print('대기중')
                    else:
                        break
                    break
                except:
                    run_cnt += 1
                    continue
                
            time.sleep(1)
            cate_in.send_keys(Keys.ENTER)

            time.sleep(1)
            ditect_str = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[5]/td/div/a/span').text
            if ditect_str != cate:
                driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[19]/div[2]/div/table/tbody/tr[5]/td/a').click()
                time.sleep(0.5)
                driver2.find_element_by_xpath('/html/body/form[7]/div[1]/div[1]/div[2]/table/tbody/tr/td/input').send_keys(cate)
                
                driver2.find_element_by_xpath('/html/body/form[7]/div[1]/div[2]/a[1]').click()
                time.sleep(0.5)
                try:
                    Alert(driver2).dismiss()
                except:
                    print("no alert")
            
            #중복 url 정보 기입 (검색어설정)
            url_data = self.parent.lineEdit.text()
            sp_url = url_data.split('#/theme_detail/')
            fornt_url_sp = sp_url[0].split('?')
            input_url = fornt_url_sp[0] + '#/theme_detail/' + sp_url[len(sp_url) - 1]
            
            add_btn = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[32]/div[1]/div/span/button')
            driver2.execute_script('arguments[0].click();', add_btn)
            url_in = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[32]/div[2]/div/table/tbody/tr/td/textarea')
            url_in.clear()
            url_in.send_keys(input_url)

            #등록 버튼
            try:
                driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[35]/a[1]').click()
                time.sleep(1)
            except:
                try:
                    add_btn = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[35]/a[1]')
                    driver2.execute_script('arguments[0].click();', add_btn)
                    time.sleep(1)
                except:
                    add_btn = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[33]/a[1]')
                    driver2.execute_script('arguments[0].click();', add_btn)
                    time.sleep(1)
                    
                    
            try:
                Alert(driver2).dismiss()
            except:
                print("no alert")

            self.signal.emit(1)

            last_one = self.parent.lineEdit.text()
            last_one = last_one.replace('https', 'http')
            last_one = last_one.replace('#', '')

            try:
                temp_list = list()
                txt = open('C:\\CafeData\\url_data.txt', 'r', encoding='utf-8')
                lines = txt.realines()
                for line in lines:
                    line = line.strip()
                    temp_list.append(line)
                txt.close()

                txt = open('C:\\CafeData\\url_data.txt', 'w', encoding='utf-8')

                for k in temp_list:
                    txt.write(k)
                txt.write(last_one)
                txt.close()
            except:
                txt = open('C:\\CafeData\\url_data.txt', 'w', encoding='utf-8')
                txt.write(last_one)
                txt.close()

            try:
                codeinfo = self.parent.lineEdit_7.text()
                txt = open('C:\\CafeData\\code.txt', 'w', encoding='utf-8')
                txt.write(codeinfo)
                txt.close()
            except:
                print('invalid')

            clear_photo()
        except Exception as e:
            self.signal.emit(0)
            print(e)

def download_image(url, filename):

    while(True):
        try:
            urllib.request.urlretrieve(url, filename)
            img = Image.open(filename)
            break
        except:
            time.sleep(0.2)
            continue

class get_information(QThread):
    signal = pyqtSignal(int,str,str,str)
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        try:
            starttime = time.time()
            url_data = self.parent.lineEdit_9.text()
            url_data = url_data.replace('https', 'http')

            driver.get(url_data)
            
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]')))
            try:
                big_format = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[3]')
                picture_list = big_format.find_elements_by_tag_name('img')
            except:
                try:
                    big_format = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div')
                    picture_list = big_format.find_elements_by_tag_name('img')
                except:
                    try:
                        big_format = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]')
                        picture_list = big_format.find_elements_by_tag_name('img')
                    except:
                        big_format = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[1]/div[2]/div[1]/div/div[3]')
                        picture_list = big_format.find_elements_by_tag_name('img')

            photo_cnt = 0
            global photo_data_exist
            photo_data_exist = 1
            
            endtime = time.time()

            print(endtime - starttime)

            try:
                f = open('C:\\CafeData\\photo_cnt.txt', 'r', encoding='utf-8')
                data = f.readline()
                data = data.replace('\n', '')
                data = int(data)
                photo_cnt = data
            except:
                print("no photo count data")
                photo_data_exist = 0
                photo_cnt = 0
            

            with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
                for pic_data in picture_list:
                    src_url = pic_data.get_attribute('src')
                    if 'video' not in src_url:
                        photo_cnt += 1
                        src_temp = src_url.split('?')
                        src_url = src_temp[0]
                        nm = 'C:\\CafeData\\Photo\\' + str(photo_cnt) + '.jpg'
                        pool.apply_async(download_image, args=(src_url, nm))
                        time.sleep(0.1)
                pool.close()
                pool.join()

            endtime = time.time()
            
            print(endtime - starttime)

            try:
                if 'Specs' in driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[3]/div[1]').text:
                    specs = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[3]/div[2]/div')
                elif 'Specs' in driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[5]/div[1]').text:
                    specs = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[5]/div[2]/div')
                specs_txt = specs.text
            except:
                try:
                    specs = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[2]/div[4]/span')
                    specs_txt = specs.text
                except:
                    try:
                        specs = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[2]/div[5]/span')
                        specs_txt = specs.text
                    except:
                        try:
                            specs = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[3]/div[2]/div')
                            specs_txt = specs.text
                        except:
                            try:
                                if 'Specs' in driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[4]/div[1]').text:
                                    specs = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[4]/div[2]/div')
                                    specs_txt = specs.text
                                else:
                                    specs_txt = 'None'
                            except:
                                specs_txt = 'None'
            try:
                label = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[1]/div')
                label_txt = label.text 
            except:
                try:
                    label = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[2]/div[2]/span')
                    label_txt = label.text
                except:
                    try:
                        label = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[1]/div')
                        label_txt = label.text
                    except:
                        label_txt = 'none'

            try:
                
                if 'Search' in driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[2]/div[1]').text:
                    search_code_d = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[2]/div[2]')
                elif 'Search' in driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[3]/div[1]').text:
                    search_code_d = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[3]/div[2]')
                search_code = search_code_d.text 
            except:
                try:
                    search_code_d = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[2]/div[1]')
                    search_code = search_code_d.text
                except:
                    try:
                        search_code_d = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[2]/div[2]')
                        search_code = search_code_d.text
                    except:
                        search_code = 'none'

            search_code = search_code.replace('Search Code：', '')
            
            img = Image.open('C:\\CafeData\\Photo\\1.jpg')
            img_resize = img.resize((251,331))
            img_resize.save('C:\\CafeData\\Photoex\\k.jpg')

            if photo_data_exist == 0:
                self.parent.lineEdit_31.setText(str(search_code))
                pixmap = QPixmap('C:\\CafeData\\Photoex\\k.jpg')
                self.parent.label_3.setPixmap(pixmap)

            endtime = time.time()

            print(endtime - starttime)
            txt = open('C:\\CafeData\\photo_cnt.txt', 'w', encoding='utf-8')
            txt.write(str(photo_cnt))
            txt.close()

            self.parent.pushButton_4.setEnabled(True)
            self.signal.emit(0,specs_txt,str(label_txt),str(search_code))
            
        except Exception as e:
            self.parent.pushButton_4.setEnabled(True)
            print(e)
            self.signal.emit(1, '', '', '')

class checking_information(QThread):
    signal = pyqtSignal(int)
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    def run(self):
        input_url = self.parent.lineEdit.text()
        sp_url = input_url.split('/theme_detail/')
        fornt_url_sp = sp_url[0].split('?')
        input_url = fornt_url_sp[0] + '#/theme_detail/' + sp_url[len(sp_url) - 1]
        input_url = input_url.replace('##', '#')

        global first_upload
        global driver2
        idstr3 = self.parent.lineEdit_29.text()
        pwstr3 = self.parent.lineEdit_30.text()
        usrid = idstr3
        usrpw = pwstr3

        if first_upload == 0:
            try:
                driver2.set_window_size(1300, 1000)
                driver2.get('https://eclogin.cafe24.com/Shop/')
            except:
                driver2 = operate_chrome2()
                driver2.set_window_size(1300, 1000)
                driver2.get('https://eclogin.cafe24.com/Shop/')

            idpart = driver2.find_element_by_xpath('/html/body/div[2]/div/section/div/form/div/div[1]/div/div[1]/div/input')
            idpart.clear()
            idpart.send_keys(usrid)

            pwpart = driver2.find_element_by_xpath('/html/body/div[2]/div/section/div/form/div/div[1]/div/div[2]/div/input')
            pwpart.clear()
            pwpart.send_keys(usrpw)

            driver2.find_element_by_xpath('/html/body/div[2]/div/section/div/form/div/div[3]/button').click()

            time.sleep(1)

            try:
                driver2.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[4]/a[2]').click()
                time.sleep(1)
            except:
                pass

            first_upload = 1
        
        driver2.get(f'https://{usrid}.cafe24.com/disp/admin/shop1/product/productmanage')
        time.sleep(1)

        select_option = Select(driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/form/div[1]/div[2]/table/tbody/tr[1]/td/ul/li/select[1]'))
        select_option.select_by_value('pm_memo')

        driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/form/div[1]/div[2]/table/tbody/tr[1]/td/ul/li/input').send_keys(input_url)

        driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/form/div[1]/div[5]/a[1]').click()

        temp_text = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/form/div[2]/div[2]/div[1]/p').text
        numbers = re.sub(r'[^0-9]', '', temp_text)
        numbers = int(numbers)

        self.parent.pushButton.setEnabled(True)
        if numbers > 0:
            #ui.alert_message('상품등록여부','중복된 상품이 없습니다.')
            self.signal.emit(3)
        else:
            #ui.alert_message('상품등록여부','다른 상품으로 등록하세요.')
            self.signal.emit(2)

def Upimagefile():
    try:
        jpgfile = askopenfilename(title='jpg 파일을 선택하세요.', filetypes=[('Test File', '*.jpg'),('image file', '*.png')])
        f = open("C:\\CafeData\\upimage.txt", 'w', encoding='utf-8')
        f.write(jpgfile)
        f.close()
        return jpgfile
    except:
        return ''

def Downimagefile():
    try:
        jpgfile = askopenfilename(title='jpg 파일을 선택하세요.', filetypes=[('Test File', '*.jpg'),('image file', '*.png')])
        f = open("C:\\CafeData\\downimage.txt", 'w', encoding='utf-8')
        f.write(jpgfile)
        f.close()
        
        return jpgfile
    except:
        return ''

def mk_dir():
    os.makedirs("C:\\CafeData", exist_ok=True)
    os.makedirs("C:\\CafeData\\Photo", exist_ok=True)
    os.makedirs("C:\\CafeData\\Photoex", exist_ok=True)

class Ui_MainWindow(QMainWindow):
    def getfile1(self):
        result = Upimagefile()
        sp_result = result.split('/')
        self.lineEdit_8.setText(str(sp_result[len(sp_result) - 1]))

    def getfile2(self):
        result = Downimagefile()
        sp_result = result.split('/')
        self.lineEdit_10.setText(str(sp_result[len(sp_result) - 1]))
    
    def get_info(self):
        try:
            self.pushButton_4.setDisabled(True)
            x = get_information(self)
            x.signal.connect(self.alert_message4)
            x.start()
        except Exception as e:
            print('error')
            print(e)

    def posting(self):
        try:
            self.pushButton_11.setDisabled(True)
            x = cafe24posting(self)
            x.signal.connect(self.alert_message2)
            x.start()
        except:
            print('error')
    
    def checking_url(self):
        try:
            self.pushButton.setDisabled(True)
            x = checking_information(self)
            x.signal.connect(self.alert_message)
            x.start()
        except Exception as e:
            print(e)
        '''try:
            input_url = self.lineEdit.text()
            input_url = input_url.replace('https', 'http')
            txtdata = open("C:\\CafeData\\url_data.txt", 'r', encoding='utf-8')

            exist_value = 0
            lines = txtdata.readlines()
            for line in lines:
                line = line.strip()
                if line == input_url:
                    exist_value = 1
                    break
            
            if exist_value == 0:
                QMessageBox.about(self, '상품등록여부','중복된 상품이 없습니다.')
            else:
                self.lineEdit.clear()
                QMessageBox.about(self, '상품등록여부','다른 상품으로 등록하세요.')
        except:
            QMessageBox.about(self, '상품등록여부','중복된 상품이 없습니다.')'''
    
    @pyqtSlot(int)
    def alert_message(self, i):
        if i == 0:
            QMessageBox.information(self, '상품등록여부','이미지추출완료', QMessageBox.Yes | QMessageBox.Ok)
        elif i == 1:
            QMessageBox.information(self, '상품등록여부','이미지추출실패', QMessageBox.Yes | QMessageBox.Ok)
        elif i == 2:
            QMessageBox.information(self, '상품등록여부','중복된 상품이 없습니다', QMessageBox.Yes | QMessageBox.Ok)
        elif i == 3:
            QMessageBox.information(self, '상품등록여부','다른 상품으로 등록하세요', QMessageBox.Yes | QMessageBox.Ok)

    @pyqtSlot(int,str,str,str)
    def alert_message4(self, i, specs_txt, label_txt, search_code):
        global photo_data_exist
        if photo_data_exist == 0:
            self.lineEdit_5.setText(str(specs_txt))
            self.lineEdit_6.setText(str(label_txt))
        if i == 0:
            QMessageBox.information(self, '상품등록여부','이미지추출완료', QMessageBox.Yes | QMessageBox.Ok)
        elif i == 1:
            QMessageBox.information(self, '상품등록여부','이미지추출실패', QMessageBox.Yes | QMessageBox.Ok)
        elif i == 2:
            QMessageBox.information(self, '상품등록여부','중복된 상품이 없습니다', QMessageBox.Yes | QMessageBox.Ok)
        elif i == 3:
            QMessageBox.information(self, '상품등록여부','다른 상품으로 등록하세요', QMessageBox.Yes | QMessageBox.Ok)
    
    def clear_info(self):
        try:
            clear_photo()
            self.lineEdit.clear()
            if self.checkBox.isChecked():
                print('checked')
            else:
                self.lineEdit_2.clear()
            if self.checkBox_2.isChecked():
                print('checked')
            else:
                self.lineEdit_28.clear()
            if self.checkBox_3.isChecked():
                print('checked')
            else:
                self.lineEdit_3.clear()
                self.lineEdit_4.clear()
            self.lineEdit_9.clear()
            
            
            if self.checkBox_4.isChecked():
                print('checked')
            else:
                self.lineEdit_11.clear()
                self.lineEdit_14.clear()

            if self.checkBox_5.isChecked():
                print('checked')
            else:
                self.lineEdit_12.clear()
                self.lineEdit_15.clear()

            if self.checkBox_6.isChecked():
                print('checked')
            else:
                self.lineEdit_13.clear()
                self.lineEdit_16.clear()
            
            self.lineEdit_17.clear()
            self.lineEdit_18.clear()
            self.lineEdit_19.clear()
            self.lineEdit_20.clear()
            self.lineEdit_21.clear()

            if self.checkBox_7.isChecked():
                print('checked')
            else:
                self.plainTextEdit.clear()

            self.lineEdit_31.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.label_3.clear()
            QMessageBox.information(self, '초기화여부','성공', QMessageBox.Yes | QMessageBox.Ok)
        except:
            QMessageBox.information(self, '초기화여부','실패', QMessageBox.Yes | QMessageBox.Ok)

    @pyqtSlot(int)
    def alert_message2(self, i):
        self.pushButton_11.setEnabled(True)
        if i == 0:
            QMessageBox.information(self, '등록여부','실패', QMessageBox.Yes | QMessageBox.Ok)
        elif i == 1:
            clear_photo()
            self.lineEdit.clear()
            if self.checkBox.isChecked():
                print('checked')
            else:
                self.lineEdit_2.clear()
            if self.checkBox_2.isChecked():
                print('checked')
            else:
                self.lineEdit_28.clear()
            if self.checkBox_3.isChecked():
                print('checked')
            else:
                self.lineEdit_3.clear()
                self.lineEdit_4.clear()
            self.lineEdit_9.clear()
            
            
            if self.checkBox_4.isChecked():
                print('checked')
            else:
                self.lineEdit_11.clear()
                self.lineEdit_14.clear()

            if self.checkBox_5.isChecked():
                print('checked')
            else:
                self.lineEdit_12.clear()
                self.lineEdit_15.clear()

            if self.checkBox_6.isChecked():
                print('checked')
            else:
                self.lineEdit_13.clear()
                self.lineEdit_16.clear()
            
            self.lineEdit_17.clear()
            self.lineEdit_18.clear()
            self.lineEdit_19.clear()
            self.lineEdit_20.clear()
            self.lineEdit_21.clear()
            if self.checkBox_7.isChecked():
                print('checked')
            else:
                self.plainTextEdit.clear()

            self.lineEdit_31.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.label_3.clear()
            
            QMessageBox.information(self, '등록여부','완료', QMessageBox.Yes | QMessageBox.Ok)
    
    def openimageMenu(self):
        w.showimg()
        w.show()
    
    def calculating(self, target_m):
        #환율, 최소순익, 배송비, 관부가세, 마진율, 수수료/세금 순
        try:
            exchange_rate = int(self.lineEdit_22.text())
            least_benefit = int(self.lineEdit_25.text())
            send_money = int(self.lineEdit_23.text())
            tax1 = float(self.lineEdit_26.text())
            tax2 = float(self.lineEdit_27.text())
            margin_rate = float(self.lineEdit_24.text())

            tax1 = tax1/100 + 1
            tax2 = tax2/100 + 1
            margin_rate = margin_rate/100 + 1

            if target_m == self.lineEdit_3:
                target_money = int(self.lineEdit_3.text())
            elif target_m == self.lineEdit_17:
                target_money  = int(self.lineEdit_17.text())
            elif target_m == self.lineEdit_19:
                target_money  = int(self.lineEdit_19.text())

            middle_value = target_money * exchange_rate * margin_rate + least_benefit + send_money
            result_value = middle_value * tax1 * tax2
            
            print(result_value)
            mot, namuji = divmod(result_value, 100)

            result_value = int(mot * 100)

            if target_m == self.lineEdit_3:
                self.lineEdit_4.setText(str(result_value))
            elif target_m == self.lineEdit_17:
                self.lineEdit_18.setText(str(result_value))
            elif target_m == self.lineEdit_19:
                self.lineEdit_20.setText(str(result_value))

        except Exception as e:
            print(e)
            print('Cal')
            #QMessageBox.about(self, '입력값 오류','단가계산의 입력값을 확인해주세요')
    
    def save_extra_info(self):
        try:
            exchange_rate = int(self.lineEdit_22.text())
            least_benefit = int(self.lineEdit_25.text())
            send_money = int(self.lineEdit_23.text())
            tax1 = float(self.lineEdit_26.text())
            tax2 = float(self.lineEdit_27.text())
            margin_rate = float(self.lineEdit_24.text())

            f = open("C:\\CafeData\\info.txt",'w', encoding='utf-8')

            f.write(str(exchange_rate))
            f.write('\n')
            f.write(str(least_benefit))
            f.write('\n')
            f.write(str(send_money))
            f.write('\n')
            f.write(str(tax1))
            f.write('\n')
            f.write(str(tax2))
            f.write('\n')
            f.write(str(margin_rate))
            f.write('\n')

            f.close()

            QMessageBox.about(self, '알람','정보 저장완료')
        except:
            QMessageBox.about(self, '오류','입력값을 확인해주세요')

    def cal2(self):
        try:
            tar_a = int(self.lineEdit_18.text())
            tar_b = int(self.lineEdit_20.text())

            result = tar_a - tar_b

            self.lineEdit_21.setText(str(result))
        except Exception as e:
            print(e)
            QMessageBox.about(self, '입력값 오류','계산기1,2 값을 확인해주세요')

    def option_select(self, whichButton):
        global which_B

        if whichButton == self.pushButton_7:
            which_B = 1
        elif whichButton == self.pushButton_8:
            which_B = 2
        elif whichButton == self.pushButton_9:
            which_B = 3
        else:
            which_B = 3
        option_ui.load_file()
        MainWindow2.show()
    
    def detail_select(self):
        detail_ui.load_file()
        MainWindow5.show()
    
    def main_select(self):
        w2.showimg()
        w2.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 875)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 781, 821))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 31, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 611, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.checking_url)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 110, 291, 401))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(320, 170, 451, 341))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 20, 211, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_28.setGeometry(QtCore.QRect(80, 50, 81, 20))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 50, 61, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.textChanged.connect(lambda :self.calculating(self.lineEdit_3))
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(80, 240, 261, 91))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 520, 761, 111))
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(110, 20, 111, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_14.setGeometry(QtCore.QRect(250, 20, 431, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_12.setGeometry(QtCore.QRect(110, 50, 111, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_15.setGeometry(QtCore.QRect(250, 50, 431, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_13.setGeometry(QtCore.QRect(110, 80, 111, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        
        
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_16.setGeometry(QtCore.QRect(250, 80, 431, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda :self.option_select(self.pushButton_7))
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda :self.option_select(self.pushButton_8))
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 80, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda :self.option_select(self.pushButton_9))
        
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_4.setGeometry(QtCore.QRect(690, 20, 81, 21))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_5.setGeometry(QtCore.QRect(690, 50, 81, 21))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_6.setGeometry(QtCore.QRect(690, 80, 81, 21))
        self.checkBox_6.setObjectName("checkBox_6")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(700, 30, 71, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.checking_url)

        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 251, 291))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 330, 211, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.main_select)
        
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 41, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(170, 50, 41, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(310, 50, 41, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(360, 50, 81, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 41, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 80, 81, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(170, 80, 51, 21))
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 80, 61, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(300, 80, 51, 21))
        self.label_10.setObjectName("label_10")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(360, 80, 81, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 120, 61, 21))
        self.label_11.setObjectName("label_11")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(80, 120, 201, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 120, 51, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.getfile1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(80, 150, 201, 51))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.returnPressed.connect(self.get_info)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(80, 210, 201, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 150, 61, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(10, 210, 61, 21))
        self.label_13.setObjectName("label_13")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 150, 61, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.get_info)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 150, 61, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.openimageMenu)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 210, 51, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.getfile2)
        self.pushButton_detail = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_detail.setGeometry(QtCore.QRect(10, 240, 61, 21))
        self.pushButton_detail.setObjectName("label_14")
        self.pushButton_detail.clicked.connect(self.detail_select)
        
        self.label_25 = QtWidgets.QLabel(self.groupBox_3)
        self.label_25.setGeometry(QtCore.QRect(10, 50, 41, 21))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_3)
        self.label_26.setGeometry(QtCore.QRect(300, 20, 51, 21))
        self.label_26.setObjectName("label_26")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_31.setGeometry(QtCore.QRect(360, 20, 81, 20))
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(60, 20, 16, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_2.setGeometry(QtCore.QRect(60, 50, 16, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_3.setGeometry(QtCore.QRect(210, 50, 16, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_7.setGeometry(QtCore.QRect(60, 270, 16, 21))
        self.checkBox_7.setObjectName("checkBox_7")
        self.label_27 = QtWidgets.QLabel(self.groupBox_3)
        self.label_27.setGeometry(QtCore.QRect(350, 240, 98, 91))
        self.label_27.setObjectName("label_27")
        
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 640, 181, 131))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(10, 40, 51, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(10, 80, 51, 21))
        self.label_16.setObjectName("label_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_17.setGeometry(QtCore.QRect(70, 40, 101, 20))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_17.textChanged.connect(lambda :self.calculating(self.lineEdit_17))
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_18.setGeometry(QtCore.QRect(70, 80, 101, 20))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setGeometry(QtCore.QRect(200, 640, 181, 131))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_17 = QtWidgets.QLabel(self.groupBox_6)
        self.label_17.setGeometry(QtCore.QRect(10, 40, 51, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_6)
        self.label_18.setGeometry(QtCore.QRect(10, 80, 51, 21))
        self.label_18.setObjectName("label_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_19.setGeometry(QtCore.QRect(70, 40, 101, 20))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_19.textChanged.connect(lambda :self.calculating(self.lineEdit_19))
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_20.setGeometry(QtCore.QRect(70, 80, 101, 20))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_7.setGeometry(QtCore.QRect(390, 640, 81, 131))
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 20, 61, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.cal2)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_21.setGeometry(QtCore.QRect(10, 80, 61, 20))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_8.setGeometry(QtCore.QRect(480, 650, 291, 131))
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_19 = QtWidgets.QLabel(self.groupBox_8)
        self.label_19.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_8)
        self.label_20.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_8)
        self.label_21.setGeometry(QtCore.QRect(10, 80, 41, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_8)
        self.label_22.setGeometry(QtCore.QRect(140, 20, 51, 21))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_8)
        self.label_23.setGeometry(QtCore.QRect(140, 50, 51, 21))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_8)
        self.label_24.setGeometry(QtCore.QRect(140, 80, 71, 21))
        self.label_24.setObjectName("label_24")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_22.setGeometry(QtCore.QRect(70, 20, 61, 20))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_23.setGeometry(QtCore.QRect(70, 50, 61, 20))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_24.setGeometry(QtCore.QRect(70, 80, 61, 20))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_25.setGeometry(QtCore.QRect(220, 20, 61, 20))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_26.setGeometry(QtCore.QRect(220, 50, 61, 20))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_27.setGeometry(QtCore.QRect(220, 80, 61, 20))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 103, 271, 20))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.save_extra_info)
        
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setGeometry(QtCore.QRect(90, 780, 680, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.posting)

        self.clear_btn = QtWidgets.QPushButton(self.groupBox)
        self.clear_btn.setGeometry(QtCore.QRect(10, 780, 75, 31))
        self.clear_btn.setObjectName("pushButton_11")
        self.clear_btn.clicked.connect(self.clear_info)

        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_9.setGeometry(QtCore.QRect(320, 110, 451, 61))
        self.groupBox_9.setObjectName("groupBox_9")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_29.setGeometry(QtCore.QRect(60, 20, 121, 20))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_30.setGeometry(QtCore.QRect(250, 20, 171, 20))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_30.setEchoMode(QLineEdit.Password)
        self.label_2 = QtWidgets.QLabel(self.groupBox_9)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_9)
        self.label_4.setGeometry(QtCore.QRect(190, 20, 51, 21))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "상품설정"))
        self.label.setText(_translate("MainWindow", "URL"))
        self.pushButton.setText(_translate("MainWindow", "검증"))
        self.groupBox_2.setTitle(_translate("MainWindow", "이미지설정"))
        self.pushButton_2.setText(_translate("MainWindow", "대표이미지 변경"))
        self.groupBox_3.setTitle(_translate("MainWindow", "상품설정"))
        self.label_5.setText(_translate("MainWindow", "상품명"))
        self.label_6.setText(_translate("MainWindow", "구매가"))
        self.label_7.setText(_translate("MainWindow", "판매가"))
        self.label_8.setText(_translate("MainWindow", "셀러명"))
        self.label_9.setText(_translate("MainWindow", "자체분류"))
        self.label_10.setText(_translate("MainWindow", "작업코드"))
        self.label_11.setText(_translate("MainWindow", "상단이미지"))
        self.pushButton_3.setText(_translate("MainWindow", "입력"))
        self.label_12.setText(_translate("MainWindow", "상품이미지"))
        self.label_13.setText(_translate("MainWindow", "하단이미지"))
        self.pushButton_4.setText(_translate("MainWindow", "추출"))
        self.pushButton_5.setText(_translate("MainWindow", "수정"))
        self.pushButton_6.setText(_translate("MainWindow", "입력"))
        self.pushButton_detail.setText(_translate("MainWindow", "상세설명"))
        self.label_25.setText(_translate("MainWindow", "브랜드"))
        self.label_26.setText(_translate("MainWindow", "검색코드"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.label_27.setText(_translate("MainWindow", "SWEGO\n상품등록 프로그램\n202306112238"))
        self.groupBox_4.setTitle(_translate("MainWindow", "옵션"))
        self.pushButton_7.setText(_translate("MainWindow", "옵션1"))
        self.pushButton_8.setText(_translate("MainWindow", "옵션2"))
        self.pushButton_9.setText(_translate("MainWindow", "옵션3"))
        self.checkBox_4.setText(_translate("MainWindow", "No Reset"))
        self.checkBox_5.setText(_translate("MainWindow", "No Reset"))
        self.checkBox_6.setText(_translate("MainWindow", "No Reset"))
        self.groupBox_5.setTitle(_translate("MainWindow", "계산기1"))
        self.label_15.setText(_translate("MainWindow", "구매원가"))
        self.label_16.setText(_translate("MainWindow", "판매가"))
        self.groupBox_6.setTitle(_translate("MainWindow", "계산기2"))
        self.label_17.setText(_translate("MainWindow", "구매원가"))
        self.label_18.setText(_translate("MainWindow", "판매가"))
        self.groupBox_7.setTitle(_translate("MainWindow", "차액계산"))
        self.pushButton_10.setText(_translate("MainWindow", "계산"))
        self.groupBox_8.setTitle(_translate("MainWindow", "단가계산"))
        self.label_19.setText(_translate("MainWindow", "환율"))
        self.label_20.setText(_translate("MainWindow", "국제배송비"))
        self.label_21.setText(_translate("MainWindow", "마진율"))
        self.label_22.setText(_translate("MainWindow", "최소순익"))
        self.label_23.setText(_translate("MainWindow", "관부가세"))
        self.label_24.setText(_translate("MainWindow", "수수료/세금"))
        self.pushButton_12.setText(_translate("MainWindow", "저장"))
        self.pushButton_11.setText(_translate("MainWindow", "등록"))
        self.clear_btn.setText(_translate("MainWindow", "초기화"))
        self.groupBox_9.setTitle(_translate("MainWindow", "로그인정보"))
        self.label_2.setText(_translate("MainWindow", "아이디"))
        self.label_4.setText(_translate("MainWindow", "패스워드"))

        try:
            f = open("C:\\CafeData\\info.txt",'r', encoding='utf-8')

            data = f.readlines()
            f.close()

            for k in range(len(data)):
                data[k] = data[k].replace('\n', '')

            self.lineEdit_22.setText(data[0])
            self.lineEdit_25.setText(data[1])
            self.lineEdit_23.setText(data[2])
            self.lineEdit_26.setText(data[3])
            self.lineEdit_27.setText(data[4])
            self.lineEdit_24.setText(data[5])
        except:
            print('no save extra info')

        try:
            f = open("C:\\CafeData\\idps.txt", 'r', encoding='utf-8')

            data = f.readlines()
            f.close()

            for k in range(len(data)):
                data[k] = data[k].replace('\n', '')
            self.lineEdit_29.setText(data[0])
            self.lineEdit_30.setText(data[1])
        except:
            print('no save id ps data')

        try:
            f = open("C:\\CafeData\\code.txt", 'r', encoding='utf-8')

            data = f.readline()
            f.close()

            data = data.replace('\n', '')
            self.lineEdit_7.setText(data)
        except:
            print('no save id ps data')
        
class Ui_Option(QMainWindow):

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            MainWindow2.close()

        if e.key() in (Qt.Key_Return, Qt.Key_Enter):
            MainWindow2.close()

    def save_file(self):
        try:
            f = open("C:\\CafeData\\option1.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit.text()
            d2 = self.lineEditL.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data1')

        try:
            f = open("C:\\CafeData\\option2.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_2.text()
            d2 = self.lineEditL_2.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data2')

        try:
            f = open("C:\\CafeData\\option3.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_3.text()
            d2 = self.lineEditL_3.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data3')

        try:
            f = open("C:\\CafeData\\option4.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_4.text()
            d2 = self.lineEditL_4.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data4')
        
        try:
            f = open("C:\\CafeData\\option5.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_5.text()
            d2 = self.lineEditL_5.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data5')
        
        try:
            f = open("C:\\CafeData\\option6.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_6.text()
            d2 = self.lineEditL_6.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data6')

        try:
            f = open("C:\\CafeData\\option7.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_7.text()
            d2 = self.lineEditL_7.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data7')

        try:
            f = open("C:\\CafeData\\option8.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_8.text()
            d2 = self.lineEditL_8.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data8')
        
        try:
            f = open("C:\\CafeData\\option9.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_9.text()
            d2 = self.lineEditL_9.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data9')

        try:
            f = open("C:\\CafeData\\option10.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_10.text()
            d2 = self.lineEditL_10.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data10')

        try:
            f = open("C:\\CafeData\\option11.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_11.text()
            d2 = self.lineEditL_11.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data11')

        try:
            f = open("C:\\CafeData\\option12.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_12.text()
            d2 = self.lineEditL_12.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data12')

        try:
            f = open("C:\\CafeData\\option13.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_13.text()
            d2 = self.lineEditL_13.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data13')

        try:
            f = open("C:\\CafeData\\option14.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_14.text()
            d2 = self.lineEditL_14.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data14')
        
        try:
            f = open("C:\\CafeData\\option15.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_15.text()
            d2 = self.lineEditL_15.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data15')
        
        try:
            f = open("C:\\CafeData\\option16.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_16.text()
            d2 = self.lineEditL_16.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data16')

        try:
            f = open("C:\\CafeData\\option17.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_17.text()
            d2 = self.lineEditL_17.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data17')
        
        try:
            f = open("C:\\CafeData\\option18.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_18.text()
            d2 = self.lineEditL_18.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data18')

        try:
            f = open("C:\\CafeData\\option19.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_19.text()
            d2 = self.lineEditL_19.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data19')

        try:
            f = open("C:\\CafeData\\option20.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_20.text()
            d2 = self.lineEditL_20.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data20')

        try:
            f = open("C:\\CafeData\\option21.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_21.text()
            d2 = self.lineEditL_21.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data21')
        
        try:
            f = open("C:\\CafeData\\option22.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_22.text()
            d2 = self.lineEditL_22.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data22')
        try:
            f = open("C:\\CafeData\\option23.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_23.text()
            d2 = self.lineEditL_23.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data23')

        try:
            f = open("C:\\CafeData\\option24.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_24.text()
            d2 = self.lineEditL_24.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data24')
        
        try:
            f = open("C:\\CafeData\\option25.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_25.text()
            d2 = self.lineEditL_25.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data25')

        try:
            f = open("C:\\CafeData\\option26.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_26.text()
            d2 = self.lineEditL_26.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data26')

        try:
            f = open("C:\\CafeData\\option27.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_27.text()
            d2 = self.lineEditL_27.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data27')

        try:
            f = open("C:\\CafeData\\option28.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_28.text()
            d2 = self.lineEditL_28.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data28')

        try:
            f = open("C:\\CafeData\\option29.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_29.text()
            d2 = self.lineEditL_29.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data29')

        try:
            f = open("C:\\CafeData\\option30.txt", 'w', encoding='utf-8')
            d1 = self.lineEdit_30.text()
            d2 = self.lineEditL_30.text()

            f.write(d1)
            f.write('\n')
            f.write(d2)
            f.write('\n')

            f.close()
        except:
            print('no data30')
        QMessageBox.about(self, '알림', '저장되었습니다')

    def load_file(self):
        try:
            f = open("C:\\CafeData\\option1.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit.setText(data[0])
            self.lineEditL.setText(data[1])
            f.close()
        except:
            print('no data1')

        try:
            f = open("C:\\CafeData\\option2.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_2.setText(data[0])
            self.lineEditL_2.setText(data[1])
            f.close()
        except:
            print('no data2')

        try:
            f = open("C:\\CafeData\\option3.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_3.setText(data[0])
            self.lineEditL_3.setText(data[1])
            f.close()
        except:
            print('no data3')

        try:
            f = open("C:\\CafeData\\option4.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_4.setText(data[0])
            self.lineEditL_4.setText(data[1])
            f.close()
        except:
            print('no data4')

        try:
            f = open("C:\\CafeData\\option5.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_5.setText(data[0])
            self.lineEditL_5.setText(data[1])
            f.close()
        except:
            print('no data5')

        try:
            f = open("C:\\CafeData\\option6.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_6.setText(data[0])
            self.lineEditL_6.setText(data[1])
            f.close()
        except:
            print('no data6')

        try:
            f = open("C:\\CafeData\\option7.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_7.setText(data[0])
            self.lineEditL_7.setText(data[1])
            f.close()
        except:
            print('no data7')

        try:
            f = open("C:\\CafeData\\option8.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_8.setText(data[0])
            self.lineEditL_8.setText(data[1])
            f.close()
        except:
            print('no data8')

        try:
            f = open("C:\\CafeData\\option9.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_9.setText(data[0])
            self.lineEditL_9.setText(data[1])
            f.close()
        except:
            print('no data9')

        try:
            f = open("C:\\CafeData\\option10.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_10.setText(data[0])
            self.lineEditL_10.setText(data[1])
            f.close()
        except:
            print('no data10')

        try:
            f = open("C:\\CafeData\\option11.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_11.setText(data[0])
            self.lineEditL_11.setText(data[1])
            f.close()
        except:
            print('no data11')

        try:
            f = open("C:\\CafeData\\option12.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_12.setText(data[0])
            self.lineEditL_12.setText(data[1])
            f.close()
        except:
            print('no data12')

        try:
            f = open("C:\\CafeData\\option13.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_13.setText(data[0])
            self.lineEditL_13.setText(data[1])
            f.close()
        except:
            print('no data13')

        try:
            f = open("C:\\CafeData\\option14.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_14.setText(data[0])
            self.lineEditL_14.setText(data[1])
            f.close()
        except:
            print('no data14')

        try:
            f = open("C:\\CafeData\\option15.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_15.setText(data[0])
            self.lineEditL_15.setText(data[1])
            f.close()
        except:
            print('no data15')
        
        try:
            f = open("C:\\CafeData\\option16.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_16.setText(data[0])
            self.lineEditL_16.setText(data[1])
            f.close()
        except:
            print('no data16')

        try:
            f = open("C:\\CafeData\\option17.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_17.setText(data[0])
            self.lineEditL_17.setText(data[1])
            f.close()
        except:
            print('no data17')

        try:
            f = open("C:\\CafeData\\option18.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_18.setText(data[0])
            self.lineEditL_18.setText(data[1])
            f.close()
        except:
            print('no data18')

        try:
            f = open("C:\\CafeData\\option19.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_19.setText(data[0])
            self.lineEditL_19.setText(data[1])
            f.close()
        except:
            print('no data19')

        try:
            f = open("C:\\CafeData\\option20.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_20.setText(data[0])
            self.lineEditL_20.setText(data[1])
            f.close()
        except:
            print('no data20')

        try:
            f = open("C:\\CafeData\\option21.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_21.setText(data[0])
            self.lineEditL_21.setText(data[1])
            f.close()
        except:
            print('no data21')

        try:
            f = open("C:\\CafeData\\option22.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_22.setText(data[0])
            self.lineEditL_22.setText(data[1])
            f.close()
        except:
            print('no data22')

        try:
            f = open("C:\\CafeData\\option23.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_23.setText(data[0])
            self.lineEditL_23.setText(data[1])
            f.close()
        except:
            print('no data23')

        try:
            f = open("C:\\CafeData\\option24.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_24.setText(data[0])
            self.lineEditL_24.setText(data[1])
            f.close()
        except:
            print('no data24')

        try:
            f = open("C:\\CafeData\\option25.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_25.setText(data[0])
            self.lineEditL_25.setText(data[1])
            f.close()
        except:
            print('no data25')

        try:
            f = open("C:\\CafeData\\option26.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_26.setText(data[0])
            self.lineEditL_26.setText(data[1])
            f.close()
        except:
            print('no data26')

        try:
            f = open("C:\\CafeData\\option27.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_27.setText(data[0])
            self.lineEditL_27.setText(data[1])
            f.close()
        except:
            print('no data27')

        try:
            f = open("C:\\CafeData\\option28.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_28.setText(data[0])
            self.lineEditL_28.setText(data[1])
            f.close()
        except:
            print('no data28')

        try:
            f = open("C:\\CafeData\\option29.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_29.setText(data[0])
            self.lineEditL_29.setText(data[1])
            f.close()
        except:
            print('no data29')

        try:
            f = open("C:\\CafeData\\option30.txt", 'r', encoding='utf-8')
            data = f.readlines()
            for i in range(len(data)):
                data[i] = data[i].replace('\n', '')
            self.lineEdit_30.setText(data[0])
            self.lineEditL_30.setText(data[1])
            f.close()
        except:
            print('no data30')
    
    def exit_button(self):
        MainWindow2.close()
    
    def insert_info(self, which_button):
        if which_B == 1:
            insert1 = ui.lineEdit_11
            insert2 = ui.lineEdit_14
        elif which_B == 2:
            insert1 = ui.lineEdit_12
            insert2 = ui.lineEdit_15
        elif which_B == 3:
            insert1 = ui.lineEdit_13
            insert2 = ui.lineEdit_16
        
        if which_button == self.pushButton:
            insert1.setText(self.lineEdit.text())
            insert2.setText(self.lineEditL.text())
        elif which_button == self.pushButton_2:
            insert1.setText(self.lineEdit_2.text())
            insert2.setText(self.lineEditL_2.text())
        elif which_button == self.pushButton_3:
            insert1.setText(self.lineEdit_3.text())
            insert2.setText(self.lineEditL_3.text())
        elif which_button == self.pushButton_4:
            insert1.setText(self.lineEdit_4.text())
            insert2.setText(self.lineEditL_4.text())
        elif which_button == self.pushButton_5:
            insert1.setText(self.lineEdit_5.text())
            insert2.setText(self.lineEditL_5.text())
        elif which_button == self.pushButton_6:
            insert1.setText(self.lineEdit_6.text())
            insert2.setText(self.lineEditL_6.text())
        elif which_button == self.pushButton_7:
            insert1.setText(self.lineEdit_7.text())
            insert2.setText(self.lineEditL_7.text())
        elif which_button == self.pushButton_8:
            insert1.setText(self.lineEdit_8.text())
            insert2.setText(self.lineEditL_8.text())
        elif which_button == self.pushButton_9:
            insert1.setText(self.lineEdit_9.text())
            insert2.setText(self.lineEditL_9.text())
        elif which_button == self.pushButton_10:
            insert1.setText(self.lineEdit_10.text())
            insert2.setText(self.lineEditL_10.text())
        elif which_button == self.pushButton_11:
            insert1.setText(self.lineEdit_11.text())
            insert2.setText(self.lineEditL_11.text())
        elif which_button == self.pushButton_12:
            insert1.setText(self.lineEdit_12.text())
            insert2.setText(self.lineEditL_12.text())
        elif which_button == self.pushButton_13:
            insert1.setText(self.lineEdit_13.text())
            insert2.setText(self.lineEditL_13.text())
        elif which_button == self.pushButton_14:
            insert1.setText(self.lineEdit_14.text())
            insert2.setText(self.lineEditL_14.text())
        elif which_button == self.pushButton_15:
            insert1.setText(self.lineEdit_15.text())
            insert2.setText(self.lineEditL_15.text())
        elif which_button == self.pushButton_16:
            insert1.setText(self.lineEdit_16.text())
            insert2.setText(self.lineEditL_16.text())
        elif which_button == self.pushButton_17:
            insert1.setText(self.lineEdit_17.text())
            insert2.setText(self.lineEditL_17.text())
        elif which_button == self.pushButton_18:
            insert1.setText(self.lineEdit_18.text())
            insert2.setText(self.lineEditL_18.text())
        elif which_button == self.pushButton_19:
            insert1.setText(self.lineEdit_19.text())
            insert2.setText(self.lineEditL_19.text())
        elif which_button == self.pushButton_20:
            insert1.setText(self.lineEdit_20.text())
            insert2.setText(self.lineEditL_20.text())
        elif which_button == self.pushButton_21:
            insert1.setText(self.lineEdit_21.text())
            insert2.setText(self.lineEditL_21.text())
        elif which_button == self.pushButton_22:
            insert1.setText(self.lineEdit_22.text())
            insert2.setText(self.lineEditL_22.text())
        elif which_button == self.pushButton_23:
            insert1.setText(self.lineEdit_23.text())
            insert2.setText(self.lineEditL_23.text())
        elif which_button == self.pushButton_24:
            insert1.setText(self.lineEdit_24.text())
            insert2.setText(self.lineEditL_24.text())
        elif which_button == self.pushButton_25:
            insert1.setText(self.lineEdit_25.text())
            insert2.setText(self.lineEditL_25.text())
        elif which_button == self.pushButton_26:
            insert1.setText(self.lineEdit_26.text())
            insert2.setText(self.lineEditL_26.text())
        elif which_button == self.pushButton_27:
            insert1.setText(self.lineEdit_27.text())
            insert2.setText(self.lineEditL_27.text())
        elif which_button == self.pushButton_28:
            insert1.setText(self.lineEdit_28.text())
            insert2.setText(self.lineEditL_28.text())
        elif which_button == self.pushButton_29:
            insert1.setText(self.lineEdit_29.text())
            insert2.setText(self.lineEditL_29.text())
        elif which_button == self.pushButton_30:
            insert1.setText(self.lineEdit_30.text())
            insert2.setText(self.lineEditL_30.text())
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(700, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.keyPressEvent = self.keyPressEvent

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 0, 670, 400))
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(10, 0, 670, 920))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 101, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 40, 101, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 70, 101, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 100, 101, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 130, 101, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 160, 101, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_7.setGeometry(QtCore.QRect(20, 190, 101, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_8.setGeometry(QtCore.QRect(20, 220, 101, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setGeometry(QtCore.QRect(20, 250, 101, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_10.setGeometry(QtCore.QRect(20, 280, 101, 21))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_11.setGeometry(QtCore.QRect(20, 310, 101, 21))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_12.setGeometry(QtCore.QRect(20, 340, 101, 21))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_13.setGeometry(QtCore.QRect(20, 370, 101, 21))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_14.setGeometry(QtCore.QRect(20, 400, 101, 21))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_15.setGeometry(QtCore.QRect(20, 430, 101, 21))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_16.setGeometry(QtCore.QRect(20, 460, 101, 21))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_17.setGeometry(QtCore.QRect(20, 490, 101, 21))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_18.setGeometry(QtCore.QRect(20, 520, 101, 21))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_19.setGeometry(QtCore.QRect(20, 550, 101, 21))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_20.setGeometry(QtCore.QRect(20, 580, 101, 21))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_21.setGeometry(QtCore.QRect(20, 610, 101, 21))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_22.setGeometry(QtCore.QRect(20, 640, 101, 21))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_23.setGeometry(QtCore.QRect(20, 670, 101, 21))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_24.setGeometry(QtCore.QRect(20, 700, 101, 21))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_25.setGeometry(QtCore.QRect(20, 730, 101, 21))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_26.setGeometry(QtCore.QRect(20, 760, 101, 21))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_27.setGeometry(QtCore.QRect(20, 790, 101, 21))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_28.setGeometry(QtCore.QRect(20, 820, 101, 21))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_29.setGeometry(QtCore.QRect(20, 850, 101, 21))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_30.setGeometry(QtCore.QRect(20, 880, 101, 21))
        self.lineEdit_30.setObjectName("lineEdit_30")


        self.lineEditL = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL.setGeometry(QtCore.QRect(140, 10, 361, 21))
        self.lineEditL.setObjectName("lineEditL")
        self.lineEditL_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_2.setGeometry(QtCore.QRect(140, 40, 361, 21))
        self.lineEditL_2.setObjectName("lineEditL_2")
        self.lineEditL_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_3.setGeometry(QtCore.QRect(140, 70, 361, 21))
        self.lineEditL_3.setObjectName("lineEditL_3")
        self.lineEditL_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_4.setGeometry(QtCore.QRect(140, 100, 361, 21))
        self.lineEditL_4.setObjectName("lineEditL_4")
        self.lineEditL_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_5.setGeometry(QtCore.QRect(140, 130, 361, 21))
        self.lineEditL_5.setObjectName("lineEditL_5")
        self.lineEditL_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_6.setGeometry(QtCore.QRect(140, 160, 361, 21))
        self.lineEditL_6.setObjectName("lineEditL_6")
        self.lineEditL_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_7.setGeometry(QtCore.QRect(140, 190, 361, 21))
        self.lineEditL_7.setObjectName("lineEditL_7")
        self.lineEditL_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_8.setGeometry(QtCore.QRect(140, 220, 361, 21))
        self.lineEditL_8.setObjectName("lineEditL_8")
        self.lineEditL_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_9.setGeometry(QtCore.QRect(140, 250, 361, 21))
        self.lineEditL_9.setObjectName("lineEditL_9")
        self.lineEditL_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_10.setGeometry(QtCore.QRect(140, 280, 361, 21))
        self.lineEditL_10.setObjectName("lineEditL_10")
        self.lineEditL_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_11.setGeometry(QtCore.QRect(140, 310, 361, 21))
        self.lineEditL_11.setObjectName("lineEditL_11")
        self.lineEditL_12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_12.setGeometry(QtCore.QRect(140, 340, 361, 21))
        self.lineEditL_12.setObjectName("lineEditL_12")
        self.lineEditL_13 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_13.setGeometry(QtCore.QRect(140, 370, 361, 21))
        self.lineEditL_13.setObjectName("lineEditL_13")

        self.lineEditL_14 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_14.setGeometry(QtCore.QRect(140, 400, 361, 21))
        self.lineEditL_14.setObjectName("lineEditL_14")
        self.lineEditL_15 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_15.setGeometry(QtCore.QRect(140, 430, 361, 21))
        self.lineEditL_15.setObjectName("lineEditL_15")
        self.lineEditL_16 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_16.setGeometry(QtCore.QRect(140, 460, 361, 21))
        self.lineEditL_16.setObjectName("lineEditL_16")
        self.lineEditL_17 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_17.setGeometry(QtCore.QRect(140, 490, 361, 21))
        self.lineEditL_17.setObjectName("lineEditL_17")
        self.lineEditL_18 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_18.setGeometry(QtCore.QRect(140, 520, 361, 21))
        self.lineEditL_18.setObjectName("lineEditL_18")
        self.lineEditL_19 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_19.setGeometry(QtCore.QRect(140, 550, 361, 21))
        self.lineEditL_19.setObjectName("lineEditL_19")
        self.lineEditL_20 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_20.setGeometry(QtCore.QRect(140, 580, 361, 21))
        self.lineEditL_20.setObjectName("lineEditL_20")
        self.lineEditL_21 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_21.setGeometry(QtCore.QRect(140, 610, 361, 21))
        self.lineEditL_21.setObjectName("lineEditL_21")
        self.lineEditL_22 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_22.setGeometry(QtCore.QRect(140, 640, 361, 21))
        self.lineEditL_22.setObjectName("lineEditL_22")
        self.lineEditL_23 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_23.setGeometry(QtCore.QRect(140, 670, 361, 21))
        self.lineEditL_23.setObjectName("lineEditL_23")
        self.lineEditL_24 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_24.setGeometry(QtCore.QRect(140, 700, 361, 21))
        self.lineEditL_24.setObjectName("lineEditL_24")
        self.lineEditL_25 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_25.setGeometry(QtCore.QRect(140, 730, 361, 21))
        self.lineEditL_25.setObjectName("lineEditL_25")
        self.lineEditL_26 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_26.setGeometry(QtCore.QRect(140, 760, 361, 21))
        self.lineEditL_26.setObjectName("lineEditL_26")
        self.lineEditL_27 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_27.setGeometry(QtCore.QRect(140, 790, 361, 21))
        self.lineEditL_27.setObjectName("lineEditL_27")
        self.lineEditL_28 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_28.setGeometry(QtCore.QRect(140, 820, 361, 21))
        self.lineEditL_28.setObjectName("lineEditL_28")
        self.lineEditL_29 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_29.setGeometry(QtCore.QRect(140, 850, 361, 21))
        self.lineEditL_29.setObjectName("lineEditL_29")
        self.lineEditL_30 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditL_30.setGeometry(QtCore.QRect(140, 880, 361, 21))
        self.lineEditL_30.setObjectName("lineEditL_30")

        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(520, 10, 113, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda :self.insert_info(self.pushButton))
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 40, 113, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda :self.insert_info(self.pushButton_2))
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 70, 113, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda :self.insert_info(self.pushButton_3))
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 100, 113, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda :self.insert_info(self.pushButton_4))
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setGeometry(QtCore.QRect(520, 130, 113, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda :self.insert_info(self.pushButton_5))
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setGeometry(QtCore.QRect(520, 160, 113, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda :self.insert_info(self.pushButton_6))
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setGeometry(QtCore.QRect(520, 190, 113, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda :self.insert_info(self.pushButton_7))
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setGeometry(QtCore.QRect(520, 220, 113, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda :self.insert_info(self.pushButton_8))
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setGeometry(QtCore.QRect(520, 250, 113, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda :self.insert_info(self.pushButton_9))
        self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setGeometry(QtCore.QRect(520, 280, 113, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(lambda :self.insert_info(self.pushButton_10))
        self.pushButton_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_11.setGeometry(QtCore.QRect(520, 310, 113, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(lambda :self.insert_info(self.pushButton_11))
        self.pushButton_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_12.setGeometry(QtCore.QRect(520, 340, 113, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(lambda :self.insert_info(self.pushButton_12))
        self.pushButton_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_13.setGeometry(QtCore.QRect(520, 370, 113, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(lambda :self.insert_info(self.pushButton_13))

        self.pushButton_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_14.setGeometry(QtCore.QRect(520, 400, 113, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(lambda :self.insert_info(self.pushButton_14))
        self.pushButton_15 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_15.setGeometry(QtCore.QRect(520, 430, 113, 31))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(lambda :self.insert_info(self.pushButton_15))
        self.pushButton_16 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_16.setGeometry(QtCore.QRect(520, 460, 113, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(lambda :self.insert_info(self.pushButton_16))
        self.pushButton_17 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_17.setGeometry(QtCore.QRect(520, 490, 113, 31))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(lambda :self.insert_info(self.pushButton_17))
        self.pushButton_18 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_18.setGeometry(QtCore.QRect(520, 520, 113, 31))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(lambda :self.insert_info(self.pushButton_18))
        self.pushButton_19 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_19.setGeometry(QtCore.QRect(520, 550, 113, 31))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(lambda :self.insert_info(self.pushButton_19))
        self.pushButton_20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_20.setGeometry(QtCore.QRect(520, 580, 113, 31))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.clicked.connect(lambda :self.insert_info(self.pushButton_20))
        self.pushButton_21 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_21.setGeometry(QtCore.QRect(520, 610, 113, 31))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_21.clicked.connect(lambda :self.insert_info(self.pushButton_21))
        self.pushButton_22 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_22.setGeometry(QtCore.QRect(520, 640, 113, 31))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_22.clicked.connect(lambda :self.insert_info(self.pushButton_22))
        self.pushButton_23 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_23.setGeometry(QtCore.QRect(520, 670, 113, 31))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.clicked.connect(lambda :self.insert_info(self.pushButton_23))
        self.pushButton_24 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_24.setGeometry(QtCore.QRect(520, 700, 113, 31))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_24.clicked.connect(lambda :self.insert_info(self.pushButton_24))
        self.pushButton_25 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_25.setGeometry(QtCore.QRect(520, 730, 113, 31))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_25.clicked.connect(lambda :self.insert_info(self.pushButton_25))
        self.pushButton_26 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_26.setGeometry(QtCore.QRect(520, 760, 113, 31))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_26.clicked.connect(lambda :self.insert_info(self.pushButton_26))
        self.pushButton_27 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_27.setGeometry(QtCore.QRect(520, 790, 113, 31))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_27.clicked.connect(lambda :self.insert_info(self.pushButton_27))
        self.pushButton_28 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_28.setGeometry(QtCore.QRect(520, 820, 113, 31))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_28.clicked.connect(lambda :self.insert_info(self.pushButton_28))
        self.pushButton_29 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_29.setGeometry(QtCore.QRect(520, 850, 113, 31))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_29.clicked.connect(lambda :self.insert_info(self.pushButton_29))
        self.pushButton_30 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_30.setGeometry(QtCore.QRect(520, 880, 113, 31))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_30.clicked.connect(lambda :self.insert_info(self.pushButton_30))
    
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_31.setGeometry(QtCore.QRect(190, 410, 113, 32))
        self.pushButton_31.setObjectName("pushButton_32")
        self.pushButton_31.clicked.connect(self.save_file)

        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setGeometry(QtCore.QRect(310, 410, 113, 32))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_32.clicked.connect(self.exit_button)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "옵션창"))
        self.pushButton.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_2.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_3.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_4.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_5.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_6.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_7.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_8.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_9.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_10.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_11.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_12.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_13.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_14.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_15.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_16.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_17.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_18.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_19.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_20.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_21.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_22.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_23.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_24.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_25.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_26.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_27.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_28.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_29.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_30.setText(_translate("MainWindow", "적용하기"))

        self.pushButton_31.setText(_translate("MainWindow", "저장"))
        self.pushButton_32.setText(_translate("MainWindow", "닫기"))

        self.load_file()

class Ui_Detail(QMainWindow):
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            MainWindow5.close()

        if e.key() in (Qt.Key_Return, Qt.Key_Enter):
            MainWindow5.close()

    def save_file(self):
        try:
            f = open("C:\\CafeData\\detail1.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data1')

        try:
            f = open("C:\\CafeData\\detail2.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit_2.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data2')

        try:
            f = open("C:\\CafeData\\detail3.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit_3.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data3')

        try:
            f = open("C:\\CafeData\\detail4.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit_4.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data4')

        try:
            f = open("C:\\CafeData\\detail5.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit_5.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data5')

        try:
            f = open("C:\\CafeData\\detail6.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit_6.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data6')

        try:
            f = open("C:\\CafeData\\detail7.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit_7.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data7')

        try:
            f = open("C:\\CafeData\\detail8.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit_8.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data8')

        try:
            f = open("C:\\CafeData\\detail9.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit_9.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data9')

        try:
            f = open("C:\\CafeData\\detail10.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit_10.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data10')

        try:
            f = open("C:\\CafeData\\detail11.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit_11.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data11')

        try:
            f = open("C:\\CafeData\\detail12.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit_12.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data12')

        try:
            f = open("C:\\CafeData\\detail13.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit_13.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data13')

        try:
            f = open("C:\\CafeData\\detail14.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit_14.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data14')

        try:
            f = open("C:\\CafeData\\detail15.txt", 'w', encoding='utf-8')
            d1 = self.plainTextEdit_15.toPlainText()
            f.write(d1)
            f.close()
        except:
            print('no data15')
    
    def load_file(self):
        try:
            f = open("C:\\CafeData\\detail1.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit.setPlainText(data_str)
            f.close()
        except:
            print('no data1')

        try:
            f = open("C:\\CafeData\\detail2.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit_2.setPlainText(data_str)
            f.close()
        except:
            print('no data2')

        try:
            f = open("C:\\CafeData\\detail3.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit_3.setPlainText(data_str)
            f.close()
        except:
            print('no data3')

        try:
            f = open("C:\\CafeData\\detail4.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit_4.setPlainText(data_str)
            f.close()
        except:
            print('no data4')

        try:
            f = open("C:\\CafeData\\detail5.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit_5.setPlainText(data_str)
            f.close()
        except:
            print('no data5')
        try:
            f = open("C:\\CafeData\\detail6.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit_6.setPlainText(data_str)
            f.close()
        except:
            print('no data6')

        try:
            f = open("C:\\CafeData\\detail7.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit_7.setPlainText(data_str)
            f.close()
        except:
            print('no data7')

        try:
            f = open("C:\\CafeData\\detail8.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit_8.setPlainText(data_str)
            f.close()
        except:
            print('no data8')

        try:
            f = open("C:\\CafeData\\detail9.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit_9.setPlainText(data_str)
            f.close()
        except:
            print('no data9')

        try:
            f = open("C:\\CafeData\\detail10.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit_10.setPlainText(data_str)
            f.close()
        except:
            print('no data10')

        try:
            f = open("C:\\CafeData\\detail11.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit_11.setPlainText(data_str)
            f.close()
        except:
            print('no data11')

        try:
            f = open("C:\\CafeData\\detail12.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit_12.setPlainText(data_str)
            f.close()
        except:
            print('no data12')

        try:
            f = open("C:\\CafeData\\detail13.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit_13.setPlainText(data_str)
            f.close()
        except:
            print('no data13')

        try:
            f = open("C:\\CafeData\\detail14.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit_14.setPlainText(data_str)
            f.close()
        except:
            print('no data14')

        try:
            f = open("C:\\CafeData\\detail15.txt", 'r', encoding='utf-8')
            data = f.readlines()
            data_str = ''
            threshold_list = len(data) - 1
            for i in range(len(data)):
                if threshold_list == i:
                    data_str = data_str + data[i].replace('\n', '')
                else:
                    data_str = data_str + data[i]
            self.plainTextEdit_15.setPlainText(data_str)
            f.close()
        except:
            print('no data15')

    def exit_button(self):
        MainWindow5.close()
    
    def insert_info(self, which_button):
        insert1 = ui.plainTextEdit
        if which_button == self.pushButton:
            insert1.setPlainText(self.plainTextEdit.toPlainText())
        elif which_button == self.pushButton_2:
            insert1.setPlainText(self.plainTextEdit_2.toPlainText())
        elif which_button == self.pushButton_3:
            insert1.setPlainText(self.plainTextEdit_3.toPlainText())
        elif which_button == self.pushButton_4:
            insert1.setPlainText(self.plainTextEdit_4.toPlainText())
        elif which_button == self.pushButton_5:
            insert1.setPlainText(self.plainTextEdit_5.toPlainText())
        elif which_button == self.pushButton_6:
            insert1.setPlainText(self.plainTextEdit_6.toPlainText())
        elif which_button == self.pushButton_7:
            insert1.setPlainText(self.plainTextEdit_7.toPlainText())
        elif which_button == self.pushButton_8:
            insert1.setPlainText(self.plainTextEdit_8.toPlainText())
        elif which_button == self.pushButton_9:
            insert1.setPlainText(self.plainTextEdit_9.toPlainText())
        elif which_button == self.pushButton_10:
            insert1.setPlainText(self.plainTextEdit_10.toPlainText())
        elif which_button == self.pushButton_11:
            insert1.setPlainText(self.plainTextEdit_11.toPlainText())
        elif which_button == self.pushButton_12:
            insert1.setPlainText(self.plainTextEdit_12.toPlainText())
        elif which_button == self.pushButton_13:
            insert1.setPlainText(self.plainTextEdit_13.toPlainText())
        elif which_button == self.pushButton_14:
            insert1.setPlainText(self.plainTextEdit_14.toPlainText())
        elif which_button == self.pushButton_15:
            insert1.setPlainText(self.plainTextEdit_15.toPlainText())
   
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 487)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.keyPressEvent = self.keyPressEvent

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 740, 371))
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 739, 760))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 621, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(640, 10, 75, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda :self.insert_info(self.pushButton))
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 60, 621, 41))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(10, 110, 621, 41))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(10, 160, 621, 41))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(10, 210, 621, 41))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(10, 260, 621, 41))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(10, 310, 621, 41))
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")

        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(10, 360, 621, 41))
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.plainTextEdit_9 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_9.setGeometry(QtCore.QRect(10, 410, 621, 41))
        self.plainTextEdit_9.setObjectName("plainTextEdit_9")
        self.plainTextEdit_10 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_10.setGeometry(QtCore.QRect(10, 460, 621, 41))
        self.plainTextEdit_10.setObjectName("plainTextEdit_10")
        self.plainTextEdit_11 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_11.setGeometry(QtCore.QRect(10, 510, 621, 41))
        self.plainTextEdit_11.setObjectName("plainTextEdit_11")
        self.plainTextEdit_12 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_12.setGeometry(QtCore.QRect(10, 560, 621, 41))
        self.plainTextEdit_12.setObjectName("plainTextEdit_12")
        self.plainTextEdit_13 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_13.setGeometry(QtCore.QRect(10, 610, 621, 41))
        self.plainTextEdit_13.setObjectName("plainTextEdit_13")
        self.plainTextEdit_14 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_14.setGeometry(QtCore.QRect(10, 660, 621, 41))
        self.plainTextEdit_14.setObjectName("plainTextEdit_14")
        self.plainTextEdit_15 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_15.setGeometry(QtCore.QRect(10, 710, 621, 41))
        self.plainTextEdit_15.setObjectName("plainTextEdit_15")

        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 60, 75, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda :self.insert_info(self.pushButton_2))
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 110, 75, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda :self.insert_info(self.pushButton_3))
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 160, 75, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda :self.insert_info(self.pushButton_4))
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setGeometry(QtCore.QRect(640, 210, 75, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda :self.insert_info(self.pushButton_5))
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 260, 75, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda :self.insert_info(self.pushButton_6))
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setGeometry(QtCore.QRect(640, 310, 75, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda :self.insert_info(self.pushButton_7))
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setGeometry(QtCore.QRect(640, 360, 75, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda :self.insert_info(self.pushButton_8))
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setGeometry(QtCore.QRect(640, 410, 75, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda :self.insert_info(self.pushButton_9))
        self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setGeometry(QtCore.QRect(640, 460, 75, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(lambda :self.insert_info(self.pushButton_10))
        self.pushButton_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_11.setGeometry(QtCore.QRect(640, 510, 75, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(lambda :self.insert_info(self.pushButton_11))
        self.pushButton_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_12.setGeometry(QtCore.QRect(640, 560, 75, 41))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(lambda :self.insert_info(self.pushButton_12))
        self.pushButton_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_13.setGeometry(QtCore.QRect(640, 610, 75, 41))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(lambda :self.insert_info(self.pushButton_13))
        self.pushButton_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_14.setGeometry(QtCore.QRect(640, 660, 75, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(lambda :self.insert_info(self.pushButton_14))
        self.pushButton_15 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_15.setGeometry(QtCore.QRect(640, 710, 75, 41))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(lambda :self.insert_info(self.pushButton_15))

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(270, 400, 75, 31))
        self.pushButton_save.setObjectName("pushButton_8")
        self.pushButton_save.clicked.connect(self.save_file)
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(400, 400, 75, 31))
        self.pushButton_exit.setObjectName("pushButton_9")
        self.pushButton_exit.clicked.connect(self.exit_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "상세설명"))
        self.pushButton.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_2.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_3.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_4.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_5.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_6.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_7.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_8.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_9.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_10.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_11.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_12.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_13.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_14.setText(_translate("MainWindow", "적용하기"))
        self.pushButton_15.setText(_translate("MainWindow", "적용하기"))


        self.pushButton_save.setText(_translate("MainWindow", "저장"))
        self.pushButton_exit.setText(_translate("MainWindow", "닫기"))

class ClassUi(object):

    def setup(self, MainW):
        MainW.setObjectName("MainW")
        MainW.setFixedSize(600,500)

        self.mainlayout = QtWidgets.QVBoxLayout()

        self.centralwidget = QtWidgets.QWidget(MainW)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayout(self.mainlayout)
        MainW.setCentralWidget(self.centralwidget)

        self.scrollwidget = QtWidgets.QScrollArea()
        self.mainlayout.addWidget(self.scrollwidget)
        self.scrollwidget.setWidgetResizable(True)
        self.scrollwidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.scrollgrid = QtWidgets.QGridLayout()

        self.widgetforscroll = QtWidgets.QWidget()
        self.widgetforscroll.setLayout(self.scrollgrid)

        self.scrollwidget.setWidget(self.widgetforscroll)

        self.direcwidget = QtWidgets.QWidget()
        self.direclayout = QtWidgets.QGridLayout()
        self.direcwidget.setLayout(self.direclayout)
        self.mainlayout.addWidget(self.direcwidget)

        self.opdirbut = QtWidgets.QPushButton() 
        self.opdirbut.setText("그림판")
        self.opdirbut.setFixedSize(90,40)

        self.backpath = QtWidgets.QPushButton() 
        self.backpath.setFixedSize(80,40)
        self.backpath.setText("등록")

        self.addthing = QtWidgets.QPushButton() 
        self.addthing.setFixedSize(80,40)
        self.addthing.setText("추가")

        self.deleteall = QtWidgets.QPushButton() 
        self.deleteall.setFixedSize(90,40)
        self.deleteall.setText("전체삭제")

        self.direclayout.addWidget(self.opdirbut, 0,0, 1, 1)
        self.direclayout.addWidget(self.addthing, 0,2, 1, 1)
        self.direclayout.addWidget(self.backpath, 0,4, 1, 1)
        self.direclayout.addWidget(self.deleteall, 0,6, 1, 1)

class MainWindow3(QtWidgets.QMainWindow, ClassUi):
    def __init__(self):
        super().__init__()
        self.setup(self)

        self.picturerow = 0
        self.picturecolumn = 0
        self.howmany = 0

        self.backpath.clicked.connect(self.close_image)
        self.opdirbut.clicked.connect(self.open_grimpan)
        self.addthing.clicked.connect(self.add_button)
        self.deleteall.clicked.connect(self.delete_img)
        self.opdial()
    
    def add_button(self):
        try:
            jpgfile = QFileDialog.getOpenFileName(self, '사진선택', './')
            split_file = jpgfile[0].split('/')
            file_path = 'C:\\CafeData\\Photo\\'

            try:
                photofile = open('C:\\CafeData\\photo_cnt.txt', 'r', encoding='utf-8')
                photo_cnt = photofile.readline()
                photofile.close()
                photo_cnt = int(photo_cnt.replace('\n', ''))
                photo_cnt = photo_cnt + 1
            except:
                photo_cnt = 1
            file_path = file_path + str(photo_cnt) + '.jpg'
            shutil.copyfile(jpgfile[0],file_path)
            photofile = open('C:\\CafeData\\photo_cnt.txt', 'w', encoding='utf-8')
            photofile.write(str(photo_cnt))
            photofile.close()

            w.showimg()
        except:
            print('no file')
    
    def delete_img(self):
        clear_photo()
        w.showimg()
    
    def open_grimpan(self):
        file_list = os.listdir('C:\\CafeData\\Photo')
        file_list_result2 = [file for file in file_list if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")]
        file_list_result = natsort.natsorted(file_list_result2)
        
        pic_link = 'C:\\CafeData\\Photo\\' + file_list_result[selected_picture]
        checking = subprocess.call([r'C:\Windows\System32\mspaint.exe', pic_link])

        if checking == 0:
            print('success')
            w.showimg()

        #w.opdial()
    
    def close_image(self):
        w.close()
    
    def addpicture(self, pic):
        if self.picturecolumn == 3:
            self.picturecolumn = 0
            self.picturerow += 1
        self.howmany += 1

        newwidget = picwidg(self.howmany, pic)

        def addnewone(lyout,nw,rw,cl):
            lyout.addWidget(nw, rw, cl)

        QtCore.QTimer.singleShot(
            self.howmany*500,
            lambda sc=self.scrollgrid, nr = newwidget, ow = self.picturerow, mn=self.picturecolumn : addnewone(sc,nr,ow,mn)
        )

        self.picturecolumn += 1

    def showimg(self):
        try:
            main_path = os.getcwd()
            main_path = 'C:\\CafeData\\Photo\\'
            file_list = os.listdir('C:\\CafeData\\Photo')
            file_list_result2 = [file for file in file_list if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")]
            file_list_result = natsort.natsorted(file_list_result2)

            for i in range(self.scrollgrid.count()):
                widgetToRemove = self.scrollgrid.itemAt(i).widget()
                widgetToRemove.newpic.setPixmap(QtGui.QPixmap(main_path))
            
            for k in range(len(file_list_result)):
                temp_path = main_path + file_list_result[k]
                print(temp_path)

                widgetforimg = self.scrollgrid.itemAt(k).widget()
                widgetforimg.newpic.setPixmap(QtGui.QPixmap(temp_path).scaled(150, 150, aspectRatioMode= QtCore.Qt.KeepAspectRatio))
        except Exception as e:
            print(e)
            pass
   
    def opdial(self):
        global last_one
        last_one = 0
        try:
            main_path = os.getcwd()
            main_path = 'C:\\CafeData\\Photo\\'
            file_list = os.listdir('C:\\CafeData\\Photo')
            file_list_result2 = [file for file in file_list if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")]
            file_list_result = natsort.natsorted(file_list_result2)

            self.picturecolumn =0
            self.picturerow =0
            self.howmany = 0

            #temp1 = len(file_list_result)
            temp1 = 99
            for i in range(temp1):
                time.sleep(0.02)
                #i = file_list_result[i]
                i = main_path + str(i)
                self.addpicture(i)
        except Exception as e:
            print(e)
            pass

class picwidg(QtWidgets.QWidget):
    whoshover = None
    picwidglist =[]

    def __init__(self, numb, pic):
        super().__init__()
        self.setMouseTracking(True)
        self.numb = numb
        self.pic = pic
        picwidg.picwidglist.append(self)

        SizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        newwidgetlayout = QtWidgets.QVBoxLayout()
        self.setLayout(newwidgetlayout)
        self.setSizePolicy(SizePolicy)
        self.setMinimumSize(QtCore.QSize(150, 200))
        self.setMaximumSize(QtCore.QSize(150, 200))

        if last_one == 0:
            #Pic Label
            self.newpic = QtWidgets.QLabel()
            QtCore.QTimer.singleShot(self.numb*500, self.addingnewpic)
            self.newpic.setScaledContents(True)
            self.newpic.setSizePolicy(SizePolicy)
            self.newpic.setGeometry(0, 0, 150, 150)
            self.newpic.setStyleSheet("border:1px solid gray")
            clickable(self.newpic).connect(lambda :self.print(self.newpic))

            #button
            self.newputton = QtWidgets.QPushButton()
            self.newputton.setGeometry(0,0,10,10)
            self.newputton.setText('삭제')
            self.newputton.clicked.connect(lambda :self.delete_button(self.newputton))

            #Picture text label
            self.newtext = QtWidgets.QLabel()
            font_metrics = QtGui.QFontMetrics(self.font())
            self.newtext.setAlignment(QtCore.Qt.AlignCenter)
            elided_text = font_metrics.elidedText(pic, QtCore.Qt.ElideRight, 100)
            self.newtext.setText(elided_text)
            

            newwidgetlayout.addWidget(self.newpic)
            newwidgetlayout.addWidget(self.newputton)
            newwidgetlayout.addWidget(self.newtext)

        '''if last_one == 1:
            self.newputton = QtWidgets.QPushButton()
            self.newputton.setGeometry(0,0,150,150)
            self.newputton.setText('추가')
            self.newputton.clicked.connect(self.add_button)

            newwidgetlayout.addWidget(self.newputton)'''
    
    def print(self, data):
        global selected_picture
        selected_picture = 0
        cnt = 0
        for i in range(w.scrollgrid.count()):
            try:
                widgetchanged = w.scrollgrid.itemAt(i).widget()
                if widgetchanged.newpic == data:
                    widgetchanged.newpic.setStyleSheet('border: 3px solid black')
                    selected_picture = i
                else:
                    widgetchanged.newpic.setStyleSheet('border: 1px solid black')
            except:
                print('add button')

        print(selected_picture)

    def addingnewpic(self):
        self.newpic.setPixmap(QtGui.QPixmap(self.pic))

    def add_button(self):
        try:
            jpgfile = QFileDialog.getOpenFileName(self, '사진선택', './')
            split_file = jpgfile[0].split('/')
            file_path = 'C:\\CafeData\\Photo\\'
            file_path = file_path + split_file[len(split_file) - 1]
            shutil.copyfile(jpgfile[0],file_path)
            time.sleep(1)
            w.showimg()
            #w.opdial()
        except:
            print('no file')

    def delete_button(self, target):
        temp_a = 0
        for i in range(w.scrollgrid.count()):
            widgetToRemove = w.scrollgrid.itemAt(i).widget()
            if widgetToRemove.newputton == target:
                temp_a = i
                break
        file_list = os.listdir('C:\\CafeData\\Photo')
        file_list_result2 = [file for file in file_list if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")]
        file_list_result = natsort.natsorted(file_list_result2)

        os.remove('C:\\CafeData\\Photo\\' + file_list_result[temp_a])

        w.showimg()
        #w.opdial()

class ClassUi2(object):
    def setup(self, MainW):
        MainW.setObjectName("MainW")
        MainW.setFixedSize(600,500)

        self.mainlayout = QtWidgets.QVBoxLayout()

        self.centralwidget = QtWidgets.QWidget(MainW)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayout(self.mainlayout)
        MainW.setCentralWidget(self.centralwidget)

        self.scrollwidget = QtWidgets.QScrollArea()
        self.mainlayout.addWidget(self.scrollwidget)
        self.scrollwidget.setWidgetResizable(True)
        self.scrollwidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.scrollgrid = QtWidgets.QGridLayout()

        self.widgetforscroll = QtWidgets.QWidget()
        self.widgetforscroll.setLayout(self.scrollgrid)

        self.scrollwidget.setWidget(self.widgetforscroll)

        self.direcwidget = QtWidgets.QWidget()
        self.direclayout = QtWidgets.QGridLayout()
        self.direcwidget.setLayout(self.direclayout)
        self.mainlayout.addWidget(self.direcwidget)

        self.backpath = QtWidgets.QPushButton() 
        self.backpath.setFixedSize(80,40)
        self.backpath.setText("등록")

        self.direclayout.addWidget(self.backpath, 0,4, 1, 1)

class MainWindow4(QtWidgets.QMainWindow, ClassUi2):
    def __init__(self):
        super().__init__()
        self.setup(self)

        self.picturerow = 0
        self.picturecolumn = 0
        self.howmany = 0

        self.backpath.clicked.connect(self.close_image)
        self.opdial()
        
    def close_image(self):
        main_path = os.getcwd()
        main_path = 'C:\\CafeData\\Photo\\'
        file_list = os.listdir('C:\\CafeData\\Photo')
        file_list_result2 = [file for file in file_list if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")]
        file_list_result = natsort.natsorted(file_list_result2)

        which_number = selected_picture

        
        img = Image.open(main_path + file_list_result[which_number])
        img_resize = img.resize((300,300))
        img_resize.save('C:\\CafeData\\Photoex\\k.jpg')

        pixmap = QPixmap('C:\\CafeData\\Photoex\\k.jpg')
        ui.label_3.setPixmap(pixmap)

        w2.close()
    
    def addpicture(self, pic):
        if self.picturecolumn == 3:
            self.picturecolumn = 0
            self.picturerow += 1
        self.howmany += 1

        newwidget = picwidgsec(self.howmany, pic)

        def addnewone(lyout,nw,rw,cl):
            lyout.addWidget(nw, rw, cl)

        QtCore.QTimer.singleShot(
            self.howmany*500,
            lambda sc=self.scrollgrid, nr = newwidget, ow = self.picturerow, mn=self.picturecolumn : addnewone(sc,nr,ow,mn)
        )

        self.picturecolumn += 1

    def opdial(self):
        global last_one
        last_one = 0
        try:
            main_path = os.getcwd()
            main_path = 'C:\\CafeData\\Photo\\'
            file_list = os.listdir('C:\\CafeData\\Photo')
            file_list_result2 = [file for file in file_list if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")]
            file_list_result = natsort.natsorted(file_list_result2)

            self.picturecolumn =0
            self.picturerow =0
            self.howmany = 0

            #temp1 = len(file_list_result)
            temp1 = 99
            for i in range(temp1):
                time.sleep(0.02)
                #i = file_list_result[i]
                i = main_path + str(i)
                self.addpicture(i)
        except Exception as e:
            print(e)
            pass
            
    def showimg(self):
        try:
            main_path = os.getcwd()
            main_path = 'C:\\CafeData\\Photo\\'
            file_list = os.listdir('C:\\CafeData\\Photo')
            file_list_result2 = [file for file in file_list if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")]
            file_list_result = natsort.natsorted(file_list_result2)

            for i in range(self.scrollgrid.count()):
                widgetToRemove = self.scrollgrid.itemAt(i).widget()
                widgetToRemove.newpic.setPixmap(QtGui.QPixmap(main_path))
            
            for k in range(len(file_list_result)):
                temp_path = main_path + file_list_result[k]
                print(temp_path)

                widgetforimg = self.scrollgrid.itemAt(k).widget()
                widgetforimg.newpic.setPixmap(QtGui.QPixmap(temp_path).scaled(150, 150, aspectRatioMode= QtCore.Qt.KeepAspectRatio))
        except Exception as e:
            print(e)
            pass
   
class picwidgsec(QtWidgets.QWidget):
    whoshover = None
    picwidgseclist =[]

    def __init__(self, numb, pic):
        super().__init__()
        self.setMouseTracking(True)
        self.numb = numb
        self.pic = pic
        picwidgsec.picwidgseclist.append(self)

        SizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        newwidgetlayout = QtWidgets.QVBoxLayout()
        self.setLayout(newwidgetlayout)
        self.setSizePolicy(SizePolicy)
        self.setMinimumSize(QtCore.QSize(150, 200))
        self.setMaximumSize(QtCore.QSize(150, 200))

        if last_one == 0:
            #Pic Label
            self.newpic = QtWidgets.QLabel()
            QtCore.QTimer.singleShot(self.numb*500, self.addingnewpic)
            self.newpic.setScaledContents(True)
            self.newpic.setSizePolicy(SizePolicy)
            self.newpic.setGeometry(0, 0, 150, 150)
            self.newpic.setStyleSheet("border:1px solid gray")
            clickable(self.newpic).connect(lambda :self.print(self.newpic))

            #button
            self.newputton = QtWidgets.QPushButton()
            self.newputton.setGeometry(0,0,10,10)
            self.newputton.setText('삭제')
            self.newputton.clicked.connect(lambda :self.delete_button(self.newputton))

            #Picture text label
            self.newtext = QtWidgets.QLabel()
            font_metrics = QtGui.QFontMetrics(self.font())
            self.newtext.setAlignment(QtCore.Qt.AlignCenter)
            elided_text = font_metrics.elidedText(pic, QtCore.Qt.ElideRight, 100)
            self.newtext.setText(elided_text)
            

            newwidgetlayout.addWidget(self.newpic)
            newwidgetlayout.addWidget(self.newputton)
            newwidgetlayout.addWidget(self.newtext)

        if last_one == 1:
            self.newputton = QtWidgets.QPushButton()
            self.newputton.setGeometry(0,0,150,150)
            self.newputton.setText('추가')
            self.newputton.clicked.connect(self.add_button)

            newwidgetlayout.addWidget(self.newputton)
    
    def print(self, data):
        global selected_picture
        selected_picture = 0
        for i in range(w2.scrollgrid.count()):
            try:
                widgetchanged = w2.scrollgrid.itemAt(i).widget()
                if widgetchanged.newpic == data:
                    widgetchanged.newpic.setStyleSheet('border: 3px solid black')
                    selected_picture = i
                else:
                    widgetchanged.newpic.setStyleSheet('border: 1px solid black')
            except:
                print('add button')

        print(selected_picture)

    def addingnewpic(self):
        self.newpic.setPixmap(QtGui.QPixmap(self.pic))

    def add_button(self):
        jpgfile = QFileDialog.getOpenFileName(self, '사진선택', './')
        split_file = jpgfile[0].split('/')
        file_path = 'C:\\CafeData\\Photo\\'
        file_path = file_path + split_file[len(split_file) - 1]
        shutil.copyfile(jpgfile[0],file_path)
        w2.opdial()

    def delete_button(self, target):
        temp_a = 0
        for i in range(w2.scrollgrid.count()):
            widgetToRemove = w2.scrollgrid.itemAt(i).widget()
            if widgetToRemove.newputton == target:
                temp_a = i
                break
        file_list = os.listdir('C:\\CafeData\\Photo')
        file_list_result2 = [file for file in file_list if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")]
        file_list_result = natsort.natsorted(file_list_result2)
        
        os.remove('C:\\CafeData\\Photo\\' + file_list_result[temp_a])
        w2.showimg()

def clickable(widget):
    class Filter(QObject):
    
        clicked = pyqtSignal()	
        
        def eventFilter(self, obj, event):
        
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True
            
            return False
    
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

if __name__ == "__main__":
    import sys
    from contextlib import suppress
    import psutil
    from signal import SIGTERM
    from os import environ

    environ['QT_DEVICE_PIXEL_RATIO'] = "0"
    environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = "1"
    environ['QT_SCREEN_SCALE_FACTORS'] = "1"
    environ['QT_SCALE_FACTOR'] = "1"
    multiprocessing.freeze_support()
    mk_dir()
    clear_photo()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    MainWindow2 = QtWidgets.QMainWindow()
    option_ui = Ui_Option()
    option_ui.setupUi(MainWindow2)

    MainWindow5 = QtWidgets.QMainWindow()
    detail_ui = Ui_Detail()
    detail_ui.setupUi(MainWindow5)

    w = MainWindow3()

    w2 = MainWindow4()

    global driver
    driver = operate_chrome()
    global driver2
    driver2 = operate_chrome2()
    #driver2 = operate_chrome2()
    
    app.exec_()
    try:
        driver.close()
    except:
        pass
    try:
        driver2.close()
    except:
        pass
    
    for process in psutil.process_iter():
        if process.name() == 'chrome.exe' and '--test-type=webdriver' in process.cmdline():
            with suppress(psutil.NoSuchProcess):
                print(process.pid)
                os.kill(process.pid, SIGTERM)
                
    for process in psutil.process_iter():
        if process.name() == 'chromedriver.exe':
            with suppress(psutil.NoSuchProcess):
                print(process.pid)
                os.kill(process.pid, SIGTERM)
    sys.exit()
    
    
