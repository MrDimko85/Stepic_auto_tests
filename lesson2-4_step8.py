from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome(r"C:\Users\mrdim\environments\chromedriver.exe")

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    
button = browser.find_element_by_css_selector("button.btn")
button.click()

element = browser.find_element_by_css_selector("#input_value")
x_element = int(element.text)
value = calc(x_element)

input1 = browser.find_element_by_tag_name ("#answer")
input1.send_keys(value)

button = browser.find_element_by_css_selector("#solve")
button.click()