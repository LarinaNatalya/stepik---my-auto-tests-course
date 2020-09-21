
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

main_page_link="http://selenium1py.pythonanywhere.com/ru/"
search_input="input#id_q"
search_submit="input.btn.btn-default"
search_title_locator="div.page-header h1"
search_button="button.btn.btn-default"
link_button_locator="#login_link"
email_reg="[name='registration-email']"
password_reg="[name='registration-password1']"
password_repeat_reg="[name='registration-password2']"
reg_button="[name='registration_submit']"
answer_result="div.alertinner.wicon"
item_book="a[title='Coders at Work']"
select_basket="button:nth-child(3)"
search_item="div.col-sm-4:nth-child(2)>h3"

#1. Поиск товара
def search_item():
    search_text="city"
    try:
        #Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)
        search=browser.find_element_by_css_selector(search_input)

        #Act
        search.send_keys(search_text)
        browser.find_element_by_css_selector(search_submit).click()

        #Assert
        search_title=browser.find_element_by_css_selector(search_title_locator).text
        assert search_text in search_title, \
        "Seach page title '\s' should contain search text '\s'" %(search_title, search_text)

    finally:
        browser.quit()
#search_item()
# не забываем оставить пустую строку в конце файла

#2.Выбор языка
def search_language():
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)
        browser.find_element_by_tag_name("select").click()
        browser.find_element_by_css_selector("[value='ru']").click()

        # Act
        browser.find_element_by_css_selector(search_button).click()
        # Assert
        link_button = browser.find_element_by_css_selector(link_button_locator).text
        assert link_button in " Войти или зарегистрироваться"

    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()
#search_language()

#3.Регистрация
def sign_up():
    mail=''
    email=''
    for x in range(12):
        mail=mail+random.choice(list('12345678'))
        email=mail+'@gmail.com'
        print(email)
    password_text="test200920"


    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)
        browser.find_element_by_css_selector(link_button_locator).click()
        browser.find_element_by_css_selector(email_reg).send_keys(email)
        browser.find_element_by_css_selector(password_reg).send_keys(password_text)
        browser.find_element_by_css_selector(password_repeat_reg).send_keys(password_text)
        # Act
        browser.find_element_by_css_selector(reg_button).click()
        # Assert
        answer=browser.find_element_by_css_selector(answer_result).text
        assert "Спасибо" in answer

    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()
#sign_up()

#4.Добавление товара в корзину
def basket_in():

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/category/books_2/")
        browser.find_element_by_css_selector(item_book).click()
        choice=browser.find_element_by_css_selector(select_basket)
        choice_title=choice.text
        assert "Добавить в корзину" in choice_title

        browser.find_element_by_css_selector(select_basket).click()

        see_basket=browser.find_element_by_link_text("Посмотреть корзину")
        time.sleep(5)
        see_basket.click()
        see_choice = browser.find_element_by_css_selector(search_item)
        assert "Coders at Work" in see_choice.text
    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()
basket_in()
