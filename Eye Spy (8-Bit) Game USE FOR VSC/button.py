import pyxel
from bg import BG
from bg import levels


class button:
    def __init__(self, name, x, y, width, height, background, bg):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.background = background
        self.bg = bg
        
    def on_click(self):
        self.bg.change_screen(background)
        pyxel.play(1, 19, loop=False)
        pyxel.play(2, 20, loop=False)
        self.update_funct = self.update_dict.get("change_level")