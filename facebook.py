from selenium import webdriver
import threading
class facebook(threading.Thread):
    def run(self):
        driver = webdriver.Chrome(executable_path="C:\Anaconda3\envs\hello\chromedriver_win32\chromedriver.exe")
        driver.get('https://www.facebook.com/')

        input('Enter anything after scanning QR code')


        user="bhimsen.dabbi@facebook.com"
        password="bhimsendabbi"
        id_user = driver.find_element_by_id("email")
        pass_user = driver.find_element_by_id("pass")
        id_user.send_keys(user)
        pass_user.send_keys(password)

        button = driver.find_element_by_id('loginbutton')
        button.click()