from selenium import webdriver
from selenium.webdriver.common.by import By

URL ="https://www.amazon.com/dp/B075CYMYK6/ref=twister_B0CMMLY4YS?_encoding=UTF8&th=1"
#keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")
#
# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")
#
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, "submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation widget a")
# print(documentation_link.text)


# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/')
# print(bug_link.text)


event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
upcoming_events = {}

for n in range(len(event_times)):
    upcoming_events[n]: {
        'time': event_times[n].text,
        'name': event_names[n].text,
    }

print(upcoming_events)

# closes the active(single) tab
# driver.close()
#Quits the entire tab
driver.quit()


