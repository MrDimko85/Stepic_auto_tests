import unittest
from selenium import webdriver

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(r"C:\Users\николаевда\environments\chromedriver.exe")
        browser.get(link)
        
        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input3.send_keys("qwe@gmail.com")
        
        button = browser.find_element_by_css_selector("button.btn.btn-default")
        button.click()
        
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        
        welcome_text = welcome_text_elt.text
        
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome(r"C:\Users\николаевда\environments\chromedriver.exe")
        browser.get(link)
        
        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input3.send_keys("qwe@gmail.com")
        
        button = browser.find_element_by_css_selector("button.btn.btn-default")
        button.click()
        
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        
        welcome_text = welcome_text_elt.text    

    
if __name__ == "__main__":
    unittest.main()
