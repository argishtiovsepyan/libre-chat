from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import base64

class LibreScraper:
    def __init__(self, base_url, target_folder="/Users/argishtiovsepyan/Desktop/WORK/libreAI/trainingData"):
        self.base_url = base_url
        self.target_folder = target_folder
        self.chrome_options = Options()

        if not os.path.exists(self.target_folder):
            os.makedirs(self.target_folder)

    def start_driver(self):
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.implicitly_wait(10)

    def navigate_to_page(self):
        self.driver.get(self.base_url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    def extract_links(self):
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        urls_to_scrape = set()

        for link in links:
            try:
                href = link.get_attribute('href')
                if href and href.startswith(self.base_url):
                    urls_to_scrape.add(href)
            except:
                print("Error occurred while processing a link.")
                pass
        
        print(f"\nTotal unique links to scrape: {len(urls_to_scrape)}\n")

        return urls_to_scrape

    def extract_and_save_content(self, url):
        
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(url)

        # Extract title for the PDF name
        relative_path = url.replace(self.base_url, '').strip('/')
        pdf_name = relative_path.replace('/', '_') + ".pdf"
        pdf_path = os.path.join(self.target_folder, pdf_name)

        # Use Chrome's print to PDF feature
        print_options = {
            'printBackground': True,
            'pageSize': 'A4'
        }
        response = self.driver.execute_cdp_cmd('Page.printToPDF', print_options)
        with open(pdf_path, 'wb') as file:
            file.write(base64.b64decode(response['data']))
        print(f"Saved PDF as: {pdf_name}")
        
        # Close the tab and switch back to the main tab
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def close_browser(self):
        self.driver.quit()

    def scrape_and_save_all(self):
        self.start_driver()
        self.navigate_to_page()
        urls_to_scrape = self.extract_links()

        for url in urls_to_scrape:
            self.extract_and_save_content(url)

        self.close_browser()

if __name__ == "__main__":
    websites = [
        "https://blog.libre.org/",
        "https://docs.libredex.org/",
        "https://docs.libre.org/libre-docs/"
    ]

    for website in websites:
        scraper = LibreScraper(website)
        scraper.scrape_and_save_all()
