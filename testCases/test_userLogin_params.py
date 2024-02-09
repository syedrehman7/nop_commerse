import time

import pytest

from pageObjects.loginPage import LoginPageClass
from utilities.readConfig import ReadConfig


@pytest.mark.usefixtures("setup")
class TestUserLoginParamsClass:

    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def test_userLoginParams_004(self, setup, DataforLogin):
        self.driver = setup

        self.lp = LoginPageClass(self.driver)
        self.lp.Enter_username(DataforLogin[0])
        self.lp.Enter_password(DataforLogin[1])
        self.lp.Click_loginButton()
        time.sleep(5)

        actualCondition = []

        if self.lp.Verify_Login() == "Verify login pass":
            if DataforLogin[2] == 'pass':
                print('expected login - pass')
                actualCondition.append('pass')
                self.lp.Click_logoutButton()
            elif DataforLogin[2] == 'fail':
                print('expected login - fail')
                actualCondition.append('fail')
        else:
            if DataforLogin[2] == 'fail':
                print('expected login - fail')
                actualCondition.append('pass')
            elif DataforLogin[2] == 'pass':
                print('expected login - pass')
                actualCondition.append('fail')

        print(actualCondition)
        if 'pass' in actualCondition:
            print('assert true')
            assert True
        else:
            print('assert false')
            assert False

