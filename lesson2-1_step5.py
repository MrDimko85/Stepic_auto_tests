from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome(r"C:\Users\николаевда\environments\chromedriver.exe")
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = str(calc(x))
    
    input1 = browser.find_element_by_tag_name ("input")
    input1.send_keys(y)
    
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    
    option1 = browser.find_element_by_css_selector("#robotsRule")
    option1.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()