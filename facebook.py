from selenium import webdriver
import threading
class facebook(threading.Thread):
    def run(self):
        driver = webdriver.Chrome(executable_path="C:\Anaconda3\envs\hello\chromedriver_win32\chromedriver.exe")    #chorme driver path
        driver.get('https://www.facebook.com/')                      #link to open facebook login page

        input('Enter anything after scanning QR code')


        user_id="bhimsen.dabbi@facebook.com"              #user details
        password="**************"
        id_user = driver.find_element_by_id("email")                 #path of inputbox of email
        pass_user = driver.find_element_by_id("pass")                #path of input box of password
        id_user.send_keys(user_id)                               #send data to logiin page
        pass_user.send_keys(password)

        button = driver.find_element_by_id('loginbutton')            #login button to click the data
        button.click()