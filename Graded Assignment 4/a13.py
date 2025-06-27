# /// script
# dependencies = ["playwright"]
# ///

from playwright.sync_api import sync_playwright
import pandas as pd

def scrape_tables():
    with sync_playwright() as p:
        # Channel can be "chrome", "msedge", "chrome-beta", "msedge-beta" or "msedge-dev".
        browser = p.chromium.launch(headless=True, channel="chrome")
        page = browser.new_page()
        sum = 0
        for i in range(63, 73):
            page.goto(f"https://sanand0.github.io/tdsdata/js_table/?seed={i}")
            table = page.query_selector_all("table")
            #convert the table data to a DataFrame
            data = []
            for row in table[0].query_selector_all("tr"):
                cols = row.query_selector_all("td")
                if cols:
                    data.append([int(col.inner_text()) for col in cols])
            df = pd.DataFrame(data[0:])
            sum = sum + df.sum().sum()
        print(f"Sum of all numbers in the tables: {sum}")
        browser.close()
if __name__ == "__main__":
    scrape_tables()

# Output: 2494397
