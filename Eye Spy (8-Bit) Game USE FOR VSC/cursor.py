import pyxel

class Cursor():
    width = 16
    height = 16
    xpos = 0
    ypos = 0
    u = 128
    v = 80
    drawCursor = False

    def update(self):
        self.xpos = pyxel.mouse_x
        self.ypos = pyxel.mouse_y
    
    def toggleDraw (self):
        if self.drawCursor == False:
            self.drawCursor = True
        else:
            self.drawCursor = False


    def draw(self):

        if self.drawCursor == True:
            pyxel.blt(self.xpos, self.ypos, 0, self.u, self.v, self.width, self.height, 11)