from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class DriverService:

    @staticmethod
    def driver_options():
        options = Options()
        options.headless = True
        return options

    def driver(self):
        return webdriver.Chrome(ChromeDriverManager().install(),
                                options=self.driver_options())


driver_service = DriverService()