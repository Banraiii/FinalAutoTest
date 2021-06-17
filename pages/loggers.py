import os
import logging

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, r'seleniumlogs\test.log')
file_path = str(file_path).replace('\\','//')
file_path = file_path[0:-29] + file_path[-22:len(file_path)]
logging.basicConfig(filename=file_path,
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.INFO
                    )
