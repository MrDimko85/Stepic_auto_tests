from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(r"C:\Users\николаевда\environments\chromedriver.exe")
    browser.get(link)

    input_first_name = browser.find_element_by_css_selector("input.form-control.first[placeholder='Input your first name']")
    input_first_name.send_keys('first name')
    input_middle_name = browser.find_element_by_css_selector("input.form-control.second[placeholder='Input your last name']")
    input_middle_name.send_keys('last name')
    input_email = browser.find_element_by_css_selector("input.form-control.third[placeholder='Input your email']")
    input_email.send_keys('email')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
