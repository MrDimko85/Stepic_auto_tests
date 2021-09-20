from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\николаевда\environments\chromedriver.exe")
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
