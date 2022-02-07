from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

lang_strings = {"es": "Añadir al carrito", "fr": "Ajouter au panier"}


def test_guest_should_see_login_link(browser):
    browser.get(link)
    correct_btn = WebDriverWait(browser, 12).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
    )
    assert browser.find_element(By.CSS_SELECTOR,".btn-add-to-basket").is_displayed()
