import time
import csv


def main():
    pass

if __name__ == "__main__":


    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    driver.get("http://registeronline.nhif.or.ke/member/?home=1#")
    time.sleep(5)
    for page in range(500, 800):
        print(f"Handling data for the page {page}")
        driver.execute_script(f'return portal.list_group_members_paginate({page})')
        time.sleep(10)
        tr_elements = driver.find_elements(By.TAG_NAME, "tr")
        # open a new CSV file for writing
        with open("data.csv", "a", newline="") as csvfile:
            # create a CSV writer
            writer = csv.writer(csvfile)

            # loop through the tr elements
            for idx, tr in enumerate(tr_elements):
                if idx == 0:
                    continue
                # write the text of each tr element to the CSV file
                writer.writerow([tr.text])

