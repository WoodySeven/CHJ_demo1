import unittest
import time
import ddt as ddt
from selenium import webdriver

test_date = [["admin","123456","退出"],
             ["","","用户名 不可为空白"],
             ["addmdm","123456","用户名不存在"],
             ["admin","123321","用户名和密码不匹配"]]
@ddt.ddt
class BugfreeAdminLoginLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.2.87"
        driver = self.driver

    def tearDown(self):
        pass

    @ddt.unpack
    @ddt.data(*test_date)
    def test_admin_login_test(self,admin,password,flag):
        """admin的登录的所有测试用例"""
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys(admin)
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys(password)
        driver.find_element_by_id("LoginForm_rememberMe").click()
        driver.find_element_by_id("SubmitLoginBTN").click()
        time.sleep(3)
        self.assertIn(flag, driver.page_source)

if __name__ == '__main__':
    unittest.main()
