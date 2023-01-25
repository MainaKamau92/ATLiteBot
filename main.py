import logging
import sys

from services.auth_service import AuthenticationService
from services.driver_service import driver_service
from services.market_service import MarketService
from services.order_service import OrderService

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def main():
    driver = driver_service.driver()
    try:
        order_service = OrderService(driver)
        order_service.make_order("EVRD", 10, 0.63)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
