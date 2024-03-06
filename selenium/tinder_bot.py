from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
EMAIL = "benblacck@gmail.com"
PASSWORD = "#@6?weyu"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

# Accept cookie
cookie = driver.find_element(By.XPATH, '//*[@id="o2120851872"]/div/div[2]/div/div/div[1]/div[1]/button')
cookie.click()
time.sleep(2)

#login
login = driver.find_element(By.XPATH, '//*[@id="o2120851872"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
time.sleep(3)

#login with facebook
facebook = driver.find_element(By.XPATH, '//*[@id="o392470796"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook.click()
time.sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys(EMAIL)

password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys(PASSWORD)

log_in = driver.find_element(By.NAME, "login")
log_in.click()

driver.switch_to.window(base_window)

# share location
time.sleep(20)
allow_button = driver.find_element(By.XPATH, '//*[@id="o2120851872"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button/span/span/svg')
allow_button.click()
time.sleep(3)

# disable notifications
notifications = driver.find_element(By.XPATH, '//*[@id="o392470796"]/main/div/div/div/div[3]/button[2]')
notifications.click()

# matching
time.sleep(20)
for i in range(20):
    time.sleep(4)
    like_button = driver.find_element(By.XPATH, ']/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button/span/span/svg/path')
    like_button.click()
    # except NoSuchElementException:
    #     time.sleep(4)
    #     like_button.click()


