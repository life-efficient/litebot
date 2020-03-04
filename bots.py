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
    def __init__(self, port_no="9220", headless=False, verbose=False):
        print('initialising bot')
        my_env = os.environ.copy()
        my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
        port_no="9220"
        subprocess.Popen(f'google-chrome --remote-debugging-port={port_no} --user-data-dir=bots'.split(), env=my_env)
        print('process ran')
        options = Options()
        options.add_argument("--no-sandbox")	# without this, the chrome webdriver can't start (SECURITY RISK)
        # print(f"127.0.0.1:{port_no}")
        options.add_experimental_option(f"debuggerAddress", f"127.0.0.1:{port_no}")	# attach to the same port that you're running chrome on
        if headless:
            options.add_argument("--headless")
        #options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome(chrome_options=options)			# create webdriver
        self.verbose = verbose

    def click_btn(self, text):
        if self.verbose: print(f'clicking {text} btn')
        element_types = ['button', 'div', 'input', 'a', 'label']
        for element_type in element_types:
            btns = self.driver.find_elements_by_xpath(f'//{element_type}')
            # for btn in btns:
            #     print(btn.text)
            
            # SEARCH BY TEXT
            try:
                btn = [b for b in btns if b.text.lower() == text.lower()][0]
                btn.click()
                return
            except IndexError:
                pass

        # for element_type in element_types:
            # SEARCH BY VALUE ATTRIBUTE IF NOT YET FOUND
            try:
                btn = self.driver.find_elements_by_xpath(f'//{element_type}[@value="{text}"]')[0]
                btn.click()
                return
            except:
                continue

        raise ValueError(f'button containing "{text}" not found')

    def _search(self, query, _type='search', placeholder=None):
        sleep(1)
        s = self.driver.find_elements_by_xpath(f'//input[@type="{_type}"]')
        print(s)
        if placeholder:
            s = [i for i in s if i.get_attribute('placeholder').lower() == placeholder.lower()][0]
        else:
            s = s[0]
        s.send_keys(query) 

    def toggle_verbose(self):
        self.verbose = not self.verbose