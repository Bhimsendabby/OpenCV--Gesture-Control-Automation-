from selenium import webdriver
import threading
class whats(threading.Thread):
    def run(self):
        driver = webdriver.Chrome(executable_path="C:\Anaconda3\envs\hello\chromedriver_win32\chromedriver.exe") #chorme driver path
        driver.get('https://web.whatsapp.com/')                                           #link which you want to open
        input('Enter anything after scanning QR code')
        name = "Arunav Goel"    #name of receiver
        msg = "hey"             #message which you want to send
        count = 3
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))         #find the path of textbox
        user.click()

        msg_box = driver.find_element_by_class_name('_2S1VP')                            #find the path of button

        for i in range(count):
            msg_box.send_keys(msg)
            button = driver.find_element_by_class_name('_35EW6')
            button.click()