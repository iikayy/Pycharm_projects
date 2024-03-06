from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from InternetSpeedTwitterBot import InternetSpeedTwitterBot
import time

from selenium.webdriver.common.selenium_manager import SeleniumManager

PROMISED_UP = 10
PROMISED_DOWN = 150
TWITTER_EMAIL = "benblacck@outlook.com"
TWITTER_PASSWORD = "#@6?weyu"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
CHROME_DRIVER_PATH = SeleniumManager().driver_location(options=chrome_options)
# CHROME_DRIVER_PATH = "C:\\Users\V V\.cache\selenium\chromedriver\win64\119.0.6045.105\chromedriver.exe"
driver.get("https://www.speedtest.net/")


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        continue_button = driver.find_element(By.CSS_SELECTOR, 'button .onetrust-accept-btn-handler')
        continue_button.click()

        time.sleep(3)
        go_button = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        time.sleep(120)
        down_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f"down:{down_speed}")

        up_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"up:{up_speed}")

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
