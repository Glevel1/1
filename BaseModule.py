from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth



class Base:
    url = "https://capnco.gg/download"
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")
    options.page_load_strategy = 'eager'
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    stealth(driver, languages=["en-US", "en"], vendor="Google Inc.", platform="Win32", webgl_vendor="Intel Inc.", renderer="Intel Iris OpenGL Engine", fix_hairline=True)



    def GoToGamePage(self):
        self.driver.maximize_window() #Открытие браузера в полную шириун и высоту
        self.driver.get(self.url) #Переход на главную страницу веб-сервиса
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            'source': '''
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
          '''
        })

    def find_element(self, locator, time):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Невозможно найти локатор {locator}")

    def find_clickable_element(self, locator, time):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f"Невозможно найти локатор {locator}")



