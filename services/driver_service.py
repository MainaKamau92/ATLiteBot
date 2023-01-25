from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class DriverService:

    @staticmethod
    def driver_options():
        options = Options()
        options.headless = False
        return options

    def driver(self):
        return webdriver.Firefox(options=self.driver_options())


driver_service = DriverService()
