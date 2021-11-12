# from pyxel.editor.app import App

# App("Eye_Spy")


import pyxel
import random
import time
from player import Player
from magglass import MagGlass
from bg import BG
from checkmark import Checkmark
from cursor import Cursor
from item_list import Item_List
from collectables import Collectables
from collectables import Collectable_Crab
from crabs import Crabs



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
    mytime = 0
    oldtime = 0
    #The maximum width and height of the screen is 255
    palette = [
        # 0xffa500
        # 0xFF0000
        0x000000, 0x1D2242, 0x7E2553, 0x2E3D28, 0xAB5236, 0xB8B4B0, 0xA9C1FF,
        0xFFFFFF, 0xA30000, 0xFFA300, 0xFFEC27, 0x466941, 0x29ADFF, 0x9C5C35,
        0xFF848C, 0x693F28
    ]  # 0 - 15

    glitch_initiation =  False

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


        # self.bg.change_to_glitch_screen_1()
        self.bg.change_to_start_screen()

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
                self.bg.change_to_start_screen_scary()
                self.update_funct = self.update_dict.get("start_screen")
                self.glitch_initiation = True
                pyxel.play(1, 19, loop=False)
                pyxel.play(2, 20, loop=False)

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
                if self.glitch_initiation == True:
                    self.bg.change_to_glitch_screen_1()
                    self.update_funct = self.glitch_screen_update
                    pyxel.playm(2, loop=True)
                    self.oldtime = time.clock_gettime_ns(time.CLOCK_REALTIME)
                    
                else:
                    pyxel.quit()
            if self.choose_button("start", 0, 114, 56, 32) and self.glitch_initiation == False:
                self.bg.change_to_level_select()
                self.update_funct = self.update_dict.get("change_level")
                pyxel.play(1, 17, loop=False)
                pyxel.play(2, 18, loop=False)
            elif self.glitch_initiation == True:
                pyxel.play(1, 0, loop=False)
 
                
    def glitch_screen_update(self):
        self.bg.glitch_screen_animation()
        if self.oldtime+10000000000 < time.clock_gettime_ns(time.CLOCK_REALTIME):
            pyxel.stop()
            self.bg.change_to_j_level_load()
            self.update_funct = self.update_dict.get("j_level_load")


        

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