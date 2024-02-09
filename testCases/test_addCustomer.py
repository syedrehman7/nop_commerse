import random
import string
import time

from pageObjects.loginPage import LoginPageClass
from pageObjects.addCustomerPage import AddCustomerPageClass

from utilities.readConfig import ReadConfig
from utilities.logger import LoggenClass

class Test_AddCustomerClass:

    # read config login page data
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    # read config addcustomer page data
    firstName = ReadConfig.getFirstName()
    lastName = ReadConfig.getLastName()
    newPassword = ReadConfig.getNewPassword()
    companyName = ReadConfig.getCompanyName()
    adminContent = ReadConfig.getAdminContent()

    # import logger
    log = LoggenClass.log_generator()

    def test_addCustomer_003(self, setup):
        self.driver = setup

        # login
        self.log.info("entering login details")
        self.lp = LoginPageClass(self.driver)
        self.lp.Enter_username(self.username)
        self.lp.Enter_password(self.password)
        self.lp.Click_loginButton()
        self.log.info("login done")
        time.sleep(1)

        # method call and moving to add new
        self.ac = AddCustomerPageClass(self.driver)
        self.log.info("moving to add customer page")
        self.ac.Click_customerMain()
        self.ac.Click_customerSubMain()
        self.ac.Click_addNewButton()
        self.log.info("at add customer page")
        time.sleep(3)

        # filling the data
        self.log.info("start filling the details")
        email = Generate_Email()
        self.ac.Enter_email(email)
        self.ac.Enter_password(self.newPassword)
        self.ac.Enter_firstName(self.firstName)
        self.ac.Enter_lastName(self.lastName)
        self.ac.Click_Gender("Female")
        self.ac.Enter_DOB("12/25/1995")
        self.ac.Enter_companyName(self.companyName)
        self.ac.Checked_taxExempt()
        self.ac.Click_newsLetter()
        self.ac.Select_newsLetter_list("Your store name")
        self.ac.Select_managerVendor("Vendor 2")
        self.ac.Checked_active()
        self.ac.Enter_adminContent(self.adminContent)
        self.log.info("data filled")
        self.ac.Click_saveButton()
        self.log.info("clicked save button")
        time.sleep(5)

        # verify save details
        if self.ac.Verify_saveDetails() == "Save Customer":
            self.log.info("add new customer succesfull")
            self.log.info("taking screenshot of pass new customer")
            self.driver.save_screenshot("D:\\E Drive Data\\CREDENCE\\9. YUSUF SIR - Automation Testing\\0. PRACTICAL\\PRACTICALS\\NOP_Commerse\\screenshots\\test_addCustomer_003_pass.png")
            assert True
        else:
            self.log.info("add new customer UNsuccessfull")
            self.log.info("taking screenshot of fail new customer")
            self.driver.save_screenshot("D:\\E Drive Data\\CREDENCE\\9. YUSUF SIR - Automation Testing\\0. PRACTICAL\\PRACTICALS\\NOP_Commerse\\screenshots\\test_addCustomer_003_fail.png")
            assert False


def Generate_Email():
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    domain = ''.join(random.choices(string.ascii_lowercase, k=6)) + ".com"
    return f"{username}@{domain}"


