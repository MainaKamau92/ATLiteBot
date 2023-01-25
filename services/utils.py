from selenium.webdriver.common.by import By


def switch_frame(driver):
    # get the iframe
    iframe = driver.find_element(By.XPATH, '//*[@id="iMarketDetailsFrame"]')
    # get market data from iframe
    driver.switch_to.frame(iframe)
    return driver
