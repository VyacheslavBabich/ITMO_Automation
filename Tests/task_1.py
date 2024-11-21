from selenium.webdriver.common.by import By
from selenium import webdriver

def check_elements():

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    try:
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.CSS_SELECTOR, ".btn_action")

        print("Элементы найдены")
    except:
        print("Элементы не найдены")

    driver.quit()

check_elements()
