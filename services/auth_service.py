import os
from selenium.webdriver.common.by import By


class AuthenticationService:

    def __init__(self, driver):
        self.driver = driver
        self._login_url = "https://onlinetrading.ncbagroup.com/tradeweb/login.aspx"
        self._username = os.getenv("AUTH_USERNAME")
        self._password = os.getenv("AUTH_PASSWORD")

    def login_user(self):
        self.driver.get(self._login_url)
        # implicit delay
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '//*[@id="txtLogin"]').send_keys(self._username)
        self.driver.find_element(By.XPATH, '//*[@id="txtPassword"]').send_keys(self._password)
        self.driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
        # wait for page to load
        self.driver.implicitly_wait(10)
