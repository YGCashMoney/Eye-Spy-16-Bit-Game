# from pyxel.editor.app import App
# App("Eye_Spy")


import pyxel
import random
import time
from player import Player
from magglass import MagGlass
from bg import BG
from bg import levels
from checkmark import Checkmark
from cursor import Cursor
from item_list import Item_List
from collectables import Collectables
from collectables import Collectable_Crab
from crabs import Crabs
from button import button



class App:
    # width = 256
    # height = 256
    # frame_count = 0
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

    glitch_initiation = False

    #creates an app
    def __init__(self):
        self.width = 256
        self.height = 256
        self.frame_count = 0
        pyxel.init(
            self.width,
            self.height,
            caption="Eye Spy [16 - bit]",
            scale=3,
            palette=self.palette
        )  # Lets us create the window for the application i.e. the way we see the game...
        #the caption, is the name on the window.... i.e. what the game is called probably


        exit = button("exit", 0, 192, 56, 32, levels.start_screen, self.bg)
        start = button("start", 0, 114, 56, 32, levels.level_select, self.bg)
        return = button("return", 240, 0, 16, 16, levels.start_scary, self.bg)
        shop = ("shop", 0, 0, 32, 32, levels.shop, self.bg)
        crab_rave_level = ("crab_rave_level", 192, 232, 16, 16, levels.crab_level, self.bg)
        j_level = ("j_level", 232, 232, 16, 16, levels.j_level, self.bg)
        car_mountain_level = ("car_mountain_level", 184, 136, 16, 16, levels.car_level, self.bg)
        beautiful_nature_level = ("beautiful_nature_level", 24, 136, 16, 16, levels.good_nature, self.bg)
        iceberg_level = ("iceberg_level", 64, 136, 16, 16, levels.iceberg_level, self.bg)
        level_return = ("level_return", 0, 40, 40, 16, center, levels.level_select, self.bg)

        self.button_dict = {
            levels.magglass:[],
            levels.start_screen:[
                ("exit", 0, 192, 56, 32),
                ("start", 0, 114, 56, 32)],
            levels.level_select:[
                ("return", 240, 0, 16, 16),
                ("shop", 0, 0, 32, 32),
                ("crab_rave_level", 192, 232, 16, 16),
                ("j_level", 232, 232, 16, 16),
                ("car_mountain_level", 184, 136, 16, 16),
                ("beautiful_nature_level", 24, 136, 16, 16),
                ("iceberg_level", 64, 136, 16, 16)],
            levels.start_scary:[],
            levels.shop: [("return", 240, 0, 16, 16)],
            levels.crab_load:[],
            levels.level_load:[],
            levels.j_level:[],
            levels.crab_level:[("level_return", 0, 40, 40, 16, center)],
            levels.car_level:[("level_return", 0, 40, 40, 16, center)],
            levels.good_nature:[("level_return", 0, 40, 40, 16, center)],
            levels.iceberg_level:[("level_return", 0, 40, 40, 16, center)],
            levels.glitch_1:[],
            levels.j_load:[],
        }

        self.update_dict = {
            "j_level": self.j_level_update,
            "j_level_load": self.j_level_load_update,
            "crab_rave": self.crab_rave_update,
            "crab_rave_load": self.crab_rave_load_update,
            "change_level": self.change_level_update, 
            "start_screen": self.start_screen_update,
            "car_mountain_level": self.car_mountain_level_update,
            "car_mountain_level_load": self.car_mountain_level_load_update,
            "beautiful_nature_level": self.beautiful_nature_level_update,
            "beautiful_nature_level_load": self.beautiful_nature_level_load_update,
            "iceberg_level": self.iceberg_level_update,
            "iceberg_level_load": self.iceberg_level_load_update,
            "shop_update": self.shop_update,
        }

        self.player = Player()

        #We have to import the assests we want to use in our game, or level per say...
        #in this case its the following
        pyxel.load("Eye_Spy.pyxres")
        self.magglass.toggleDraw()
        self.update_funct = self.update_dict.get("start_screen")

        # Start Screen
        self.bg.change_screen (levels.start_screen)

        self.cursor.toggleDraw()

        pyxel.run(self.update, self.draw)

    #makes buttons functioning
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

    def update_buttons(self, level):
        for button in self.button_dict[level]:
            if self.choose_button(button):
                pass


    #shop
    def shop_update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if self.choose_button("return", 240, 0, 16, 16):
                # Level Select
                self.bg.change_screen(levels.level_select)
                pyxel.play(1, 19, loop=False)
                pyxel.play(2, 20, loop=False)
                self.update_funct = self.update_dict.get("change_level")
        
    #level screen (and all the buttons to shop and levels)
    # def button_press(self):shop_update
        # if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
        #     for button in level_buttons[screen]
    def change_level_update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if self.choose_button("exit", 240, 0, 16, 16):
                # Start Scary
                self.bg.change_screen(levels.start_scary)
                self.update_funct = self.update_dict.get("start_screen")
                self.glitch_initiation = True
                pyxel.play(1, 19, loop=False)
                pyxel.play(2, 20, loop=False)

            elif self.choose_button("shop", 0, 0, 32, 32):
                self.update_funct = self.update_dict.get("shop_update")
                # Shop
                self.bg.change_screen(levels.shop)
                pyxel.play(1, 17, loop=False)
                pyxel.play(2, 18, loop=False)

            elif self.choose_button("crab_rave_level", 192, 232, 16, 16):
                #Crab Level
                self.bg.change_screen(levels.crab_load)
                self.update_funct = self.update_dict.get("crab_rave_load")

            elif self.choose_button("j_level", 232, 232, 16, 16):
                # self.bg.change_to_j_level_load()
                self.bg.change_screen(levels.j_load)
                self.update_funct = self.update_dict.get("j_level_load")

            elif self.choose_button("car_mountain_level", 184, 136, 16, 16):
                # Level Load
                self.bg.change_screen(levels.level_load)
                self.update_funct = self.update_dict.get("car_mountain_level_load")

            elif self.choose_button("beautiful_nature_level", 24, 136, 16, 16):
                # self.bg.change_to_level_load()
                self.bg.change_screen(levels.level_load)
                self.update_funct = self.update_dict.get("beautiful_nature_level_load")

            elif self.choose_button("iceberg_level", 64, 136, 16, 16):
                # self.bg.change_to_iceberg_level()
                self.bg.change_screen(levels.level_load)
                self.update_funct = self.update_dict.get("iceberg_level_load")

    #functions the load screen of j level
    def j_level_load_update(self):
        self.magglass.changeGlass("corrupted")
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.cursor.toggleDraw()
            self.magglass.toggleDraw()
            # J Level
            self.bg.change_screen(levels.j_level)
            self.items = Item_List.Jonathen_level_list
            self.update_funct = self.update_dict.get("j_level")
            pyxel.playm(1, loop=True)

    #j level
    def j_level_update(self):
        self.magglass.update()
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            for item in self.items:
                center = self.magglass.getCenter()
                if item.update(center[0], center[1], self.magglass.margin):
                    self.player.point+=item.value
                    self.player.found_items.append(item)

    # crab load
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
            #Crab Level
            self.bg.change_screen(levels.crab_level)
            self.cursor.toggleDraw()
            self.magglass.toggleDraw()
            self.update_funct = self.update_dict.get("crab_rave")

    # crab level
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
            if self.choose_button("level_return", 0, 40, 40, 16, center):
                pyxel.stop()
                self.crabs = []
                self.items = []
                self.update_funct = self.update_dict.get("change_level")
                # self.bg.change_to_level_select()
                self.bg.change_screen(levels.level_select)
                self.magglass.toggleDraw()
                self.cursor.toggleDraw()

    #car mountain level            
    def car_mountain_level_update(self):
        self.magglass.update()
        center = self.magglass.getCenter()
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            for item in self.items:
                if item.update(center[0], center[1], self.magglass.margin):
                    self.items.remove(item)
            if self.choose_button("level_return", 0, 40, 40, 16, center):
                pyxel.stop()
                self.crabs = []
                self.items = []
                self.update_funct = self.update_dict.get("change_level")
                # self.bg.change_to_level_select()
                self.bg.change_screen(levels.level_select)
                self.magglass.toggleDraw()
                self.cursor.toggleDraw()
    # car load
    def car_mountain_level_load_update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.cursor.toggleDraw()
            self.magglass.toggleDraw()
            # Car Level
            self.bg.change_screen(levels.car_level)
            self.items = Item_List.car_mountain_level_list
            self.update_funct = self.update_dict.get("car_mountain_level")
            pyxel.playm(5, loop=True)
    # nature lvl
    def beautiful_nature_level_update(self):
        self.magglass.update()
        center = self.magglass.getCenter()
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            for item in self.items:
                if item.update(center[0], center[1], self.magglass.margin):
                    self.items.remove(item)
            if self.choose_button("level_return", 0, 40, 40, 16, center):
                pyxel.stop()
                self.crabs = []
                self.items = []
                self.update_funct = self.update_dict.get("change_level")
                # self.bg.change_to_level_select()
                self.bg.change_screen(levels.level_select)
                self.magglass.toggleDraw()
                self.cursor.toggleDraw()

    # nature load
    def beautiful_nature_level_load_update(self):

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.cursor.toggleDraw()
            self.magglass.toggleDraw()
            # Good Nature Level
            self.bg.change_screen(levels.good_nature)
            self.items = Item_List.beautiful_nature_level_list
            self.update_funct = self.update_dict.get("beautiful_nature_level")
            pyxel.playm(5, loop=True)

    # iceberg lvl
    def iceberg_level_update(self):
        self.magglass.update()
        center = self.magglass.getCenter()
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            for item in self.items:
                if item.update(center[0], center[1], self.magglass.margin):
                    self.items.remove(item)
            if self.choose_button("level_return", 0, 40, 40, 16, center):
                pyxel.stop()
                self.crabs = []
                self.items = []
                self.update_funct = self.update_dict.get("change_level")
                # self.bg.change_to_level_select()
                self.bg.change_screen(levels.level_select)
                self.magglass.toggleDraw()
                self.cursor.toggleDraw()

    # iceberg load
    def iceberg_level_load_update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.cursor.toggleDraw()
            self.magglass.toggleDraw()
            # Iceberg Level
            self.bg.change_screen(levels.iceberg_level)
            self.items = Item_List.beautiful_nature_level_list
            self.update_funct = self.update_dict.get("iceberg_level")
            pyxel.playm(5, loop=True)

    # start + glitch initiation to j lvl
    def start_screen_update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if self.choose_button("exit", 0, 192, 56, 32):
                if self.glitch_initiation == True:
                    # Glitch Screen 1
                    self.bg.change_screen(levels.glitch_1)
                    self.update_funct = self.glitch_screen_update
                    pyxel.playm(2, loop=True)
                    self.oldtime = time.clock_gettime_ns(time.CLOCK_REALTIME)
                    
                else:
                    pyxel.quit()
            if self.choose_button("start", 0, 114, 56, 32) and self.glitch_initiation == False:
                # self.bg.change_to_level_select()
                self.bg.change_screen(levels.level_select)
                self.update_funct = self.update_dict.get("change_level")
                pyxel.play(1, 17, loop=False)
                pyxel.play(2, 18, loop=False)
            elif self.glitch_initiation == True:
                pyxel.play(1, 0, loop=False)
 
    # glitch animation for j lvl  
    def glitch_screen_update(self):
        self.bg.glitch_screen_animation()
        if self.oldtime+10000000000 < time.clock_gettime_ns(time.CLOCK_REALTIME):
            pyxel.stop()
            # J Load
            self.bg.change_screen(levels.j_load)
            self.update_funct = self.update_dict.get("j_level_load")


        
    # updates everything
    def update(self):
        if self.frame_count <= 256:
            self.frame_count += 1

    
        self.update_funct()

        pyxel.MOUSE_LEFT_BUTTON

        self.cursor.update()
        
        if pyxel.btnp(pyxel.KEY_C):
          self.magglass.toggleDraw()
          # Mag Screen
          self.bg.change_screen(levels.magglass)
          self.cursor.toggleDraw()
          for item in self.items:
              item.toggleDraw()
          for crab in self.crabs:
              crab.toggleDraw()
          pyxel.stop()
          #newGlass = input("Would you like to change the size of your magnifying glass? If so, type in the size!")
          #self.magglass.changeGlass(newGlass)

    # draws everything (so its not all just a black screen)
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
            item.draw(self.update_funct,self.update_dict)
        self.magglass.draw()
        self.cursor.draw()
        #pyxel.bltm(0, 0, 0, 0, 0, 255, 255) #this takes the text element from the first slot in the image bank, and places it at the location defined in the first two slots of the blt function....
        if self.frame_count <= 256:
            pyxel.text(0, 41, "Testing for Text",
                       13)  #0x4f4f4f) color must be depending on the pallete.
              


App()