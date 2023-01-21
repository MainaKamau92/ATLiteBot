import logging
import sys

from services.auth_service import AuthenticationService
from services.driver_service import driver_service
from services.market_service import MarketService

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def main():
    driver = driver_service.driver()
    try:
        mkrt_service = MarketService(driver)
        mkrt_service.get_market_data()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
