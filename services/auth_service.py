import os
from selenium.webdriver.common.by import By

from services import XPATH_MAP


class AuthenticationService:

    def __init__(self, driver):
        self.driver = driver
        self._login_url = "https://onlinetrading.ncbagroup.com/tradeweb/login.aspx"
        self._username = os.getenv("AUTH_USERNAME")
        self._password = os.getenv("AUTH_PASSWORD")
        self.x_paths = XPATH_MAP['auth_service']

    def login_user(self):
        self.driver.get(self._login_url)
        # implicit delay
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, f'{self.x_paths.get("username")}').send_keys(self._username)
        self.driver.find_element(By.XPATH, f'{self.x_paths.get("password")}').send_keys(self._password)
        self.driver.find_element(By.XPATH, f'{self.x_paths.get("submit")}').click()
        # wait for page to load
        self.driver.implicitly_wait(10)
