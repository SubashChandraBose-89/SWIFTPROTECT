from selenium.webdriver.common.by import By


class SwiftLogin:
    text_username_id = "username"
    text_password_id = "password"
    button_login_id = "loginbtn"
    alert_login_xpath = "//button[@class='btn btn-primary bootbox-accept']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.text_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def login(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

    def dismissAlert(self):
        self.driver.find_element(By.XPATH, self.alert_login_xpath).click()
