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


max_time = 10

class Bot():
    def __init__(self, port_no="9220"):
        print('initialising bot')
        my_env = os.environ.copy()
        my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
        port_no="9220"
        subprocess.Popen(f'google-chrome --remote-debugging-port={port_no} --user-data-dir="bots"'.split(), env=my_env)
        print('process ran')
        options = Options()
        options.add_argument("--no-sandbox")	# without this, the chrome webdriver can't start (SECURITY RISK)
        # print(f"127.0.0.1:{port_no}")
        options.add_experimental_option(f"debuggerAddress", f"127.0.0.1:{port_no}")	# attach to the same port that you're running chrome on
        # options.add_argument("--headless")
        #options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome(chrome_options=options)			# create webdriver

    def click_btn(self, text):
        btns = self.driver.find_elements_by_xpath('//button')
        btn = [b for b in btns if b.text.lower() == text.lower()][0]
        btn.click()

    def search(self, query, _type='search', placeholder=None):
        sleep(1)
        s = self.driver.find_elements_by_xpath(f'//input[@type="{_type}"]')
        print(s)
        if placeholder:
            s = [i for i in s if i.get_attribute('placeholder') == placeholder][0]
        else:
            s = s[0]
        s.send_keys(query) 