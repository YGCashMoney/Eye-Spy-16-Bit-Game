# from pyxel.editor.app import App

# App("Eye_Spy")


import pyxel
import random
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
        
       #>:D-<

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

  def __init__(self, name, xpos, ypos, u, v, value, width = None, height = None):
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
  def update(self, magX, magY, margin):
    if self.body[0] >= magX - margin and self.body[0] <= magX + margin:
        if self.body[1] >= magY - margin and self.body[1] <= magY + margin:
            self.u = 0
            self.v = 240
            print ("Congrats! You found " + self.name + "!!!")
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

class Item_List():
    j_gravestone = Collectables("J Gravstone", 239, 239, 0, 128, 50)
    blood_bush = Collectables("Blood Bush", 0, 120, 0, 160, 50)
    skull = Collectables("Skull", 144, 200, 0, 144, 50)
    head = Collectables("Head", 104, 240, 16, 144, 50)
    knife = Collectables("Knife", 96, 168, 32, 144, 50)
    teddy_bear = Collectables("Teddy Bear", 24, 216, 0, 176, 50)
    cool_land_crab = Collectable_Crab(32, 208, 232, 240, "Cool Land Crab", 8, 8, 25)
    cool_water_crab = Collectable_Crab(32, 216, 8, 168, "Cool Water Crab", 8, 8, 25)
    cool_shell_crab = Collectable_Crab(48, 224, 184, 176, "Cool Shell Crab", 8, 16, 25)
    cool_fish = Collectables("Cool Fish", 40, 168, 0, 208, 25)
    message_in_bottle = Collectables("Message in Bottle", 40, 192, 40, 208, 25)
    nautillis_shell = Collectables("Nautillis Shell", 88, 152, 24, 224, 25)
    snowboarder = Collectables("Snowboarder", 40, 88, 24, 168, 10, 8, 8)
    flag = Collectables("Flag", 176, 8, 16, 160, 10, 8, 16)
    bush_with_bunny = Collectables("Bunny Bush", 216, 96, 32, 192, 10)
    gear_shift_drive = Collectables("Drive Mode", 208, 240, 32, 176, 10, 8, 16)
    money_bag = Collectables("Shady Money Bag", 192, 48, 16, 178, 15, 16, 30)
    toyota_logo = Collectables("Toyota Logo", 72, 168, 56, 160, 15, 24, 24)

    

    Jonathen_level_list = [j_gravestone, blood_bush, skull, head, knife, teddy_bear]
    Crab_level_list = [cool_land_crab, cool_water_crab, cool_shell_crab, cool_fish, message_in_bottle, nautillis_shell]
    car_mountain_level_list = [snowboarder, flag, bush_with_bunny, gear_shift_drive, money_bag, toyota_logo]

        

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



class Checkmark():
    name = "" #j_level_checkmark, checkmard, crab_level_checkmark
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



class BG:
  name = ""
  width = 0
  height = 0
  xpos = 0 
  ypos = 0 
  u = 0 
  v = 0 
  tilemap = 0
#   def Change_Glass (self):
#       tm = 2

  def __init__(self,level):
    print("Creation of the BackGround")

  def update(self):
    print("update of the background")
    #probably not needed but could be used

  def change_mag_screen(self):
      self.tilemap = 0
      self.u = 0
      self.v = 48
      self.width = 32
      self.height = 32

  def change_to_crab_rave(self):
        self.tilemap = 0
        self.u = 48
        self.v = 0
        self.width = 32
        self.height = 32

  def change_to_crab_rave_load(self):
        self.tilemap = 0
        self.u = 144
        self.v = 48
        self.width = 32
        self.height = 32

  def change_to_j_level(self):
        self.tilemap = 0
        self.u = 0
        self.v = 0
        self.width = 32
        self.height = 32
    
  def change_to_j_level_load(self):
        self.tilemap = 0
        self.u = 192
        self.v = 48
        self.width = 32
        self.height = 32

  def change_to_level_select(self):
        self.tilemap = 0
        self.u = 48
        self.v = 48
        self.width = 32
        self.height = 32

  def change_to_start_screen(self):
        self.tilemap = 0
        self.u = 0
        self.v = 96
        self.width = 32
        self.height = 32

  def change_to_car_mountain_level(self):
      self.tilemap = 0
      self.u = 96
      self.v = 0
      self.width = 32
      self.height = 32

  def change_to_level_load(self):
      self.tilemap = 0
      self.u = 96
      self.v = 48
      self.width = 32
      self.hight  = 32

  def change_to_glitch_screen_1(self):
        self.tilemap = 0
        self.u = 0
        self.v = 192
        self.width = 32
        self.height = 32

  def draw(self):
    pyxel.bltm(0,0,self.tilemap,self.u, self.v,100,100)



  


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

#CHANGE THIS LATER (SPECIFICALLY THE U AND V COORDINATES)
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


# myglass = MagGlass() --> MagGlass.init()

class Player:
    point = 0
    completed_levels = []
    locked_level = []
    found_items = []



class App:
    width = 256
    height = 256
    frame_count = 0
    bg = BG(1)
    player = None
    magglass = MagGlass("large")
    items = []
    cursor = Cursor()
    update_dict = {}
    crabs = []
    update_funct = None
    #The maximum width and height of the screen is 255
    palette = [
        # 0xffa500
        # 0xFF0000
        0x000000, 0x1D2242, 0x7E2553, 0x2E3D28, 0xAB5236, 0xB8B4B0, 0xA9C1FF,
        0xFFFFFF, 0xA30000, 0xFFA300, 0xFFEC27, 0x466941, 0x29ADFF, 0x9C5C35,
        0xFF848C, 0x693F28
    ]  # 0 - 15

    def __init__(self):
        pyxel.init(
            self.width,
            self.height,
            caption="Eye Spy [16 - bit]",
            scale=3,
            palette=self.palette
        )  # Lets us create the window for the application i.e. the way we see the game...
        #the caption, is the name on the window.... i.e. what the game is called probably

        self.update_dict = {
            "j_level": self.j_level_update,
            "j_level_load": self.j_level_load_update,
            "crab_rave": self.crab_rave_update,
            "crab_rave_load": self.crab_rave_load_update,
            "change_level": self.change_level_update, 
            "start_screen": self.start_screen_update,
            "car_mountain_level": self.car_mountain_level_update,
            "car_mountain_level_load": self.car_mountain_level_load_update,
        }

        self.player = Player()

        #We have to import the assests we want to use in our game, or level per say...
        #in this case its the following
        pyxel.load("Eye_Spy.pyxres")
        self.magglass.toggleDraw()

       

        #init(width, height, [caption],
        #[scale] --> the magnification of the screen MUST BE WHOLE NUMBER, [palette], [fps], [quit_key], [fullscreen])

        #add image to the bank of images...
        # pyxel.image(0).load(0, 0, "Eye_Spy.pyxel")
        self.update_funct = self.update_dict.get("start_screen")


        self.bg.change_to_glitch_screen_1()

        self.cursor.toggleDraw()

        pyxel.run(self.update, self.draw)


    def choose_button(self, name, x, y, width, height, center = None):

    # if self.body[0] >= magX - margin and self.body[0] <= magX + margin:
    #     if self.body[1] >= magY - margin and self.body[1] <= magY + margin:
        if center == None:
            if self.cursor.xpos >= x and self.cursor.xpos <= x + width:
                if self.cursor.ypos >= y and self.cursor.ypos <= y + height:
                    return True
            return False
        else:
            print (center)

            if center[0] >= x and center[0] <= x + width:
                if center[1] >= y and center[1] <= y + height:
                    return True
            return False
        
    def change_level_update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if self.choose_button("exit", 240, 0, 16, 16):
                self.bg.change_to_start_screen()
                self.update_funct = self.update_dict.get("start_screen")

            if self.choose_button("crab_rave_level", 192, 232, 16, 16):
                self.bg.change_to_crab_rave_load()
                self.update_funct = self.update_dict.get("crab_rave_load")

            if self.choose_button("j_level", 232, 232, 16, 16):
                self.bg.change_to_j_level_load()
                self.update_funct = self.update_dict.get("j_level_load")

            if self.choose_button("car_mountain_level", 184, 136, 16, 16):
                self.bg.change_to_level_load()
                self.update_funct = self.update_dict.get("car_mountain_level_load")

    def j_level_load_update(self):
        self.magglass.changeGlass("corrupted")
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.cursor.toggleDraw()
            self.magglass.toggleDraw()
            self.bg.change_to_j_level()
            self.items = Item_List.Jonathen_level_list
            self.update_funct = self.update_dict.get("j_level")
            pyxel.playm(1, loop=True)

        

    def j_level_update(self):
        self.magglass.update()
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            for item in self.items:
                center = self.magglass.getCenter()
                if item.update(center[0], center[1], self.magglass.margin):
                    self.player.point+=item.value
                    self.player.found_items.append(item)
                    print (self.player.point)


    def crab_rave_load_update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            row = 0
            # sand crabs:
            for i in range(88):
                col = i%22
                self.crabs.append(
                        Crabs(96,128,(9+col)*8, (28+row)*8, 8, 8))
                if col==21:
                    row+=1

            # water crabs:
            crab_count = 0
            water_crab_pos = []
            while crab_count <= 60:
                row = random.randint(16, 29)*8
                col = random.randint(0, 8)*8
                for item in Item_List.Crab_level_list:
                    if item.xpos == row and item.ypos == col:
                        continue
                if (row, col) in water_crab_pos:
                    continue
                crab_count += 1
                self.crabs.append(
                        Crabs(96,136,col, row, 8, 8))
                water_crab_pos.append((row, col))

            pyxel.playm(0, loop=True)

            self.bg.change_to_crab_rave()
            self.cursor.toggleDraw()
            self.magglass.toggleDraw()
            self.update_funct = self.update_dict.get("crab_rave")


    def crab_rave_update(self):
        self.items = Item_List.Crab_level_list

            
        for crab in self.crabs:
            crab.update()
        for item in self.items:
            if type(item) == Collectable_Crab:
                item.update(None, None, None)
        
        self.magglass.update()
        center = self.magglass.getCenter()
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            for item in self.items:
                if item.update(center[0], center[1], self.magglass.margin):
                    self.items.remove(item)
            if self.choose_button("level_return", 0, 240, 40, 16, center):
                pyxel.stop()
                self.crabs = []
                self.items = []
                self.update_funct = self.update_dict.get("change_level")
                self.bg.change_to_level_select()
                self.magglass.toggleDraw()
                self.cursor.toggleDraw()
                
    def car_mountain_level_update(self):
        self.bg.change_to_car_mountain_level()
        self.items = Item_List.car_mountain_level_list
        self.magglass.update()

    def car_mountain_level_load_update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.cursor.toggleDraw()
            self.magglass.toggleDraw()
            self.bg.change_to_car_mountain_level()
            self.items = Item_List.car_mountain_level_list
            self.update_funct = self.update_dict.get("car_mountain_level")




    def start_screen_update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if self.choose_button("exit", 0, 192, 56, 32):
                pyxel.quit()
            if self.choose_button("start", 0, 114, 56, 32):
                self.bg.change_to_level_select()
                self.update_funct = self.update_dict.get("change_level")


        

    def update(self):
        if self.frame_count <= 256:
            self.frame_count += 1

        self.update_funct()

        pyxel.MOUSE_LEFT_BUTTON

        self.cursor.update()
        
        if pyxel.btnp(pyxel.KEY_C):
          self.magglass.toggleDraw()
          self.bg.change_mag_screen()
          self.cursor.toggleDraw()
          for item in self.items:
              item.toggleDraw()
          for crab in self.crabs:
              crab.toggleDraw()
          pyxel.stop()
          #newGlass = input("Would you like to change the size of your magnifying glass? If so, type in the size!")
          #self.magglass.changeGlass(newGlass)


    def draw(self):
        #what is drawn last is in the last layer..........
        pyxel.cls(0)
        #pyxel.blt(0,0,2,0,0,255,255)
        
        self.bg.draw()
        #pyxel.blt(100,100,0,48,64,16,16)
        #Theres an image bank, that contains all the assets of the 8 bit mappings, so if you want to put one of them in the game, you have to copy it from the bank, and then place in the screen.

        if len(self.crabs) != 0:
            for crab in self.crabs:
                crab.draw()

        for item in self.items:
            item.draw()
        self.magglass.draw()
        self.cursor.draw()
        #pyxel.bltm(0, 0, 0, 0, 0, 255, 255) #this takes the text element from the first slot in the image bank, and places it at the location defined in the first two slots of the blt function....
        if self.frame_count <= 256:
            pyxel.text(0, 41, "            Jonthan",
                       13)  #0x4f4f4f) color must be depending on the pallete.
        
        


App()
