import os 
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .pages.loggers import logging

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru or en ...")

@pytest.fixture(scope='function')
def driver(request):
    logging.info("Starting webdriver")
    user_language = request.config.getoption('language')
    print("\nстарт браузера для тестирования..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    driver = webdriver.Chrome(options=options)
    yield driver
    print('\nбраузер для тестирования закрывается.')
    driver.quit()
