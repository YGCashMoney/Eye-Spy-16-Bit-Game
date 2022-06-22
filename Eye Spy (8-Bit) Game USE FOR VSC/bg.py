import pyxel
from enum import Enum

class levels (Enum):
  magglass = 0
  start_screen = 1
  level_select = 2
  start_scary = 3
  shop = 4
  crab_load = 5
  level_load = 6
  j_level = 7
  crab_level = 8
  car_level = 9
  good_nature = 10
  iceberg_level = 11
  glitch_1 = 12
  j_load = 13


class BG:
  name = ""
  width = 32
  height = 32
  xpos = 0 
  ypos = 0
  u = 0 
  v = 0 
  tilemap = 0

  dictionary = {
        levels.magglass: (0, 0, 48),
        levels.start_screen: (0, 0, 96),
        levels.level_select: (0, 48, 48),
        levels.start_scary: (0, 48, 96),
        levels.shop: (0, 0, 48),
        levels.crab_load: (0, 144, 48),
        levels.level_load: (0, 96, 48),
        levels.j_level: (0, 0, 0),
        levels.crab_level: (0, 48, 0),
        levels.car_level: (0, 96, 0),
        levels.good_nature: (0, 96, 96),
        levels.iceberg_level: (0, 192, 0),
        levels.glitch_1: (0, 0, 192),
        levels.j_load: (0, 192, 48)
  }

  def __init__(self,level):
    print("Creation of the BackGround")

  def update(self):
    print("update of the background")

  def change_screen(self, level):
      self.tilemap, self.u, self.v = BG.dictionary [level]

  def glitch_screen_animation(self):
      self.u = self.u+48
      if self.u > 192:
          self.u = 0

  def draw(self):
    pyxel.bltm(0,0,self.tilemap,self.u, self.v, 100, 100)

