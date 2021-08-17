import pyxel

class Checkmark():
    name = ""
    width = 16
    height = 16
    xpos = 0
    ypos = 0
    u = 0
    v = 0

    def __init__(self, name, xpos, ypos):
        if name == "j_level_checkmark":
            u = 112
            v = 80
        elif name == "crab_rave_checkmark":
            u = 112
            v = 96

        else:
            u = 128
            v = 64