import pyautogui
from PIL import ImageGrab
import keyboard
import time

class Modules:
    def __init__(self, start_x, start_y, end_x, end_y, modules):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.modules = modules

    @property
    def coordinates(self):
        return (self.start_x, self.start_y, self.end_x, self.end_y)

    def get_best_available_module(self):
        image = ImageGrab.grab(bbox=self.coordinates)
        for module in self.modules:
            module_points = module.available(image)
            if module_points:
                return module_points.pop()

    def add_module(self, module):
        pyautogui.click(self.start_x + module[0], self.start_y + module[1])

class Module:
    def __init__(self, x, y, x_increment=None, y_increment=None, color=None, minimum_red=None, minimum_green=None, minimum_blue=None):
        self.x = x
        self.y = y
        self.x_increment = x_increment
        self.y_increment = y_increment
        self.color = color
        self.minimum_red=minimum_red
        self.minimum_green=minimum_green
        self.minimum_blue=minimum_blue

    def available(self, image):
        # pyautogui.moveTo(1603 + self.x, 369 + self.y)
        width, height = image.size
        available = []
        if self.x_increment is not None:
            x_to_check = range(self.x, width, self.x_increment)
        else:
            x_to_check = [self.x]
        if self.y_increment is not None:
            y_to_check = range(self.y, height, self.y_increment)
        else:
            y_to_check = [self.y]

        for x in x_to_check:
            for y in y_to_check:
                red, green, blue = image.getpixel((x, y))
                if self.color and (red, green, blue) not in self.color:
                    continue
                if self.minimum_red and red < self.minimum_red:
                    continue
                if self.minimum_green and red < self.minimum_green:
                    continue
                if self.minimum_blue and red < self.minimum_blue:
                    continue

                available.append((x,y))

        return available


class FirstUpgrade(Module):
    def __init__(self):
        super().__init__(2, 2, minimum_red=160)

class Helper(Module):
    def __init__(self):
        super().__init__(65, 24, y_increment=63, minimum_red=150)

if __name__ == "__main__":
    pyautogui.PAUSE = 0.01
    upgrades = Modules(1603, 260, 1902, 320,
        [
            FirstUpgrade()
        ]
    )
    helpers = Modules(1603, 369, 1902, 975,
        [
            Helper()
        ]
    )
    while True:
        while True:
            upgrade = upgrades.get_best_available_module()
            if upgrade:
                upgrades.add_module(upgrade)
                continue
            helper = helpers.get_best_available_module()
            if helper:
                helpers.add_module(helper)
                continue

            break
        for click in range(10000):
            print(f"click number: {click}", end="\r")
            if keyboard.is_pressed("b"):
                break
            if keyboard.is_pressed("q"):
                raise KeyboardInterrupt("User ended the app!")
            pyautogui.click(300, 480)
