from selenium import webdriver
import time

import pytest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class TestAbs:

    @pytest.fixture()
    def setup(self, link):
        self.browser = webdriver.Chrome(executable_path="C:\\Users\\extr3\\Downloads\\chromedriver.exe")
        yield
        browser.quit()

    def test_reg1(setup):
        browser.get(link1)
        input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_xpath("//input[@placeholder='Input your phone:']")
        input4.send_keys("Russia")
        input5 = browser.find_element_by_xpath("//input[@placeholder='Input your address:']")
        input5.send_keys("test")
        button = browser.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        text = browser.find_element_by_xpath("//h1").text
        self.assertEqual(text, "Congratulations! You have successfully registered!")
        # успеваем скопировать код за 30 секунд
        # time.sleep(30)
        # закрываем браузер после всех манипуляций

    def test_reg2(self):
        browser.get(link2)
        input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_xpath("//input[@placeholder='Input your phone:']")
        input4.send_keys("Russia")
        input5 = browser.find_element_by_xpath("//input[@placeholder='Input your address:']")
        input5.send_keys("test")
        button = browser.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()
