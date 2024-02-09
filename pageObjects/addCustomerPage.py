from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomerPageClass:

    Click_cutomerMain_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    Click_customerSubMain_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    Click_addNewButton_xpath = "//a[normalize-space()='Add new']"
    Type_email_xpath = "//input[@id='Email']"
    Type_password_xpath = "//input[@id='Password']"
    Type_firtName_xpath = "//input[@id='FirstName']"
    Type_lastName_xpath = "//input[@id='LastName']"
    Click_genderMale_xpath = "//input[@id='Gender_Male']"
    Click_genderFemale_xpath = "//input[@id='Gender_Female']"
    Type_DOB_xpath = "//input[@id='DateOfBirth']"
    Type_comapnyName_xpath = "//input[@id='Company']"
    Checked_taxExempt_xpath = "//input[@id='IsTaxExempt']"
    Select_newsLetter_xpath = '/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[9]/div[2]/div/div[1]/div/div'
    Select_newsLetterList_xpath = "//li[normalize-space()='Your store name']"
    Select_newsLetterList2_xpath = "//li[normalize-space()='Test store 2']"
    Select_customerRoles_xpath = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    Select_manageVendor_xpath = '//*[@id="VendorId"]'
    Checked_active_xpath = '//*[@id="Active"]'
    Type_adminComment_xpath = "//textarea[@id='AdminComment']"
    Click_saveButton_xpath = "//button[@name='save']"
    Verify_saveDeatil_xpath = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver = driver

    def Click_customerMain(self):
        self.driver.find_element(By.XPATH, self.Click_cutomerMain_xpath).click()

    def Click_customerSubMain(self):
        self.driver.find_element(By.XPATH, self.Click_customerSubMain_xpath).click()

    def Click_addNewButton(self):
        self.driver.find_element(By.XPATH, self.Click_addNewButton_xpath).click()

    def Enter_email(self, email):
        self.driver.find_element(By.XPATH, self.Type_email_xpath).send_keys(email)

    def Enter_password(self, password):
        self.driver.find_element(By.XPATH, self.Type_password_xpath).send_keys(password)

    def Enter_firstName(self, firstName):
        self.driver.find_element(By.XPATH, self.Type_firtName_xpath).send_keys(firstName)

    def Enter_lastName(self, lastName):
        self.driver.find_element(By.XPATH, self.Type_lastName_xpath).send_keys(lastName)

    def Click_Gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.Click_genderMale_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.Click_genderFemale_xpath).click()

    def Enter_DOB(self, dob):
        self.driver.find_element(By.XPATH, self.Type_DOB_xpath).send_keys(dob)

    def Enter_companyName(self, companyName):
        self.driver.find_element(By.XPATH, self.Type_comapnyName_xpath).send_keys(companyName)

    def Checked_taxExempt(self):
        self.driver.find_element(By.XPATH, self.Checked_taxExempt_xpath).click()

    def Click_newsLetter(self):
        self.driver.find_element(By.XPATH, self.Select_newsLetter_xpath).click()

    def Select_newsLetter_list(self, newsLetter):
        if newsLetter == "Your store name":
            self.driver.find_element(By.XPATH, self.Select_newsLetterList_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.Select_newsLetterList2_xpath).click()

    def Select_managerVendor(self, value):
        customerRole = Select(self.driver.find_element(By.XPATH, self.Select_manageVendor_xpath))
        customerRole.select_by_visible_text(value)

    def Checked_active(self):
        self.driver.find_element(By.XPATH, self.Checked_active_xpath).click()

    def Enter_adminContent(self, adminContent):
        self.driver.find_element(By.XPATH, self.Type_adminComment_xpath).send_keys(adminContent)

    def Click_saveButton(self):
        self.driver.find_element(By.XPATH, self.Click_saveButton_xpath).click()

    def Verify_saveDetails(self):
        try:
            self.driver.find_element(By.XPATH, self.Verify_saveDeatil_xpath)
            return "Save Customer"
        except:
            print("save customer fail")

