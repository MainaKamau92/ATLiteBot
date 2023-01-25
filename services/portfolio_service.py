from selenium.webdriver.common.by import By
import time
from datetime import datetime
import csv
from services.auth_service import AuthenticationService
from services.market_service import MarketService


class PortfolioService:

    def __init__(self, driver):
        self.driver = driver

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
        self.driver.find_element(By.XPATH, '//*[@id="btnLinkPortfolioValuation"]').click()
        # wait for page to load
        time.sleep(5)
        # click button for details
        self.driver.find_element(By.XPATH, '//*[@id="immpvssd"]').click()
        # fetch portfolio summary
        portfolio_value_free = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/center/div[2]/table/tbody/tr[3]/td[2]')
        unsettled_purchase_value = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/center/div[2]/table/tbody/tr[4]/td[2]')
        portfolio_value_frozen = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/center/div[2]/table/tbody/tr[5]/td[2]/i')
        values = [["Portfolio Value (Free)", portfolio_value_free.text],
                  ["Unsettled Purchase Value", unsettled_purchase_value.text],
                  ["Portfolio Value (Frozen)", portfolio_value_frozen.text]]
        self.write_summary_to_csv(values)
        # fetch owned securities detailed data
        market_data_body = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/center/center/div/table/tbody')
        table_header = market_data_body.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/center/center/div/table/thead')
        thead_content = table_header.find_elements(By.TAG_NAME, 'th')
        header_list = [i.text for i in thead_content]
        table_rows = market_data_body.find_elements(By.TAG_NAME, "tr")
        MarketService(self.driver).write_to_csv_file(header_list, table_rows,
                                                     csv_name=f'data/portfolio_{datetime.now().date()}.csv')