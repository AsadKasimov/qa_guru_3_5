from selene.support.shared import browser
from selene import be, have



def test_serh(open_browser):
    browser.element('[id="firstName"]').type('selene')  # записывает имя
    browser.element('[id="lastName"]').type('selenium')  # записывает фамилию
    browser.element('[id="userEmail"]').type('selene@ya.ru')  # записывает почту
    browser.element('[class="custom-control-label"]').should(have.text('Male')).click() # выбирает пол
    browser.element('[id="userNumber"]').type('123456789') # пишет номер
    browser.element('[id="dateOfBirthInput"]').click().press_enter() # я родился
    browser.element('[id="currentAddress"]').type('street house sity country') # это мой адрес
'''
осталось: 
    Subjects- предмет
    Hobbies- хоби
    Picture- твоя фоточька
    State and City- город
'''
