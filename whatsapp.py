from selenium import webdriver
import threading
class whats(threading.Thread):
    def run(self):
        driver = webdriver.Chrome(executable_path="C:\Anaconda3\envs\hello\chromedriver_win32\chromedriver.exe")
        driver.get('https://web.whatsapp.com/')
        input('Enter anything after scanning QR code')
        name = "Arunav Goel"
        msg = "hey"
        count = 3
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()

        msg_box = driver.find_element_by_class_name('_2S1VP')

        for i in range(count):
            msg_box.send_keys(msg)
            button = driver.find_element_by_class_name('_35EW6')
            button.click()