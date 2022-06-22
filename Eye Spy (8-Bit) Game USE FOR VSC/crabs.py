import pyxel
import time

class Crabs:
    width = 0
    height = 0
    xpos = 0
    ypos = 0
    u = 0
    u_strt = 0
    v = 0
    image = 0
    drawItem = True
    mytime = 0


    def __init__(self,u,v,xpos,ypos, w, h):
        self.u = u
        self.v = v
        self.xpos = xpos
        self.ypos = ypos
        self.u_strt = u
        self.width = w
        self.height = h
        self.mytime = time.time()

    def update (self):
        if self.mytime < time.time():
            if self.u == self.u_strt:
                self.u = self.u - 8
            else:
                self.u = self.u+8
            self.mytime = time.time()+0.25

    def draw (self):
        if self.drawItem == True:
            

            pyxel.blt(self.xpos, self.ypos, self.image, self.u, self.v, self.width, self.height)

    def toggleDraw (self):
       if self.drawItem == False:
            self.drawItem = True
       else:
          self.drawItem = False