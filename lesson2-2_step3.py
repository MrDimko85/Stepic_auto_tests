from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome(r"C:\Users\николаевда\environments\chromedriver.exe")
    browser.get(link)
    
    element1 = browser.find_element_by_css_selector("#num1")
    x_element1 = int(element1.text)
    element2 = browser.find_element_by_css_selector("#num2")
    x_element2 = int(element2.text)
    element = x_element1 + x_element2
    
    select = Select(browser.find_element_by_tag_name("select"))    
    select.select_by_value(str(element))  
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
     
        
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    