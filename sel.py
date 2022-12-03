from selene.support.shared import browser
from selene import be, have
from datetime import datetime
import random

def test_serh(open_browser):
    browser.element('[id="firstName"]').type('selene')
    browser.element('[id="lastName"]').type('selenium')
    browser.element('[id="userEmail"]').type('selene@ya.ru')
#    browser.element('[class="custom-control-label"]').should(have.text('Male')).click()
#    browser.element('[id="userNumber"]').type(random.getrandbits(11))
#    browser.element('[id="dateOfBirthInput"]').type(datetime.now().strftime('%x'))

    browser.all('#output p').should(have.texts(
        'selene'
        'selenium'
        'selene@ya.ru'))



