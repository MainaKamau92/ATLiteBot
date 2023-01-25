import time
import csv
from selenium.webdriver.common.by import By
from datetime import datetime

from selenium.webdriver.support.select import Select

from services.auth_service import AuthenticationService


class FinanceService:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def write_funds_to_csv(values):
        with open(f'data/available_funds_summary_{datetime.now().date()}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Amount"])
            # Iterate over the rows and write the data to the CSV file
            for row in values:
                writer.writerow(row)

    def fetch_available_funds(self):
        auth_service = AuthenticationService(self.driver)
        auth_service.login_user()
        self.driver.find_element(By.XPATH, '//*[@id="btnLinkAvailableFund"]').click()
        # wait for page to load
        time.sleep(5)
        market_data_body = self.driver.find_element(By.XPATH, '//*[@id="tbl_ATLiteAvailableFundsForNormal"]/tbody')
        table_rows = market_data_body.find_elements(By.TAG_NAME, "tr")
        final_values = []
        for row in table_rows[3:]:
            row_values = row.find_elements(By.TAG_NAME, "td")
            data_row = [row_values[0].text, row_values[1].text]
            if len([i for i in data_row if i != ""]) < 1:
                continue
            else:
                final_values.append(data_row)
        self.write_funds_to_csv(final_values)

    def execute_funds_transfer(self, amount, remarks=None):
        auth_service = AuthenticationService(self.driver)
        auth_service.login_user()
        self.driver.find_element(By.XPATH, '//*[@id="btnLinkFundTransfer"]').click()
        # wait for page to load
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="txtPayReqAmount"]').send_keys(amount)
        # select mode of payment
        select_element = Select(self.driver.find_element(By.XPATH, '//*[@id="lstPayType"]'))
        select_element.select_by_visible_text("MPESA")  # only supports MPESA for now
        if remarks:
            self.driver.find_element(By.XPATH, '//*[@id="txtPayReqRemarks"]').send_keys(remarks)
        self.driver.find_element(By.XPATH, '//*[@id="btnSubmit"]').click()
        time.sleep(5)
        # confirm withdrawal
        self.driver.find_element(By.XPATH, '//*[@id="btn_WithdrawSubmit"]').click()
        time.sleep(5)