import logging
import sys

from services.driver_service import driver_service
from services.portfolio_service import PortfolioService

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def main():
    driver = driver_service.driver()
    try:
        portfolio_service = PortfolioService(driver)
        portfolio_service.fetch_portfolio_data()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
