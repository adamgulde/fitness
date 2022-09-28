### Ensure Chrome is up to date, as is Selenium Chrome Webdriver

from venv import create
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from decoder import decode
import subprocess
from ui import create_ui
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) ### Should work universally

# driver = webdriver.Chrome('/Users/2023148/Downloads/chromedriver') UNCOMMENT ON MAC
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

    #canvas = driver.find_element_by_css_selector("#canvas")

    # get the canvas as a PNG base64 string
    #canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)

    # decode
    #canvas_png = decode(canvas_base64)

if __name__=="__main__":
    run()
