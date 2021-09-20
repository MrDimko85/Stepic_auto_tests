from selenium import webdriver

link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome(r"C:\Users\николаевда\environments\chromedriver.exe")
browser.get(link)

browser.find_element_by_id("button")