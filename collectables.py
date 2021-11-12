import pyxel
from crabs import Crabs

class Collectables:
  drawItem = True
  name = ""
  width = 16
  height = 16
  xpos = 0
  ypos = 0
  u = 0
  v = 0
  image = 0
  body = 0
  value = 0
  sound = 52

  def __init__(self, name, xpos, ypos, u, v, value, width = None, height = None, sound = None):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.u = u
        self.v = v
        self.value = value
        self.body = (self.xpos+8, self.ypos+8)
        if width == None:
            self.width = 16
            self.height = 16
        else:
            self.width = width
            self.height = height
        if sound != None:
            self.sound = sound
  def update(self, magX, magY, margin):
    if self.body[0] >= magX - margin and self.body[0] <= magX + margin:
        if self.body[1] >= magY - margin and self.body[1] <= magY + margin:
            self.u = 0
            self.v = 240
            print ("Congrats! You found " + self.name + "!!!")
            pyxel.play(2, self.sound, loop=False)
            return True
    return False
  def toggleDraw (self):
       if self.drawItem == False:
            self.drawItem = True

       else:
          self.drawItem = False
  def draw(self):

      if self.drawItem == True:
          pyxel.blt(self.xpos, self.ypos, self.image, self.u, self.v, self.width, self.height, 11)



class Collectable_Crab(Crabs, Collectables):
    def __init__(self, u, v, xpos, ypos, name, w, h, value):

        Crabs.__init__(self, u, v, xpos, ypos, w, h)
        Collectables.__init__(self, name, xpos, ypos, u, v, value, w, h)
    def update(self, magX = None, magY = None, margin = None):

        if margin != None:
            return Collectables.update(self, magX, magY, margin)
        else:
            Crabs.update(self)

    def toggleDraw(self):
        Collectables.toggleDraw(self)

    def draw(self):
        Collectables.draw(self)