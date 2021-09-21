import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(r"C:\Users\mrdim\environments\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()
    
class TestMainPage1():
    text = ''

    @pytest.mark.parametrize('links', ['https://stepik.org/lesson/236895/step/1',
            'https://stepik.org/lesson/236897/step/1',
            'https://stepik.org/lesson/236898/step/1',
            'https://stepik.org/lesson/236899/step/1',
            'https://stepik.org/lesson/236903/step/1',
            'https://stepik.org/lesson/236904/step/1',
            'https://stepik.org/lesson/236905/step/1'])
    def test_guest_should_see_login_link(self, browser, links):
        browser.get(links)        
        browser.implicitly_wait(10)
        answer = str(math.log(int(time.time())))
        browser.find_element_by_css_selector("[placeholder='Напишите ваш ответ здесь...']").send_keys(answer)
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        button.click()
        element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "attempt-message_wrong")))
        text = element.text
        

"""from selenium import webdriver
import pytest
import time
import math

final = ''


@pytest.fixture(scope="session")
def browser():
    br = webdriver.Chrome()
    yield br
    br.quit()
    print(final)  # напечатать ответ про Сов в конце всей сессии


@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_find_hidden_text(browser, lesson):
    global final
    link = f'https://stepik.org/lesson/{lesson}/step/1'
    browser.implicitly_wait(10)
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector('textarea').send_keys(str(answer))
    browser.find_element_by_css_selector('.submit-submission ').click()
    check_text = browser.find_element_by_css_selector('.smart-hints__hint').text
    try:
        assert 'Correct!' == check_text
    except AssertionError:
        final += check_text  # собираем ответ про Сов с каждой ошибкой"""
        
"""import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


links = [  # Список ссылок на тестируемые страницы
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.fixture(scope='function')
def answer():
    """Фистура применяется к функции теста.
    :return: Возвращает результат формулы math.log(int(time.time()))
    :rtype: str
    """
    return str(math.log(int(time.time())))


class TestStepik:
    @classmethod
    def setup_class(cls):
        """Метод класса инициализирует вебдрайвер.
        Устанавливает неявное ожидание
        """
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(5)
    
    @classmethod
    def teardown_class(cls):
        """Метод класса закрывает браузер
        """
        cls.browser.quit()
    
    @pytest.mark.parametrize('link', links)
    def test_stepik(self, link, answer):
        # Открывает страницу
        self.browser.get(link)
        # Ожидает появления элемента с тегом "textarea"
        textarea = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
        )
        # Передаем ответ из фикстуры answer в поле ввода
        textarea.send_keys(answer)
        # Нажимаем кнопку
        self.browser.find_element_by_css_selector('button.submit-submission ').click()
        # Получаем текст элемента, подтверждающего правильность ответа
        feedback = self.browser.find_element_by_css_selector('pre.smart-hints__hint').text
        # Проверяем ответ
        assert feedback == 'Correct!'"""
        