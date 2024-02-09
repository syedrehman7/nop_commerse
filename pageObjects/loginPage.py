from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPageClass:

    Type_username_xpath = "// input[ @ id = 'Email']"
    Type_password_xpath = "//input[@id='Password']"
    Click_loginButton_xpath = "//button[@type='submit']"
    Click_logoutButton_xpath = "//a[normalize-space()='Logout']"


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Enter_username(self, username):
        self.driver.find_element(By.XPATH, self.Type_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.Type_username_xpath).send_keys(username)

    def Enter_password(self, password):
        self.driver.find_element(By.XPATH, self.Type_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.Type_password_xpath).send_keys(password)

    def Click_loginButton(self):
        self.driver.find_element(By.XPATH, self.Click_loginButton_xpath).click()

    def Click_logoutButton(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.Click_logoutButton_xpath)))
            self.driver.find_element(By.XPATH, self.Click_logoutButton_xpath).click()
        except:
            pass

    def Verify_Login(self):
        try:
            self.driver.find_element(By.XPATH, self.Click_logoutButton_xpath)
            return "Verify login pass"
        except:
            print("verify login fail")
            return "Login Fail"








