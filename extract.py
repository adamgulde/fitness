### Ensure Chrome is up to date, as is Selenium Chrome Webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from decoder import decode
import subprocess
import os
from ui import create_ui

import platform
if(platform.platform().startswith('macOS')):
    ### MAC OS CODE
    print('macOS System')
    driver = webdriver.Chrome('/Users/2023148/Downloads/chromedriver')
if(platform.platform().startswith('Windows')):
    ### Windows OS CODE
    print('Windows System')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) ### Should work universally
    # driver = webdriver.Chrome() #executable_path="C:/selenium/chromedriver.exe") UNCOMMENT ON PC

def run():
    initialize()
    image_loop()

def initialize():
    driver.get("https://adamgulde.github.io/")
    start_button = driver.find_element('id', 'start-camera')
    start_button.click()
    ### Wait for user confirmation...
    while(True):
        with open('cmds.txt', 'r') as cmd:
            if cmd.readline() == 'start': break
    os.makedirs('')
    
def verification():
    ### VERIFICATION BLOCK
    ### 
    ###
    ###
    ###
    ###
    pass

def image_loop():
    count=0
    while(True):
        with open('cmds.txt', 'r') as cmd:
            if cmd.readline() != 'stop':
                decode(driver.find_element('id', 'data_text').text, 2, count)
            else: break
        count+=1

if __name__=="__main__":
    run()
