from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome(r"C:\Users\николаевда\environments\chromedriver.exe")
    browser.get(link)
    
    element = browser.find_element_by_css_selector("#input_value")
    x_element = int(element.text)
    value = calc(x_element)
    
    input1 = browser.find_element_by_tag_name ("#answer")
    input1.send_keys(value)
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    
    option1 = browser.find_element_by_css_selector("#robotsRule")
    option1.click()      
        
    button.click()
        
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

