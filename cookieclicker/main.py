import pyautogui
import keyboard

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
        image = pyautogui.screenshot(region=self.coordinates)
        for module in self.modules:
            if module.available(image):
                return module

    def add_module(self, module):
        pyautogui.click(self.start_x + module.x, self.start_y + module.y)

class Module:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def available(self, image):
        # pyautogui.moveTo(1603 + self.x, 369 + self.y)
        return image.getpixel((self.x, self.y)) in self.color


class FirstUpgrade(Module):
    def __init__(self):
        super().__init__(30, 72, [(144,71,17),(255,254,248)])

class Cursor(Module):
    def __init__(self):
        super().__init__(71, 24, [(255,255,255)])

class Grandma(Module):
    def __init__(self):
        super().__init__(71, 84, [(255,255,255)])

class Farm(Module):
    def __init__(self):
        super().__init__(73, 150, [(255,255,255)])

class Mine(Module):
    def __init__(self):
        super().__init__(71, 224, [(255,255,255)])

class Factory(Module):
    def __init__(self):
        super().__init__(73, 280, [(255,255,255)])

class Bank(Module):
    def __init__(self):
        super().__init__(73, 350, [(255,255,255)])

class Temple(Module):
    def __init__(self):
        super().__init__(77, 410, [(255,255,255)])

class WizardTower(Module):
    def __init__(self):
        super().__init__(73, 470, [(255,255,255)])


if __name__ == "__main__":
    pyautogui.PAUSE = 0.01
    helpers = Modules(1603, 369, 1902, 975,
        [
            WizardTower(),
            Temple(),
            Bank(),
            Factory(),
            Mine(),
            Farm(),
            Grandma(),
            Cursor(),
        ]
    )
    upgrades = Modules(1603, 245, 1902, 380,
        [
            FirstUpgrade()
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
