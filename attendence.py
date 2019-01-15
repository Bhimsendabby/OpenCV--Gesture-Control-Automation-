from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class attendance:
    @classmethod
    def login(cls):
        driver = webdriver.Chrome(executable_path="C:\Anaconda3\envs\hello\chromedriver_win32\chromedriver.exe")
        driver.get('https://academics.gndec.ac.in/')

        student_id = "1615316"
        student_pw ="Bhimsen123"

        std_id = driver.find_element_by_id("username")
        std_pw = driver.find_element_by_id("password")

        std_id.send_keys(student_id)
        std_pw.send_keys(student_pw)


        btn = driver.find_element_by_name("submit")
        btn.click()
        view_atd = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/form/button")
        # wait = WebDriverWait(driver,20)
        # wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'student_view_attendance')][@value='in']"))).click()
        view_atd.click()

