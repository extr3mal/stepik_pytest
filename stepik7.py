import math

import pytest
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

answer = math.log(int(time.time()))


@pytest.mark.parametrize('test_url', ["https://stepik.org/lesson/236895/step/1",
                                      "https://stepik.org/lesson/236896/step/1",
                                      "https://stepik.org/lesson/236897/step/1",
                                      "https://stepik.org/lesson/236898/step/1",
                                      "https://stepik.org/lesson/236899/step/1",
                                      "https://stepik.org/lesson/236903/step/1",
                                      "https://stepik.org/lesson/236904/step/1",
                                      "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, test_url):
    browser.get(test_url)
    answer_field = WebDriverWait(browser, 12).until(
        EC.visibility_of_element_located((By.XPATH, '//textarea'))
    )
    answer_field.click()
    curr_answer = math.log(int(time.time()))
    answer_field.send_keys(curr_answer)
    submit_btn = browser.find_element(By.CLASS_NAME, "submit-submission")
    submit_btn.click()
    correct_field = WebDriverWait(browser, 12).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='attempt__message']//pre"))
    )
    assert correct_field.text == 'Correct!'
