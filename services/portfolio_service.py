from selenium.webdriver.common.by import By
import time
from datetime import datetime
import csv

from services import XPATH_MAP
from services.auth_service import AuthenticationService
from services.market_service import MarketService


class PortfolioService:

    def __init__(self, driver):
        self.driver = driver
        self.x_path = XPATH_MAP.get('portfolio_service')

    @staticmethod
    def write_summary_to_csv(values):
        with open(f'data/portfolio_summary_{datetime.now().date()}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Value"])
            # Iterate over the rows and write the data to the CSV file
            for row in values:
                writer.writerow(row)

    def fetch_portfolio_data(self):
        auth_service = AuthenticationService(self.driver)
        auth_service.login_user()
        self.driver.find_element(By.XPATH, f'{self.x_path.get("portfolio_valuation_btn")}').click()
        # wait for page to load
        time.sleep(5)
        # click button for details
        self.driver.find_element(By.XPATH, f'{self.x_path.get("portfolio_details_btn")}').click()
        # fetch portfolio summary
        portfolio_value_free = self.driver.find_element(By.XPATH, f'{self.x_path.get("portfolio_value_free_btn")}')
        unsettled_purchase_value = self.driver.find_element(By.XPATH, f'{self.x_path.get("unsettled_purchase_value_btn")}')
        portfolio_value_frozen = self.driver.find_element(By.XPATH, f'{self.x_path.get("portfolio_value_frozen_btn")}')
        values = [["Portfolio Value (Free)", portfolio_value_free.text],
                  ["Unsettled Purchase Value", unsettled_purchase_value.text],
                  ["Portfolio Value (Frozen)", portfolio_value_frozen.text]]
        self.write_summary_to_csv(values)
        # fetch owned securities detailed data
        market_data_body = self.driver.find_element(By.XPATH, f'{self.x_path.get("market_data_body")}')
        table_header = market_data_body.find_element(By.XPATH, f'{self.x_path.get("table_header")}')
        thead_content = table_header.find_elements(By.TAG_NAME, 'th')
        header_list = [i.text for i in thead_content]
        table_rows = market_data_body.find_elements(By.TAG_NAME, "tr")
        MarketService(self.driver).write_to_csv_file(header_list, table_rows,
                                                     csv_name=f'data/portfolio_{datetime.now().date()}.csv')