# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:16:46 2020

@author: Ankur
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("E:\Anaconda\chromedriver.exe")

class BotMe:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
    def login(self):
        driver.get("https://twitter.com/")
        email = driver.find_element_by_name("session[username_or_email]")
        email.send_keys(self.email)
        password = driver.find_element_by_name("session[password]")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN) 
        
ankur = BotMe("_ankurgajurel", "kumarimanu")
ankur.login()
        
        

