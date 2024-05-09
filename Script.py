import time

from BaseModule import Base
from Functions import Func


class MainScript(Func):
    def script(self):
        automation = Func()
        x = 0
        while x < 1000:
            automation.navigation()
            x += 1



test = MainScript()
test.script()


