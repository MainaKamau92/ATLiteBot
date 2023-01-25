import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from services import XPATH_MAP
from services.auth_service import AuthenticationService
from services.utils import switch_frame


class OrderService:

    def __init__(self, driver):
        self.driver = driver
        self.x_paths = XPATH_MAP.get("order_service")

    def make_order(self, security, quantity, price, buy=True):
        auth_service = AuthenticationService(self.driver)
        auth_service.login_user()
        driver = switch_frame(self.driver)
        market_data_body = driver.find_element(By.XPATH, f'{self.x_paths.get("market_data_body")}')
        table_rows = market_data_body.find_elements(By.TAG_NAME, "tr")
        for table in table_rows:
            if security in table.text:
                table.find_element(By.CSS_SELECTOR, 'div').click()
                driver.switch_to.default_content()
                order_button = driver.find_element(By.XPATH, f'{self.x_paths.get("order_sell_btn")}') if not buy else driver.find_element(By.XPATH, f'{self.x_paths.get("order_buy_btn")}')
                order_button.click()
                select_element = Select(driver.find_element(By.XPATH, f'{self.x_paths.get("trade_type_select")}'))
                select_element.select_by_visible_text("ET ODD")
                # add the quantity of shares to be purchased
                driver.find_element(By.XPATH, f'{self.x_paths.get("trade_order_quantity")}').send_keys(quantity)
                # add price of sell or buy order
                driver.find_element(By.XPATH, f'{self.x_paths.get("trade_order_price")}').send_keys(price)
                # date validity of order
                driver.find_element(By.XPATH, f'{self.x_paths.get("trade_order_date")}').send_keys("2021-12-31")
                time.sleep(5)
                # delivery or intraday
                body = driver.find_element(By.XPATH, '//*[@id="lblType"]/b')
                body.click()
                # driver.execute_script("document.elementFromPoint(1132, 337).click();")

                select_element = Select(driver.find_element(By.XPATH, f'{self.x_paths.get("trading_mode_select")}'))
                select_element.select_by_visible_text("Intraday")

                # buy or sell button click
                # implicit wait for the pop up after clicking the buy or sell button
                driver.find_element(By.XPATH, f'{self.x_paths.get("order_validate_transaction")}').click()
                time.sleep(5)
                # confirm purchase
                driver.find_element(By.XPATH, f'{self.x_paths.get("order_confirm_transaction")}').click()
                time.sleep(5)

