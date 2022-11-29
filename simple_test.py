from selene.api import browser
from selene import be, have

def test_body(open_browser):
    browser.element('[name="q"]').should(be.blank).type('Selene web-ui').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))
