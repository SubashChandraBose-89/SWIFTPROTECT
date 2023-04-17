import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class SwiftSearchFI:
    report_xpath = "//a[contains(text(), 'Report Created')][1]"
    fi_details_xpath = "//a[contains(text(), 'Field Interview Details')]"
    screenshot_1 = r"C:\Users\sudha\PycharmProjects\SWIFT PROTECT HYBRID\Screenshots\SubjectDetailsImage.png"
    subject_details_xpath = "//a[contains(text(), 'Subject Details')]"
    name_xpath = "//a[contains(text(), 'Anderson')]"
    screenshot_2 = r"C:\Users\sudha\PycharmProjects\SWIFT PROTECT HYBRID\Screenshots\SubjectDetailsImage.png"
    other_details_xpath = "//a[contains(text(), 'Other Details')]"
    screenshot_3 = r"C:\Users\sudha\PycharmProjects\SWIFT PROTECT HYBRID\Screenshots\OtherDetailsImage.png"
    address_xpath = "//a[contains(text(), 'Address')]"
    screenshot_4 = r"C:\Users\sudha\PycharmProjects\SWIFT PROTECT HYBRID\Screenshots\AddressImage.png"
    vehicle_details_xpath = "//a[contains(text(), 'Vehicle Details')]"
    screenshot_5 = r"C:\Users\sudha\PycharmProjects\SWIFT PROTECT HYBRID\Screenshots\VehicleDetailsImage.png"

    def __init__(self, driver, WebDriverWait):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def selectReport(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.report_xpath))).click()

    def waitTill(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fi_details_xpath)))

    def takeScreenshotFI(self):
        time.sleep(2)
        self.driver.save_screenshot(self.screenshot_1)

    def switchToSubDetails(self):
        self.subject_details = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.subject_details_xpath)))
        self.subject_details.click()

    def clickName(self):
        self.driver.find_element(By.XPATH, self.name_xpath).click()

    def takeScreenshotSubDetail(self):
        time.sleep(2)
        self.driver.save_screenshot(self.screenshot_2)

    def switchToOtherDetails(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.other_details_xpath))).click()

    def takeScreeshotOthrDetails(self):
        time.sleep(2)
        self.driver.save_screenshot(self.screenshot_3)

    def switchToAddress(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.address_xpath))).click()

    def takeScreenshotAddress(self):
        time.sleep(2)
        self.driver.save_screenshot(self.screenshot_4)

    def switchToVehicle(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.vehicle_details_xpath))).click()

    def takeScreenshotVehicleDetails(self):
        time.sleep(2)
        self.driver.save_screenshot(self.screenshot_5)



