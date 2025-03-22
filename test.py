from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service

from tempfile import mkdtemp

options = Options()
options.binary_location = '/var/task/chrome-headless-shell-linux64/chrome-headless-shell'
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-tools")
options.add_argument("--no-zygote")
options.add_argument("--single-process")
# options.add_argument(f"--user-data-dir={mkdtemp()}")
# options.add_argument(f"--data-path={mkdtemp()}")
# options.add_argument(f"--disk-cache-dir={mkdtemp()}")
options.add_argument("--remote-debugging-pipe")
options.add_argument("--verbose")
options.add_argument("--log-path=/tmp")

service = Service(executable_path='/var/task/chromedriver-linux64/chromedriver')

print('creating driver...')

driver = webdriver.Chrome(options, service)

print('created driver ✅')

print('getting google.com...')

driver.get('https://www.google.com')

print('got google.com ✅')

title = driver.title

print(title)

