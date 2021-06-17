import os 
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru or en ...")

@pytest.fixture(scope='function')
def driver(request):
    user_language = request.config.getoption('language')
    print("\nстарт браузера для тестирования..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    driver = webdriver.Chrome(options=options)
    yield driver
    print('\nбраузер для тестирования закрывается.')
    driver.quit()

@pytest.fixture(scope='session')
def logg():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, r'seleniumlogs\test.log')
    file_path = str(file_path).replace('\\','//')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',file_path, 'test')
    logging.basicConfig(filename=file_path,
                        format='%(asctime)s: %(levelname)s: %(message)s',
                        level=logging.DEBUG
                        )
    logging.info("Starting webdriver")
    return logging