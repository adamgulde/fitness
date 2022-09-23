from selenium import webdriver
driver = webdriver.Chrome('/Users/2023148/Downloads/chromedriver')
from decoder import decode
driver.get("http://127.0.0.1:8080/index.html") ### URL 

### VERIFICATION BLOCK
### 
###
###
###
###

#canvas = driver.find_element_by_css_selector("#canvas")

# get the canvas as a PNG base64 string
#canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)

# decode
#canvas_png = decode(canvas_base64)
