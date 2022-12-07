import os.path
import time

from selene.support.shared import browser
from selene import have


def test_serh(open_browser):
    browser.element('[id="firstName"]').type('selene')  # записывает имя
    browser.element('[id="lastName"]').type('selenium')  # записывает фамилию
    browser.element('[id="userEmail"]').type('selene@ya.ru')  # записывает почту
    browser.element('[class="custom-control-label"]').should(have.text('Male')).click()  # выбирает пол
    browser.element('[id="userNumber"]').type('1234567891')  # пишет номер
    browser.element('[for="hobbies-checkbox-1"]').click()  # хобби

    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select>[value="2006"]').click()
    browser.element('.react-datepicker__month-select>[value="6"]').click()
    browser.element('.react-datepicker__day--023').click()
    browser.element('[id="subjectsInput"]').type('Maths').press_enter()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir,
                                     'C:\\Users\\kasim\\PycharmProjects\\qa_guru_3_5\\files\\photo.jpg')))
    browser.element('[id="currentAddress"]').type('street house sity country')  # это мой адрес
    browser.element('[id="react-select-3-input"]').type('Haryana').press_enter()
    browser.element('[id="react-select-4-input"]').type('Karnal').press_enter()
    browser.element('[id="submit"]').click()
    time.sleep(3)
    browser.all('[class="table table-dark table-striped table-bordered table-hover"]').should(have.texts(
        'selene',
        'selenium',
        'selene@ya.ru',
        'Male',
        '1234567891',
        '23 March 2006',
        'Maths',
        'photo.jpg',
        'street house sity country',
        'Haryana',
        'Karnal',
    ))

