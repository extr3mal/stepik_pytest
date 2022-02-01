import math
from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome(executable_path="C:\\Users\\extr3\\Downloads\\chromedriver.exe")
try:

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

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
