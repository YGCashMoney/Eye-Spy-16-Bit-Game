import pyxel

class MagGlass:
    width = 16
    height = 16
    xpos = 0
    ypos = 0
    u = 0
    v = 0
    margin = 0
    drawMag = True

    #the values given to the attributes here, are the default values = 0
    #when a default value is left at 0, "", None that means its gonna be changed later on.....
    def __init__(self, whichglass):
        #text --> "small", "medium", "large"
        if whichglass == "small":
            self.u = 8
            self.v = 8
            self.width = 16
            self.height = 16
            self.margin = 4.5
        elif whichglass == "medium":
            self.u = 80
            self.v = 32
            self.width = 32
            self.height = 32
            self.margin = 9
        elif whichglass == "large":
            self.u = 48
            self.v = 128
            self.width = 64
            self.height = 65
            self.margin = 18

        elif whichglass == "corrupted":
            self.u = 152
            self.v = 72
            self.width = 32
            self.height = 32
            self.margin = 9
        else:
            print("You have typed in an invalid input. Please try again.")
    

    def getCenter (self):
        if self.u == 8 and self.v == 8:
            return (self.xpos+23+10.5, self.ypos+20+6.5)
        elif (self.u == 80 and self.v == 32) or (self.u == 152 and self.v == 72):
            return (self.xpos+23+18.5, self.ypos+20+14.5)
        else:
            return (self.xpos+23+52, self.ypos+20+26)

    def changeGlass (self, whichglass):
        if whichglass == "small":
            self.u = 8
            self.v = 8
            self.width = 16
            self.height = 16
            self.margin = 4.5
        elif whichglass == "medium":
            self.u = 80
            self.v = 32
            self.width = 32
            self.height = 32
            self.margin = 9
        elif whichglass == "large":
            self.u = 48
            self.v = 128
            self.width = 64
            self.height = 65
            self.margin = 18

        elif whichglass == "corrupted":
            self.u = 152
            self.v = 72
            self.width = 32
            self.height = 32
            self.margin = 9
        else:
            print("You have typed in an invalid input. Please try again.")
        

    def update(self):
        self.xpos = pyxel.mouse_x
        self.ypos = pyxel.mouse_y

    def getMargin(self):
        return self.margin

    def getMagPos (self):
        magX = self.xpos+24+self.width/2
        magY = self.ypos+24+self.height/2
        return (magX, magY)

    def toggleDraw (self):
        if self.drawMag == False:
            self.drawMag = True
        else:
            self.drawMag = False


    def draw(self):
        #this is where we draw the tomb based on our mouse coordinates
        
        #this clip works by selecting the region from the first coordinates, aka our mouse position to where we say is the next coordiantes.
        if self.drawMag == True:

       #this is what draws the magnifying glass, but now we need to have different u and v values for each of the glasses we want to draw. as well as height and width....
            pyxel.blt(self.xpos, self.ypos, 2, self.u, self.v, self.width+48, self.height+48, 11)
            pyxel.clip(self.xpos+24,self.ypos+24, self.width, self.height)
        #the last value in this function, is which of the color pallete will be the transparent color.... in this case 0 means the first color in the pallete which is black...
        else:
            pyxel.clip(0,0,300, 300)
