import pyxel

class BG:
  name = ""
  width = 0
  height = 0
  xpos = 0 
  ypos = 0 
  u = 0 
  v = 0 
  tilemap = 0

  def __init__(self,level):
    print("Creation of the BackGround")

  def update(self):
    print("update of the background")

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

  def change_to_start_screen_scary(self):
        self.tilemap = 0
        self.u = 48
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



  def glitch_screen_animation(self):
      self.u = self.u+48
      if self.u > 192:
          self.u = 0

  def draw(self):
    pyxel.bltm(0,0,self.tilemap,self.u, self.v,100,100)
