import csv
from services.auth_service import AuthenticationService
from selenium.webdriver.common.by import By

from services.utils import switch_frame


class MarketService:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def write_to_csv_file(header_list, table_rows):
        with open('table.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([i.strip() for i in header_list])
            # Iterate over the rows and write the data to the CSV file
            for row in table_rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                data = [cell.text for cell in cells]
                writer.writerow(data)

    def get_market_data(self):
        auth_service = AuthenticationService(self.driver)
        auth_service.login_user()
        driver = switch_frame(self.driver)
        market_data_body = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div[65]/div[3]/div[2]/table/tbody')
        table_header = market_data_body.find_element(By.XPATH, '/html/body/form/div[3]/div/div[65]/div[3]/div[1]/div/table/thead')
        thead_content = table_header.find_elements(By.TAG_NAME, 'th')
        header_list = [i.find_element(By.CSS_SELECTOR, 'div').text for i in thead_content]
        table_rows = market_data_body.find_elements(By.TAG_NAME, "tr")
        # Write the data to a CSV file
        self.write_to_csv_file(header_list, table_rows)


