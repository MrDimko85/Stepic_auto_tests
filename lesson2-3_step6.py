from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome(r"C:\Users\николаевда\environments\chromedriver.exe")
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

element = browser.find_element_by_css_selector("#input_value")
x_element = int(element.text)
value = calc(x_element)

input1 = browser.find_element_by_tag_name ("#answer")
input1.send_keys(value)

button = browser.find_element_by_css_selector("button.btn")
button.click()