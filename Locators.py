from selenium.webdriver.common.by import By


class PagesLocators:
    browser_btn = (By.XPATH, "//span[text()='Browser']")
    browser_btn_error = (By.XPATH, "//a[contains(@class,'relative inline-flex')][1]")
    game_canvas = (By.ID, "react-unity-webgl-canvas-1")

