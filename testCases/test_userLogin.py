import allure
import pytest
from allure_commons.types import AttachmentType

from pageObjects.loginPage import LoginPageClass
from utilities.logger import LoggenClass
from utilities.readConfig import ReadConfig


@pytest.mark.usefixtures("setup")
class Test_UserLogin:
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    log = LoggenClass.log_generator()

    @allure.feature('page_title')
    @allure.story('Verifying the page title')
    @allure.issue('ABC-123')
    @allure.link(' https://admin-demo.nopcommerce.com/',name='NOP Commerse Website')
    @allure.title('NonCom - Test page_title')
    @allure.description('My test description')
    @allure.link('https://www.example.com')
    @allure.severity(allure.severity_level.CRITICAL)

    def test_login_URL_001(self, setup):
        self.driver = setup
        url_title = self.driver.title
        if url_title == "Your store. Login":
            self.log.info("login url pass")
            self.log.info("taking screenshot of login pass")
            self.driver.save_screenshot("D:\\E Drive Data\\CREDENCE\\9. YUSUF SIR - Automation Testing\\0. PRACTICAL\\PRACTICALS\\NOP_Commerse\\screenshots\\test_login_URL_001_pass.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_URL_001-Pass",
                          attachment_type=AttachmentType.PNG)
            assert True
        else:
            self.log.info("login url fail")
            self.log.info("taking sc of fail url")
            self.driver.save_screenshot("D:\\E Drive Data\\CREDENCE\\9. YUSUF SIR - Automation Testing\\0. PRACTICAL\\PRACTICALS\\NOP_Commerse\\screenshots\\test_login_URL_001_fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_URL_001-Fail",
                          attachment_type=AttachmentType.PNG)
            assert False


    def test_userLogin_002(self, setup):

        self.driver = setup
        self.lp = LoginPageClass(self.driver)
        self.log.info("enter username")
        self.lp.Enter_username(self.userName)
        self.log.info("enter password")
        self.lp.Enter_password(self.password)
        self.log.info("click login button")
        self.lp.Click_loginButton()


        if self.lp.Verify_Login() == "Verify login pass":
            self.log.info("login pass")
            self.log.info("taking sc of login pass")
            self.driver.save_screenshot("D:\\E Drive Data\\CREDENCE\\9. YUSUF SIR - Automation Testing\\0. PRACTICAL\\PRACTICALS\\NOP_Commerse\\screenshots\\test_userLogin_002_pass.png")
            self.log.info("click logout button")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_userLogin_002-Pass",
                          attachment_type=AttachmentType.PNG)
            self.lp.Click_logoutButton()
            assert True
        else:
            self.log.info("login fail")
            self.log.info("taking sc of fail login case")
            self.driver.save_screenshot("D:\\E Drive Data\\CREDENCE\\9. YUSUF SIR - Automation Testing\\0. PRACTICAL\\PRACTICALS\\NOP_Commerse\\screenshots\\test_userLogin_002_fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_userLogin_002-Fail",
                          attachment_type=AttachmentType.PNG)
            assert False


# pytest -v -n=2 --html=HtmlReports/myreport.html
# pytest -v -n=2 --html=HtmlReports/myreport.html -m sanity -p
# pytest -v -n=2 -m sanity --html=HtmlReports/myreport.html --alluredir="D:\Credence Class Notes\CredenceBatches\Credence_Automation_Jan 24\nopcom_Pytest\AllureReports" --browser firefox  -p no:warnings
# pytest -v -n=2 -m sanity --alluredir="D:\Credence Class Notes\CredenceBatches\Credence_Automation_Jan 24\nopcom_Pytest\AllureReports" --browser firefox  -p no:warnings
# allure serve "allure_report_folder_path" # To generate report






