from selenium import webdriver
import json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException
from time import sleep, time
import random
import re

import subprocess, os
my_env = os.environ.copy()
my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
port_no="9220"
subprocess.Popen(f'google-chrome --remote-debugging-port={port_no} --user-data-dir="~/bots"'.split(), env=my_env)

print('process ran')

max_time = 10

class Bot():
    def __init__(self):
        print('initialising bot')
        options = Options()
        options.add_argument("--no-sandbox")	# without this, the chrome webdriver can't start (SECURITY RISK)
        options.add_experimental_option(f"debuggerAddress", "127.0.0.1:{port_no}")	# attach to the same port that you're running chrome on
        # options.add_argument("--headless")
        #options.add_argument("--window-size=1920x1080")
        self.browser = webdriver.Chrome(chrome_options=options)			# create webdriver
        self.browser.get('https://mywebsite.com/')						# go to webpage
