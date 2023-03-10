import csv

from services import XPATH_MAP
from services.auth_service import AuthenticationService
from selenium.webdriver.common.by import By
from datetime import datetime
from services.utils import switch_frame


class MarketService:

    def __init__(self, driver):
        self.driver = driver
        self.x_path = XPATH_MAP['market_service']

    @staticmethod
    def write_to_csv_file(header_list, table_rows, csv_name=f'data/market_data_{datetime.now().date()}.csv'):
        with open(csv_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([i.strip() for i in header_list])
            # Iterate over the rows and write the data to the CSV file
            for row in table_rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                data = [cell.text for cell in cells]
                if len([i for i in data if i != '']) < 1:
                    continue
                writer.writerow(data)

    def get_market_data(self):
        auth_service = AuthenticationService(self.driver)
        auth_service.login_user()
        driver = switch_frame(self.driver)
        market_data_body = driver.find_element(By.XPATH, f'{self.x_path.get("market_data_body")}')
        table_header = market_data_body.find_element(By.XPATH, f'{self.x_path.get("table_header")}')
        thead_content = table_header.find_elements(By.TAG_NAME, 'th')
        header_list = [i.find_element(By.CSS_SELECTOR, 'div').text for i in thead_content]
        table_rows = market_data_body.find_elements(By.TAG_NAME, "tr")
        # Write the data to a CSV file
        self.write_to_csv_file(header_list, table_rows)


