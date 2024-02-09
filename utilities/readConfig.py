

import configparser

config = configparser.RawConfigParser()

config.read("D:\\E Drive Data\\CREDENCE\\9. YUSUF SIR - Automation Testing\\0. PRACTICAL\\PRACTICALS\\NOP_Commerse\\configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def getUserName():
        userName = config.get("login page", "username")
        return userName

    @staticmethod
    def getPassword():
        password = config.get('login page', 'password')
        return password

    @staticmethod
    def getFirstName():
        firstName = config.get('addCustomer page', 'firstname')
        return firstName

    @staticmethod
    def getLastName():
        lastName = config.get('addCustomer page', 'lastname')
        return lastName

    @staticmethod
    def getNewPassword():
        newPassword = config.get('addCustomer page', 'password')
        return newPassword

    @staticmethod
    def getCompanyName():
        companyName = config.get('addCustomer page', 'companyname')
        return companyName

    @staticmethod
    def getAdminContent():
        adminContent = config.get('addCustomer page', 'admincontent')
        return adminContent



