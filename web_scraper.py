from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class WebScraper:

    def __init__(
        self, game_url, headless=False, chromedriver_path="/usr/local/bin/chromedriver"
    ):
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        if headless:
            options.add_argument("--headless")
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )

        self.open_url(game_url)

    def open_url(self, url):
        url = "https://www.linkedin.com/games/tango/"
        self.driver.get(url)

    @staticmethod
    def print_error_output_screenshot(driver, e, error_message, file_name):
        print(error_message)
        driver.save_screenshot(file_name + ".png")
        raise e

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        self.driver.quit()
