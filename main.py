import logging
import sys

from services.auth_service import AuthenticationService
from services.driver_service import driver_service
from services.finance_service import FinanceService
from services.market_service import MarketService
from services.order_service import OrderService
from services.portfolio_service import PortfolioService

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def main():
    driver = driver_service.driver()
    try:
        portfolio_service = FinanceService(driver)
        portfolio_service.execute_funds_transfer(1.00, remarks="Testing")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
