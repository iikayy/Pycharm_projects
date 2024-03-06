from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
EMAIL = "benblacck@gmail.com"
PASSWORD = "wg6_TRt5::cxVZU"
PHONE = "8106262263"


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3759777087&f_AL=true&geoId=101165590&keywords=health%20care%20assistant&location=United%20Kingdom&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true")

# Click Sign in Button
time.sleep(2)
sign = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign.click()

# Sign in
time.sleep(5)
email = driver.find_element(By.ID, "username")
email.send_keys(EMAIL)
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys(PASSWORD)
sign_in = driver.find_element(By.CSS_SELECTOR, "div button, class")
sign_in.click()

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container__link")

# Apply for Jobs
for listing in all_listings[1:]:
    print("Opening Listing")
    listing.click()
    time.sleep(6)
    try:
        # Click Apply Button
        apply_button = driver.find_element(By.CLASS_NAME, "artdeco-button__text")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone_number = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3759777087-104850325-phoneNumber-nationalNumber"]')
        phone_number.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()


# element1 = ('<a data-control-id="WYJEjbOFrrt37/n1osOf9w==" tabindex="0" href="/jobs/view/3772028571/?eBP=NOT_ELIGIBLE_'
#             'FOR_CHARGING&amp;refId=Xd%2FPLKF2U9Dc1BiTmiGQKw%3D%3D&amp;trackingId=WYJEjbOFrrt37%2Fn1osOf9w%3D%3D&amp;'
#             'trk=flagship3_search_srp_jobs" id="ember148" '
#             'class="disabled ember-view job-card-container__link job-card-list__title" aria-label="Health Care Assistant - Theatre / Theatre Runner">)
#                     Health Care Assistant - Theatre / Theatre Runner
#                 </a>'
#
# element2 = '<a data-control-id="XFtntv4Njw5Twad7OvcY9g==" tabindex="0" href="/jobs/view/3759777087/?eBP=NOT_ELIGIBLE_'
#                     'FOR_CHARGING&amp;refId=Xd%2FPLKF2U9Dc1BiTmiGQKw%3D%3D&amp;trackingId=XFtntv4Njw5Twad7OvcY9g%3D%3D&amp;'
#                     'trk=flagship3_search_srp_jobs" id="ember136" class="disabled ember-view job-card-container__link job-card-list__title" aria-label="Healthcare Assistant">
#                     Healthcare Assistant
#                 </a>'

# <span class="artdeco-button__text">
#     Easy Apply
# </span>