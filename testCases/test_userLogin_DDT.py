#
#
#
# from utilities import excelMethod
# from pageObjects.loginPage import LoginPageClass
#
#
# class Test_userLogin_DDT_Class:
#
#     excelFilePath = "D:\\E Drive Data\\CREDENCE\\9. YUSUF SIR - Automation Testing\\0. PRACTICAL\\PRACTICALS\\NOP_Commerse\\testData\\testData.xlsx"
#
#     def test_userLogin_DDT_005(self, setup):
#
#         self.driver = setup
#
#         self.lp = LoginPageClass(self.driver)
#
#         self.rows = excelMethod.numRows(self.excelFilePath,'loginSheet')
#         print(str(self.rows))
#
#         TestCase_Status_List = []
#         for r in range(2, self.rows+1):
#             self.username = excelMethod.readData(self.excelFilePath, 'loginSheet', r, 2)
#             self.password = excelMethod.readData(self.excelFilePath, 'loginSheet', r, 3)
#             self.expectedResult = excelMethod.readData(self.excelFilePath, 'loginSheet', r, 4)
#
#             self.lp.Enter_username(self.username)
#             self.lp.Enter_password(self.password)
#             self.lp.Click_loginButton()
#
#             if self.lp.Verify_Login() == "Verify login pass":
#                 excelMethod.writeData(self.excelFilePath, 'loginSheet', r, 5, 'pass')
#                 if self.expectedResult == 'pass':
#                     print('expected result - pass')
#                     # excelMethod.writeData(self.excelFilePath, 'loginSheet', r, 5, 'pass')
#                     TestCase_Status_List.append('pass')
#                 elif self.expectedResult == 'fail':
#                     print('expected result - fail')
#                     excelMethod.writeData(self.excelFilePath, 'loginSheet', r, 5, 'pass')
#                     TestCase_Status_List.append('fail')
#             else:
#                 print('login nhi hua')
#                 if self.expectedResult == 'fail':
#                     print('expected result - fail')
#                     excelMethod.writeData(self.excelFilePath, 'loginSheet', r, 5, 'fail')
#                     TestCase_Status_List.append('pass')
#                 elif self.expectedResult == 'pass':
#                     print('expected result - pass')
#                     excelMethod.writeData(self.excelFilePath, 'loginSheet', r, 5, 'fail')
#                     TestCase_Status_List.append('fail')
#
#         print(TestCase_Status_List)
#
#         if 'pass' in TestCase_Status_List:
#             assert True
#
#         elif 'fail' in TestCase_Status_List:
#             assert False
#
#
#
#
