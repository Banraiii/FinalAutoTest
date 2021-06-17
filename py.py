import os 
import logging


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, r'seleniumlogs\test.log')
file_path = str(file_path).replace('\\','//')
logging.basicConfig(filename=file_path,
					format='%(asctime)s: %(levelname)s: %(message)s',
					level=logging.DEBUG
					)
print(str(file_path).replace('\\','//'))
logging.debug("This is debug message")
logging.info("Starting webdriver")
logging.warning("This is warning message")