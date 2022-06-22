from collectables import Collectables
from collectables import Collectable_Crab

class Item_List():
# J LVL
    j_gravestone = Collectables("J Gravstone", 239, 239, 0, 128, 50, sound=63)
    blood_bush = Collectables("Blood Bush", 0, 120, 0, 160, 50, sound=63)
    skull = Collectables("Skull", 144, 200, 0, 144, 50, sound=63)
    head = Collectables("Head", 104, 240, 16, 144, 50, sound=63)
    knife = Collectables("Knife", 96, 168, 32, 144, 50, sound=63)
    teddy_bear = Collectables("Teddy Bear", 24, 216, 0, 176, 50, sound=63)
# CRAB LVL
    cool_land_crab = Collectable_Crab(32, 208, 232, 240, "Cool Land Crab", 8, 8, 25)
    cool_water_crab = Collectable_Crab(32, 216, 8, 168, "Cool Water Crab", 8, 8, 25)
    cool_shell_crab = Collectable_Crab(48, 224, 184, 176, "Cool Shell Crab", 8, 16, 25)
    cool_fish = Collectables("Cool Fish", 40, 168, 0, 208, 25)
    message_in_bottle = Collectables("Message in Bottle", 40, 192, 40, 208, 25)
    nautillis_shell = Collectables("Nautillis Shell", 88, 152, 24, 224, 25)
# CAR MOUTAIN LVL
    snowboarder = Collectables("Snowboarder", 40, 88, 24, 168, 10, 8, 8)
    flag = Collectables("Flag", 176, 8, 16, 160, 8, 8, 16)
    bush_with_bunny = Collectables("Bunny Bush", 216, 96, 32, 192, 8)
    gear_shift_drive = Collectables("Drive Mode", 208, 240, 32, 176, 10, 8, 16)
    money_bag = Collectables("Shady Money Bag", 192, 48, 16, 178, 20, 16, 30)
    toyota_logo = Collectables("Toyota Logo", 72, 168, 56, 160, 15, 24, 24)
# NATURE LVL
    dead_gold_flower = Collectables("Dead Gold Flower", 160, 208, 168, 16, 5, 8, 8)
    parrot = Collectables("Parrot", 152, 16, 176, 32, 5)
    squirrel = Collectables("Squirrel", 216, 176, 136, 216, 3, 32, 40)
    bird = Collectables("Bird", 8, 104, 112, 16, 5)
    fire_ant = Collectables("Fire Ant", 168, 200, 160, 24, 5, 8, 8)
    rich_dude = Collectables("Rich Dude", 88, 136, 160, 32, 10, 16, 8)

    

    Jonathen_level_list = [j_gravestone, blood_bush, skull, head, knife, teddy_bear]
    Crab_level_list = [cool_land_crab, cool_water_crab, cool_shell_crab, cool_fish, message_in_bottle, nautillis_shell]
    car_mountain_level_list = [snowboarder, flag, bush_with_bunny, gear_shift_drive, money_bag, toyota_logo]
    beautiful_nature_level_list = [dead_gold_flower, parrot, squirrel, bird, fire_ant, rich_dude]