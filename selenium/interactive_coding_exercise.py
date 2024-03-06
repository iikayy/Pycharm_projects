from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # number.click()
#
# navy_day = driver.find_element(By.LINK_TEXT, "Navy Day")
# # navy_day.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("ikay")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("ojiako")

email = driver.find_element(By.NAME, "email")
email.send_keys("ii_kayy@yahoo.com")

signup = driver.find_element(By.CSS_SELECTOR, ".btn-block")
signup.click()


# driver.quit()