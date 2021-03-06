import os
from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(r"C:\Users\николаевда\environments\chromedriver.exe")
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...
    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("qwe@gmail.com")
    input4 = browser.find_element_by_css_selector("#file")
    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    input4.send_keys(file_path)    
    
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()