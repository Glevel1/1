import time
import keyboard
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from BaseModule import Base
from Locators import PagesLocators
import pyautogui


class Func(Base):
    def select_browser_game(self):
        self.GoToGamePage()
        time.sleep(1.5)
        try:
            self.find_clickable_element(PagesLocators.browser_btn, 10).click() #Переход в браузерную версию веб-игры
        except TimeoutException:
            self.find_clickable_element(PagesLocators.browser_btn_error, 4).click()
        # time.sleep(60) #Задержка, чтоб юзер зашел в свой аккаунт

    def move_forward(self):
        keyboard.press("w")
        time.sleep(1.3)
        keyboard.release("w")

    def move_right(self):
        keyboard.press("d")
        time.sleep(0.7)
        keyboard.release("d")

    def move_left(self):
        keyboard.press("a")
        time.sleep(0.2)
        keyboard.release("a")

    def move_back(self):
        keyboard.press("s")
        time.sleep(0.05)
        keyboard.release("s")







    def navigation(self):
        self.select_browser_game()
        canvas = self.find_element(PagesLocators.game_canvas, time=80) #Дожидание загрузки вью игры(Canvas)
        #Получение высоты и ширины канваса у юзера во время локального запуска
        width = canvas.size['width']
        height = canvas.size['height']
        time.sleep(10)
        #Переход по координатам к кнопке продолжения во вью игры
        screenWidth, screenHeight = pyautogui.size() #Получение ширины и высоты экрана
        pyautogui.moveTo(screenWidth / 2, screenHeight / 1.25)
        #Нажатие на кнопку продолжения
        pyautogui.click()
        time.sleep(3)
        pyautogui.click()
        #Навигация до точки
        self.move_forward()
        self.move_right()
        self.move_forward()
        keyboard.press("d")
        time.sleep(0.4)
        keyboard.release("d")
        keyboard.press("w")
        time.sleep(0.4)
        keyboard.release("w")
        self.move_left()
        keyboard.press("F")
        time.sleep(0.2)
        keyboard.release("F")
        time.sleep(3)
        actual_position = pyautogui.position()
        pyautogui.moveTo(actual_position[0] + 600, None)
        time.sleep(2)
        pyautogui.click()
        time.sleep(20)
        # time.sleep(60) #Задержка до окончания бая













