from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "E:\Anaconda\chromedriver.exe"
driver = webdriver.Chrome(path)

class BotMe:
    def __init__(self, name):
        self.name = name
    
    def webMe(self):
        driver.get("https://www.selenium.dev/")
        search = driver.find_element_by_name("search")
        time.sleep(1)
        search.send_keys("selenium")
        time.sleep(1)
        search.send_keys(Keys.RETURN)
        
SelenMe = BotMe("Ankur")
SelenMe.webMe()
