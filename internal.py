from math import exp
from os import name, read, replace, getcwd
import time
from tkinter import *
import tkinter
from turtle import *
from typing import Counter
import random
import random as biomeSeed # For features like biome
import random as featureSeed # For Features like ore
import json
import re
try:import jsoncomment as jsoncomment  
except:pass

import re
from sys import path
path.insert(0,f"{getcwd()}\pyModules")
import spark as spark
from graphics import *
import executer
# Resource Pack
resources = "assets"

# Colin is to pull rgb from file
colin = "haha loser u fked up"

caveair = "cyan2"
caveblock = "stone"
caveopen = "CHANGEME"

# Height
blocksBelow0 = 64

# Button Listeners
active = 1
VolLisU = 0
VolLisD = 0
# Counting
Counter1 = 0
# Menu Tags
Tag1 = 0 # This is for startup Tests

# Visualiser Info

# Current Size.
# (!) Remembering that the more needed to draw, the more power needed.
# Current Notes:
#  The Visualiser should be similar to blockter
#  hhhhhhhh- work on biome change in 0.0.5. this will bring a new ver value
#  oh.. and.. NAMESPACE EVERYTHING!!!! Do it like a minecraft data pack
#   0.0.6 = General Idea for this is to focus on biomes only after i fix generation
#   0.0.9 = Finishing up the conversion to the graphics.py system.
#     The main reason for this was- We're able to make the generator about 90% times faster.
#     This allows a better- block based system to be implemented. I recon about-
#     18 Blocks per XPOS value can be generated at the same speed.
#     Furthermore we're gonna do a 3Dish Biomes System in 0.0.10
#   0.0.11 = Alright. We're gonna move the generator into a system similar to minecrafts data packs
#     but these data packs will sorta- these will define how the system runs
#     We're gonna move- ALL or the biome alternation out of placeblock (new) and
#     Have it all in separate functions
#   0.1.0 = The goal of this is to separate the generator into multiple systems
#     These systems are how it's drawn:
#       We're gonna have Turtle and Graphics.py
#   0.1.1 = Alright- Datafile will have some extra biomes- but first we wanna make a sorta- underground. Not caves... yet..
#     We're also gonna experiment with features! These will be in the caves! ANNNDDD- SPLITTING THE FILES!!... no wait nevermind
#   0.1.2 = hhh- one window for all systems
#   0.1.3 = Well we're finally gonna do what we were supposed to do in 0.1.1. We're going to add support for a different surface builder system (plateau)
#     which allows different blocks for every Y co-ord ^^, thus i'm also going to FINALLY add a mesa biome. BTW- Plateaus and different surface builders aren't fully supported under SPARK
#   0.1.5 = Alright! I want the Generator- FULLY configurable by a json file. I want it to be- I'm able to no longer have to open vs code to
#     Edit things like Blockmap and stuff like that!
#   0.1.6 = Window Improvements
#   0.1.7 = Better Generation. The Goal is to generate in stages
#   0.1.8 = Have all biome choosing done in one file. Have final 15 blocks of a biome follow next biomes height stats- thus also meaning- generator must know what biome is next
#     I DID IT- I ACTUALY FUCKING DID IT! BADLANDS PLATEAU CAN BE ONE BIOME- NO SECOND ONE FOR DOWNSCALE!! POSSIBILITIES ARE ENDLESS! 1 River Biome!
#   0.1.8.1 = This won't have a seperate file but- Just some extra work- done in class. We're gonna try and make caves a bit better. Currenty it overides bottom land layer.
#     On top of that- Badlands custom cave isn't there. We're gonna start having cave features off though.
#     I've decided- Since I won't be publishing this- I wanna start to copy minecraft for features.
#     The reason I wanna do this is because- I wanna convert features from popular minecrat data packs- and see them in blockter- but i don't wanna have to do much work.-
#         Nevermind.. -_-... Too much work.......
#   0.1.9 = I want trees added. oh- and water.
#      Straight up ripping off Minecraft LMAO
#     I also do comments in functions now... neatening it up a bit
#   0.2.0 = Redo Most of the feature systems
#     2:01pm: Biome VersionFile 8 is out! Biome File completely redone- Now to redo Blocks
#     4:41pm: OKAY IT SERIOUSLY TOOK THIS FUCKING LONG BUT- Blocks can have extra detail now :P Scaling is being a bit weird
#       though- I need to do some further work on that. Under Surface is now multiple blocks as well. Next goal is adding a debug mode- and fixing scaling issues (testing through debug)
#     --- 21/9/21 ---
#     5:19pm: YEAH- FUCK U ALL AHAHAHAHAH I GOT TRANSPARENCY WORKING IN BLOCKS :P
#   0.2.1
#       Well i made an oppsie. I did a new 0.2.0. That is now 0.1.10. This is to add what 0.10.0 adds.
#       - Customisable Transfer Values
#       - Spruce Trees
#       - Meadow Biome
#   0.2.2
#       UwU
#  0.0.1
#   Now it's a minecraft visualiser. well. We're gonna try and make it that
#  0.0.2
#   Switching to an image system with *hopefully* resource pack support!!
#  0.0.2.2
#   Block Generation Fixes
#  0.0.3
#   Dimension & Biome Changing
# 
#   11-11-21 | 1:50pm (ok- so- dimension files finally work!!!! I'm SO FUCKING COOL! !!! ! !! ! ! )
#
#     Ended up doing a lot more-  16-11-21 | 1:08pm (Ores!)
#  0.0.4
#   Feature targets!! (Only place if block on is the one we want)
#  0.0.5
#   ~~Data Pack Builder is gonna be worked on~~
#
#   Nevermind. Goal is to add other height features such as trapezoid- to hopefully get ores working 100% well
#
#     ok.. coming back to pack builder goal ngl
#  0.0.6
#   Get ready for release!

# Setup the world registry.

worldList = []
blankFormat = []

blankBlock = "minecraft:air"

worldStart = -4
worldHeight = 260

worldTick = 0
while not worldTick == worldHeight:
  blankFormat.append(blankBlock)
  worldTick += 1



worldList.append(blankFormat)


# MineVisualiser Project
# 0.0.1    - 5-11-21 | 3:55pm until 6:00pm
#          - 8-11-21 | 9:00am until 12:00pm
#          - 8-11-21 | 1:30pm until 2:22pm
# 0.0.2    - 8-11-21 | 2:22pm until 3:00pm
# 0.0.2.1  - 8-11-21 | 3:15pm until 6:01pm
# 0.0.2.2  - 8-11-21 | 7:23pm until 8:00pm
#          - 9-11-21 | 10:30am until 11:20am
#          - 9-11-21 | 3:20pm until 4:10pm
#          - 9-11-21 | 8:42pm until 9:58pm
# 0.0.2.3  - 9-11-21 | 9:58pm until 12:05am
#          - 10-11-21| 10:29am until 1:05pm
# 0.0.3    - 10-11-21| 1:05pm until 1:13pm
#          - 11-11-21| 9:51am until 11:20am
#          - 11-11-21| 1:02pm until 1:13pm
#          - 11-11-21| 1:33pm until 2:55pm
#          - 12-11-21| 7:17am until 8:00am
#          - 12-11-21| 2:06pm until 3:00pm
#          - 16-11-21| 9:24am until 1:09pm
# 0.0.4    - 16-11-21| 1:09pm until 1:29pm
#          - 17-11-21| 12:05pm until 1:45pm
# 0.0.5    - 18-11-21| 9:15am until 10:10am
#          - 18-11-21| 1:47pm until 3:00pm
# 0.0.6    - 18-11-21| 6:17pm until 7:30pm
#          - 23-11-21| 11:54am until 12:46pm
# 0.0.7    - 23-11-21| 12:50pm until 1:23pm


biomefeatures = [
  "vroom"
]


#
#
#   mineVis by Nova (Starcake)
#
#


# Biome Open
namespace = "open"
genopen = "minecraft:plains" # Biome
feature = "default" # Feature


currentcave = "default"


# Visualiser Tracking
height = int(65) # Y Position (x BlockMap)
height1 = int(65) # Y Position (x BlockMap) 1 Layer Behind
height2 = int(65) # Y Position (x BlockMap) 2 Layers Behind

# Keeping the 3 Layers Together:
magnetism = 60

# Visualiser Depth
scaling = 1 # How Big of steps can the generator take
smoothness = 40 # Percentage of scaling attempts can be ignored.

ocean = True # Ocean
sealevel = 62 # Sea Level
oceancol = "steelblue1"
surface = "minecraft:default"

forcetop = -75 # Top Limit
naturaltopy = -70 # Natural Generation Limit
naturalbottomy = -60 # Natural Generation Limit
forcebottom = -55 # Bottom Limit

# Generation System Information Settings
GenVer = "Enver" # This is to decide which system it uses.
# Old : 0.0.9 & Below
# Enver : Introduced in 0.0.10. This uses a 3D ish system and 3 layers of generation

# Biome Transfer
BiomePower = 25 # Biome Length Essentially
biomefallout = 20 # This is the lower end of BiomePower now | FORMER: Biome Length Mutable

try:
 with open("{}//config.json".format(namespace), "r") as FeOvAWTGb:
  ini = json.load(FeOvAWTGb)
  with open("{}//{}".format(namespace, ini["Start_File"]), "r") as AFeOvAWTGb:
    ini = json.load(AFeOvAWTGb)
    blockmap = ini["generator:size"]
    xpos = ini["starting:xpos"]
    drawingsystem = ini["generator:system"]
    settingCavesenabled = ini["setting:caves_enabled"]
    settingUnderSurface = ini["setting:undersurface_enabled"]
    settingSurfaceEnabled = ini["setting:surface_enabled"]
    settingFeaturesInCaves = ini["setting:features_in_caves"]
    settingSeaLevelWater = ini["setting:sealevelwater"]
    settingFeaturesOnSurface = ini["setting:features_on_surface"]
    settingSkyEnabled = ini["setting:sky_enabled"]
    settingSkyColor = ini["setting:sky_color_all"]
    settingSurfaceLevel = ini["height:surface_level"]
    pass
  pass
except:
 with open("datafile//config.json".format(namespace), "r") as FeOvAWTGb:
  ini = json.load(FeOvAWTGb)
  with open("datafile//{}".format(ini["Start_File"]), "r") as AFeOvAWTGb:
    ini = json.load(AFeOvAWTGb)
    blockmap = ini["generator:size"]
    xpos = ini["starting:xpos"]
    drawingsystem = ini["generator:system"]
    settingCavesenabled = ini["setting:caves_enabled"]
    settingUnderSurface = ini["setting:undersurface_enabled"]
    settingSurfaceEnabled = ini["setting:surface_enabled"]
    settingFeaturesInCaves = ini["setting:features_in_caves"]
    settingSeaLevelWater = ini["setting:sealevelwater"]
    settingFeaturesOnSurface = ini["setting:features_on_surface"]
    settingSkyEnabled = ini["setting:sky_enabled"]
    settingSkyColor = ini["setting:sky_color_all"]
    settingSurfaceLevel = ini["height:surface_level"]
    pass
  pass



seed = random.randint(0, 10)


biomeSeed.seed(seed)
featureSeed.seed(seed)
random.seed(seed)


choosertag = "plains_default"

# Biome Details
br = 255 # Biome Red
bg = 50 # Biome Green
bb = 0 # Biome Blue
blocksel = "grass" # What Block should be
blockimg = "grass" # What The Block Image Should Be
skycol = "SkyBlue2"


blockSystem = 0 # (
  # 0= 2 Colors. Outline and Fill
  # 1= multiple colors in a pixel format- 1x being 1 color/pixel 2x being 4 colors/pixels



# Screen Size
screenx = 1880
screeny = 720# 720

depthMapping = 1
scaleMapping = 0.2

# Seeds!!! :D 🎉🎉🎉🥂🥳🎉🎉🎉
# random.seed(200)

# Decide first biome
"""FirstBiome = random.randint(0, 1)
if FirstBiome == 0:
  genopen = "mesa_plateau"
if FirstBiome == 1:
  genopen = "plains"
if FirstBiome == 2:
  genopen = "river"
if FirstBiome == 3:
  genopen = "plains"
if FirstBiome == 4:
  genopen = "desert"
if FirstBiome == 5:
  genopen = "ocean"""

visualDebug = 0
# 0 = None
# 1 = Drawing Lines for Features and Biomes

namespace = "minecraft"
crawler = "open" # Data Pack

# NEW SYSTEM FOR DRAWING
print("Setup for New System")
display = 0

f = open("default//data//{}//worldgen//biome//{}.json".format((genopen.split(":"))[0], (genopen.split(":"))[1]), "r")
featuref = open("default//data//{}//worldgen//configured_feature//{}.json".format(namespace,"nothing"), "r")
cavef = open("datafile//cavesystem//{}.json".format("default"), "r")
#o = open("{}//blocks//{}.json".format(namespace,genopen), "r")
data = json.load(f)
featuredata = json.load(featuref)
cavedata = json.load(cavef)

foliageInfo = []

def makeLeaves(
  foliage_placer,
  probeher,
  publiclogheight,
  ycoord,
  xcoord,
  leaf,
  finaltrunker
):
  global foliageInfo
  if foliage_placer == "minecraft:spruce_foliage_placer":
    bheight = probeher["radius"]["spread"] # 3
    bradius = probeher["radius"]["base"] # 2
    boffset = probeher["offset"]["base"] # 0
    tick1 = round(publiclogheight/2)
    tick2 = round(publiclogheight)
    stretch = (bradius*2)+1 #The Width of leaves
    while stretch > 0:
      stretch = stretch-1
      EnverPlace((xcoord+(bradius))-stretch, ycoord+tick1, leaf, 1, 1)
    stretch = ((round(bradius-1))*2)+1 #The Width of leaves
    while stretch > 0:
      stretch = stretch-1
      EnverPlace((xcoord+(bradius-1))-stretch, ycoord+tick1+1, leaf, 1, 1)
    stretch = (bradius*2)+1 #The Width of leaves
    while stretch > 0:
      stretch = stretch-1
      EnverPlace((xcoord+(bradius))-stretch, ycoord+tick2, leaf, 1, 1)
    stretch = ((round(bradius-1))*2)+1 #The Width of leaves
    while stretch > 0:
      stretch = stretch-1
      EnverPlace((xcoord+(bradius-1))-stretch, ycoord+tick2+1, leaf, 1, 1)
  if foliage_placer == "minecraft:blob_foliage_placer":
    bheight = probeher["height"] # 3
    bradius = probeher["radius"] # 2
    boffset = probeher["offset"] # 0
    msearch = 0 # To Draw Trunk
    mtik = bheight + 2
    msearch = finaltrunker-2
    bheight = bheight+boffset
    while mtik > round(bheight/2):
      # EnverPlace(xcoord, ycoord+msearch, leaf, 1, 1)
      # Leaf Radius v2
      pingme = bradius
      pingme2 = bradius-2
      vfile = 1
      while pingme > 0:
        pingme = pingme-1
        EnverPlace(xcoord+vfile, ycoord+msearch, "minecraft:stone", 1, 1)
        vfile = vfile+1
        EnverPlace(xcoord, ycoord+msearch, leaf, 1, 1)
      pingme = bradius
      vfile = 1
      while pingme > 0:
        pingme = pingme-1
        EnverPlace(xcoord-vfile, ycoord+msearch, leaf, 1, 1)
        vfile = vfile+1
      # Radius Placer
      mtik = mtik - 1
      msearch = msearch + 1
    while mtik > 0:
      # EnverPlace(xcoord, ycoord+msearch, leaf, 1, 1)
      # Leaf Radius v2
      pingme = bradius/2
      vfile = 1
      while pingme > 0:
        pingme = pingme-1
        EnverPlace(xcoord+vfile, ycoord+msearch, "minecraft:stone", 1, 1)
        vfile = vfile+1
        EnverPlace(xcoord, ycoord+msearch, leaf, 1, 1)
      pingme = bradius/2
      vfile = 1
      while pingme > 0:
        pingme = pingme-1
        EnverPlace(xcoord-vfile, ycoord+msearch, leaf, 1, 1)
        vfile = vfile+1
      # Radius Placer
      pass
      mtik = mtik - 1
      msearch = msearch + 1
    pass
  if foliage_placer == "minecraft:fancy_foliage_placer":
    bheight = probeher["height"] # 3
    bradius = probeher["radius"] # 2
    boffset = probeher["offset"] # 0
    msearch = 0 # To Draw Trunk
    mtik = bheight + 2
    msearch = finaltrunker-2
    bheight = bheight+1
    while mtik > 0:
      mtik = mtik - 1
      msearch = msearch + 1
      EnverPlace(xcoord, ycoord+msearch, leaf, 1, 1)
      # Leaf Radius v2
      pingme = random.randint(bradius-1, bradius+1)
      vfile = 1
      while pingme > 0:
        pingme = pingme-1
        EnverPlace(xcoord+vfile, ycoord+msearch, "minecraft:stone", 1, 1)
        vfile = vfile+1
      EnverPlace(xcoord, ycoord+msearch, leaf, 1, 1)
      pingme = random.randint(bradius-1, bradius+1)
      vfile = 1
      while pingme > 0:
        pingme = pingme-1
        EnverPlace(xcoord-vfile, ycoord+msearch, leaf, 1, 1)
        vfile = vfile+1
      # Radius Placer
      pass
    pass
  pass



def maketree(
  probeme, # please.... please don't ask.
  probeher, 
  xcoord, 
  trunk, leaf, 
  trunk_placer,
  foliage_placer
  ):
  global foliageInfo
  print("received make tree")
  # Pick Placing Point
  ycoord = biomeheightmap[xcoord]

  # For Multi-Leaves
  foliageCount = -1
  foliageInfo = []
  print(trunk,leaf,trunk_placer,foliage_placer)
  if trunk_placer == "minecraft:straight_trunk_placer":
    bheight = probeme["base_height"]
    hra = probeme["height_rand_a"]
    hrb = probeme["height_rand_b"]
    bheight = bheight + random.randint(hrb, hra)
    publiclogheight = bheight
    msearch = 0 # To Draw Trunk
    mtik = bheight
    while mtik > 0:
      mtik = mtik - 1
      msearch = msearch + 1
      #print("so, Place must be the issue....")
      EnverPlace(xcoord, ycoord+msearch, trunk, 1, 1)
      finaltrunker = msearch
      pass
    foliageInfo.append(
      [
        xcoord,
        msearch
      ]
    )
    foliageCount = foliageCount + 1
    pass
  if trunk_placer == "minecraft:fancy_trunk_placer":
    bheight = probeme["base_height"]
    hra = probeme["height_rand_a"]
    hrb = probeme["height_rand_b"]
    bheight = bheight + random.randint(hrb, hra)
    publiclogheight = bheight
    msearch = 0 # To Draw Trunk
    mtik = bheight
    while mtik > 0:
      mtik = mtik - 1
      msearch = msearch + 1
      #print("so, Place must be the issue....")
      EnverPlace(xcoord, ycoord+msearch, trunk, 1, 1)
      # Decide whether or not to draw branch
      if random.randint(0,4) == 0:
        branchSize = random.randint(-4,4)
        branchTik = branchSize
        branchSearch = 0
        while not branchTik == 0:
          if branchSize < 0:
            branchSearch -= 1
          if branchSize > 0:
            branchSearch += 1
          EnverPlace(xcoord+branchSearch, ycoord+msearch, trunk, 1, 1)
          if branchTik < 0:
            branchTik += 1
          if branchTik > 0:
            branchTik -= 1
        foliageInfo.append(
          [
          xcoord+branchSearch,
          msearch
          ]
        )
        foliageCount += 1
      finaltrunker = msearch
    foliageInfo.append(
      [
        xcoord,
        msearch
      ]
    )
    foliageCount = foliageCount + 1
    pass
  #makeLeaves(
   # foliage_placer = foliage_placer,
    #probeher= probeher,
#    publiclogheight=publiclogheight,
 #   ycoord=ycoord,
  #  xcoord=xcoord,
   # leaf=leaf,
    #finaltrunker=finaltrunker
  #)
  print("Foliage Count ==", foliageCount)
  i = -1
  while not i == foliageCount:
    """
    makeLeaves(
    foliage_placer = foliage_placer,
    probeher= probeher,
    publiclogheight=publiclogheight,
    ycoord=ycoord,
    xcoord=xcoord,
    leaf=leaf,
    finaltrunker=finaltrunker
    )
    """
    try:
      print(foliageInfo[i][0])
    except:
      print("ERROR", foliageInfo)
    makeLeaves(
    foliage_placer = foliage_placer,
    probeher= probeher,
    publiclogheight=publiclogheight,
    ycoord=ycoord,
    xcoord=foliageInfo[i][0],
    leaf=leaf,
    finaltrunker=foliageInfo[i][1]
    )
    i += 1

def runState(
  blocks
):
  if blocks["type"] == "minecraft:simple_state_provider":
    return blocks["state"]["Name"]

def runHeight(
  height,
  phyisicalHeight
  ):
  global heightPoint
  if height["type"] == "minecraft:uniform":
   if not featureSeed.randint(0,1) == 0:
    try:
      topHeight = height["max_inclusive"]["absolute"]
    except:
      try:
        topHeight = blocksBelow0 + height["max_inclusive"]["above_bottom"]
      except:
        topHeight = worldHeight - height["max_inclusive"]["below_top"]
    try:
      bottomHeight = height["min_inclusive"]["absolute"]
    except:
      try:
        bottomHeight = 0 + height["min_inclusive"]["above_bottom"]
      except:
        bottomHeight = worldHeight - height["min_inclusive"]["below_top"]
    if phyisicalHeight < topHeight:
      if phyisicalHeight > bottomHeight:
        return True
   else:
     try:
      topHeight = height["max_inclusive"]["absolute"]
     except:
      try:
        topHeight = blocksBelow0 + height["max_inclusive"]["above_bottom"]
      except:
        topHeight = worldHeight - height["max_inclusive"]["below_top"]
     try:
      bottomHeight = height["min_inclusive"]["absolute"]
     except:
      try:
        bottomHeight = blocksBelow0 + height["min_inclusive"]["above_bottom"]
      except:
        bottomHeight = worldHeight - height["min_inclusive"]["below_top"]
     heightPoint = featureSeed.randint(bottomHeight,topHeight)
     return True
  if height["type"] == "minecraft:trapezoid":
   if not featureSeed.randint(0,1) == 0:
    try:
      topHeight = height["max_inclusive"]["absolute"]
    except:
      try:
        topHeight = blocksBelow0 + height["max_inclusive"]["above_bottom"]
      except:
        topHeight = worldHeight - height["max_inclusive"]["below_top"]
    try:
      bottomHeight = height["min_inclusive"]["absolute"]
    except:
      try:
        bottomHeight = 0 + height["min_inclusive"]["above_bottom"]
      except:
        bottomHeight = worldHeight - height["min_inclusive"]["below_top"]
    if phyisicalHeight < topHeight:
      if phyisicalHeight > bottomHeight:
        if not featureSeed.randint(-64,phyisicalHeight+6) < -48:
          return True
   else:
     try:
      topHeight = height["max_inclusive"]["absolute"]
     except:
      try:
        topHeight = blocksBelow0 + height["max_inclusive"]["above_bottom"]
      except:
        topHeight = worldHeight - height["max_inclusive"]["below_top"]
     try:
      bottomHeight = height["min_inclusive"]["absolute"]
     except:
      try:
        bottomHeight = blocksBelow0 + height["min_inclusive"]["above_bottom"]
      except:
        bottomHeight = worldHeight - height["min_inclusive"]["below_top"]
     heightPoint = featureSeed.randint(bottomHeight,topHeight)
     return True



cnbPower = 0
cnbLastAction = 0
heightPoint = 0

forceChance = 0

def runDecorator(
  decorator,
  heightm,
  hori
  ):
  global cnbPower
  global forceChance
  global cnbLastAction
  global heightPoint
  if decorator["type"] == "minecraft:count_extra":
    print("Feature >> Decorated >> Count Extra")
    if forceChance == 1: return True
    if featureSeed.randint(0, 100) < decorator["config"]["count"]*10:
      if visualDebug >= 1: EnverPlace(hori, 119, "minecraft:dirt", 1, 1)
      return True
    else:
      if featureSeed.randint(0, 100) < decorator["config"]["count"]*10:
        if visualDebug >= 1:EnverPlace(hori, 119, "minecraft:dirt", 1, 1)
        return True
      
  if decorator["type"] == "minecraft:ex_count_extra":
   print("Feature >> Decorated >> Count Extra")
   if forceChance == 1: return True
   try:
    print("a - 0/4")
    if featureSeed.randint(0, (decorator["config"]["extra_chance"]*100)) < (decorator["config"]["extra_chance"]*100):
      print("b - 1/4")
      if featureSeed.randint(1, round(256/(16*((decorator["config"]["count"])+decorator["config"]["extra_count"])))) == 1:
        print("b - 3/4")
        if visualDebug >= 1:EnverPlace(hori, 119, "minecraft:dirt", 1, 1)
        print("b - 4/4")
        return True
    else:
      print("c - 1/4")
      if featureSeed.randint(1, round(256/(16*(decorator["config"]["count"]/2)))) == 1:
        print("c - 2/4")
        if visualDebug >= 1:EnverPlace(hori, 119, "minecraft:dirt", 1, 1)
        print("c - 3/4")
        return True
   except:
     time.sleep(input("yes"))
  if decorator["type"] == "minecraft:count_noise_biased":
        print("Feature >> Decorated >> Count Noise Biased")
        if forceChance == 1: return True
        ntcr = decorator["config"]["noise_to_count_ratio"]
        nf = decorator["config"]["noise_factor"]
        no = decorator["config"]["noise_offset"]
        selection = featureSeed.randint(0,50)
        if selection >= 13 and selection <= 15:
          cnbPower = featureSeed.randint(0,16)
        if cnbPower > 0:
          if visualDebug >= 1:EnverPlace(hori, featureSeed.randint(120,130), "minecraft:stone", 1, 1)
          if not hori == cnbLastAction:
            cnbPower -= 1
            cnbLastAction = hori
          return True

  if decorator["type"] == "minecraft:count":
    print("Feature >> Decorated >> Count")
    if forceChance == 1: return True
    if visualDebug >= 1:EnverPlace(hori, 88, "minecraft:oak_leaves", 1, 1)
    if random.randint(1, 256/(16*decorator["config"]["count"])) == 1:
        return True
  if decorator["type"] == "minecraft:chance":
    print("Feature >> Decorated >> Chance")
    if forceChance == 1: return True
    if visualDebug >= 1:EnverPlace(hori, 87, "minecraft:birch_leaves", 1, 1)
    if decorator["config"]["chance"] == 0:
      return True
    if random.randint(1, decorator["config"]["chance"]) <= 1:
      return True
  if decorator["type"] == "minecraft:square":
    print("Feature >> Decorated >> Square")
    return True
  if decorator["type"] == "minecraft:water_depth_threshold":
    if visualDebug >= 1:EnverPlace(hori, 89, "minecraft:smooth_basalt", 1, 1)
    print("Feature >> Decorated >> Water Depth")
    if decorator["config"]["max_water_depth"] > (sealevel-heightm):
      return True
  if decorator["type"] == "minecraft:range":
    if forceChance == 1: return True
    if runHeight(decorator["config"]["height"], heightm) == True:
      return True
  if decorator["type"] == "minecraft:heightmap" or decorator["type"] == "minecraft:heightmap_spread_double":
    print("Feature >> Decorated >> Heightmap")
    if visualDebug >= 1:EnverPlace(hori, 90, "minecraft:smooth_basalt", 1, 1)
    if decorator["config"]["heightmap"] == "OCEAN_FLOOR":
      heightPoint = biomeheightmap[hori]
      heightm = heightPoint
      if heightm == biomeheightmap[hori]:
        return True
    if decorator["config"]["heightmap"] == "WORLD_SURFACE_WG":
      heightPoint = biomeheightmap[hori]
      heightm = heightPoint
      if heightm == biomeheightmap[hori]:
        if heightm > sealevel:
          return True
    if decorator["config"]["heightmap"] == "WORLD_SURFACE":
      heightPoint = biomeheightmap[hori]
      heightm = heightPoint
      if heightm == biomeheightmap[hori]:
        if heightm > sealevel:
          return True
    if decorator["config"]["heightmap"] == "MOTION_BLOCKING":
      heightPoint = biomeheightmap[hori]
      heightm = heightPoint
      if heightm == biomeheightmap[hori]:
        if heightm > sealevel:
          return True
  if decorator["type"] == "minecraft:decorated":
    print("Feature >> Decorated >> Decorated")
    p1 = runDecorator(
      decorator["config"]["outer"],
      heightm,
      hori
    )
    heightm = p1[1]
    p2 = runDecorator(
      decorator["config"]["inner"],
      heightm,
      hori
    )
    heightm = p2[1]
    if p1[0] == True:
      print("Feature >> Decorated >> Decorated >> True 0/1")
      if p2[0] == True:
        print("Feature >> Decorated >> Decorated >> True 1/1")
        return True

def runTarget(
  targets,
  x,
  y
  ):
  simPoy = y+blocksBelow0
  checkX = round(x)
  checkY = round(y)
  global worldList
  tile = worldList[checkX][checkY]
  ticker = -1
  maxTick = len(targets)
  try:
    while ticker < maxTick:
      ticker += 1
      crawl = targets[ticker]
      if crawl["target"]["predicate_type"] == "minecraft:tag_match":
        try:
          fullList = open("open//data//{}//tags//{}.json".format((crawl["target"]["tag"].split(":"))[0],crawl["target"]["tag"].split(":")[1]), "r")
        except:
          fullList = open("default//data//{}//tags//{}.json".format((crawl["target"]["tag"].split(":"))[0],crawl["target"]["tag"].split(":")[1]), "r")
        if tile in fullList["values"]:
          return [True, crawl["state"]["Name"]]
  except:
    return [False,"Obviously nothing."]

def runfeature(
  featurestring, hori, heightb,
  ):
  heightm = heightb
  global feature
  global crawler
  feature = featurestring
  global caveair
  global caveblock
  global cavedata
  global heightPoint
  global cavef
  global seed
  heightPoint = heightm
  feature = feature.split(":")
  print(f"{os.getcwd()}\open\data\{feature[0]}\worldgen\configured_feature\{feature[1]}.json")
  try:
    featuref = open("open//data//{}//worldgen//configured_feature//{}.json".format(feature[0],feature[1]), "r")
  except:
    print("sussss")
    featuref = open("default//data//{}//worldgen//configured_feature//{}.json".format(feature[0],feature[1]), "r")
  try:
    featuredata = json.load(featuref)
    def readfeature(featuredata2, type):
      heightm = heightb
      heightm = heightPoint
      #rint("Read Feature >>>", featuredata2)
      print("READINGFEATURE", featuredata2["type"])
      if type == "string":
        featuredata2 = json.loads(featuredata2)
      if featuredata2['type'] == "minecraft:ore":
       size = featureSeed.randint(featuredata2["config"]["size"],featuredata2["config"]["size"]+12)
       xFact = hori - featureSeed.randint(10,20)
       multiplier = featureSeed.randint(1,2)
       tickerFac = 0
       while not tickerFac > size:
        atXLocation = xFact-featureSeed.randint(-3,3)
        
        atYLocation = heightm-featureSeed.randint(-3,3)
        #EnverPlace(atXLocation-20, atYLocation-20, "minecraft:stone", 1, 1)
        oreSizeX = featureSeed.randint(1, 5)
        oreSizeY = featureSeed.randint(1, 5)
        highlight = Rectangle(Point(atXLocation,atYLocation),Point(atXLocation+oreSizeX,atYLocation+oreSizeY))
        oreDrawX = [] # Will Draw
        oreDrawY = [] # Will Draw
        yTick = 0
        try:
         while not yTick == oreSizeY:
          xTick = 0
          while not xTick == oreSizeX:
            if not featureSeed.randint(0,10) == 0:
              oreDrawX.append(1)
            else:
              oreDrawX.append(0)
            xTick += 1
          oreDrawY.append(oreDrawX)
          oreDrawX = []
          yTick += 1
        except:
          print(oreDrawX, oreDrawY, oreSizeX, oreSizeY, xTick, yTick,atXLocation,atYLocation)
          input("what")
        yTick = 0
        try:
         while not yTick == oreSizeY:
          print("Cleared a Y")
          xTick = 0
          try:
           while not xTick == oreSizeX:
            print("Cleared an X")
            if oreDrawY[yTick][xTick] == 1:
              tickerFac += 1
              print("Trying to place")
              test = runTarget(featuredata2["config"]["targets"], atXLocation+xTick,atYLocation+yTick)
              if test[0] == True:
                EnverPlace(
                atXLocation+xTick,
                atYLocation+yTick,
                test[1],
                1,
                1
              )
              print("Just placed")
              #print(input("---------Pause------------"))
            xTick += 1
          except:
           print("Failed at X (MIGHT BE AN OUT OF INDEX)")
          yTick += 1

        except:
          print("Failed at Y (MIGHT BE AN OUT OF INDEX)")
      try:
       if featuredata2["type"] == "minecraft:ex_ore":
        size = featuredata2["config"]["size"]
        xFact = hori - featureSeed.randint(10,20)
        oreSizeX = featureSeed.randint(1, size/2)
        oreSizeY = featureSeed.randint(1, size/2)
        oreDrawX = [] # Will Draw
        oreDrawY = [] # Will Draw
        # Setup Will Draw
        yTick = 0
        try:
         while not yTick == oreSizeX:
          xTick = 0
          while not xTick == oreSizeX:
           try:
            if featureSeed.randint(0,(xpos- oreSizeX/2)) == 0:
              oreDrawX.append(1)
            else:
              oreDrawX.append(0)
            xTick += 1
           except:
            print(input("woah so cool."))
          oreDrawY.append(oreDrawX)
          oreDrawX = []
          yTick += 1
        except:
          print(input("ur a fuck up"))
        # Aanndd to draw
        EnverPlace(
          hori,
          heightm,
          "minecraft:grass",
          1,
          1
        )
        yTick = 0
        try:
         while not yTick == oreSizeY:
          print("Cleared a Y")
          xTick = 0
          try:
           while not xTick == oreSizeX:
            print("Cleared an X")
            if oreDrawY[yTick][xTick] == 1:
              print("Trying to place")
              EnverPlace(
                hori+xTick,
                heightm+yTick,
                featuredata2["config"]["targets"][0]["state"]["Name"],
                1,
                1
              )
              print("Just placed")
              #print(input("---------Pause------------"))
            xTick += 1
          except:
           print("Failed at X (MIGHT BE AN OUT OF INDEX)")
          yTick += 1

        except:
          print("Failed at Y (MIGHT BE AN OUT OF INDEX)")
      except:
        print(input("Failed at Ore"))
      if featuredata2["type"] == "minecraft:random_patch":
        if random.randint(0,100) < 100:
          EnverPlace(
            hori,
            heightm+1,
            runState(featuredata2["config"]["state_provider"]),
            1,
            1
          )
      if featuredata2["type"] == "minecraft:random_selector":
        print("randomsel ):")
        i = len(featuredata2["config"]["features"]) - 1
        finalSel = None
        print("randsel", i)
        while not i == -1:
          if (random.randint(0, 100)/100) < featuredata2["config"]["features"][i]["chance"]:
            finalSel = i
            i = 0
          i -= 1
        print(finalSel,i)
        if finalSel == None:
          try:
            a = featuredata2["config"]["default"].startswith("hi")
            b = featuredata2["config"]["default"]
            b = b.split(":")
            print("saveme", b)
            try:
              readfeature(
              json.load(open("open//data//{}//worldgen//configured_feature//{}.json".format(b[0],b[1]),"r")), "file")
              print("Feature >> Decorated >> Sent")
            except:
              readfeature(
              json.load(open("default//data//{}//worldgen//configured_feature//{}.json".format(b[0],b[1]),"r")), "file")
              print("Feature >> Decorated >> Sent")
          except:
            readfeature(featuredata2["config"]["default"], "file")
        else:
          try:
            a = featuredata2["config"]["features"][finalSel]["feature"].startswith("hi")
            b = featuredata2["config"]["features"][finalSel]["feature"]
            b = b.split(":")
            print("saveme", b)
            try:
              readfeature(
              json.load(open("open//data//{}//worldgen//configured_feature//{}.json".format(b[0],b[1]), "r")), "file")
              print("Feature >> Decorated >> Sent")
            except:
              readfeature(
              json.load(open("default//data//{}//worldgen//configured_feature//{}.json".format(b[0],b[1]),"r")), "file")
              print("Feature >> Decorated >> Sent")
          except:
            readfeature(featuredata2["config"]["features"][finalSel]["feature"], "file")
      print("--==--")
      if featuredata2["type"] == "minecraft:decorated":
        print("Feature >> Decorated")
        if runDecorator(featuredata2["config"]["decorator"], heightm, hori) == True:
          heightm = heightPoint
          print("Feature >> Decorated >> True")
          try:
            a = featuredata2["config"]["feature"].startswith("hi")
            b = featuredata2["config"]["feature"]
            b = b.split(":")
            print("saveme", b)
            try:
              readfeature(
              json.load(open("open//data//{}//worldgen//configured_feature//{}.json".format(b[0],b[1]), "r")), "file")
              print("Feature >> Decorated >> Sent")
            except:
              readfeature(
              json.load(open("default//data//{}//worldgen//configured_feature//{}.json".format(b[0],b[1]),"r")), "file")
              print("Feature >> Decorated >> Sent")
          except:
            readfeature(featuredata2["config"]["feature"], "file")
      if featuredata2["type"] == "minecraft:count_noise_biased":
        ntcr = featuredata2["config"]["noise_to_count_ratio"]
        nf = featuredata2["config"]["noise_factor"]
        no = featuredata2["config"]["noise_offset"]
        random.seed(nf)
        selection = random.randint(0,20)
        if selection > 0 and selection < 20:
          random.seed(seed)
          print("""
          ----------------------
          
          
          
          
          
          
          
          
          
          
          
          
                COUNT
          
          
          
          
          
          
          
          
          
          
          
          
          ----------------------
          """)
          return True
        random.seed(seed)
      if featuredata2["type"] == "heightchance":
        print("--------HEIGHTCHANCE--------")
        if heightm < featuredata2["highercoord"]:
          print("--------INRANGE--------")
          #if random.randint(featuredata2["lowercoord"], featuredata2["highercoord"]-heightm):
          if random.randint(featuredata2["lowercoord"], random.randint(featuredata2["lowercoord"], featuredata2["highercoord"]-heightm)) > (featuredata2["lowercoord"] + featuredata2["chance"]):
            if featuredata2["newfeatureset"] == "reference":
              readfeature(json.load(open("{}//features//{}.json".format(namespace,featuredata2["newfeature"]), "r")), "file")
            if featuredata2["newfeatureset"] == "custom":
              readfeature(featuredata2["newfeature"], "file")
              print(featuredata2["newfeature"])
            pass
          pass
        pass
      if featuredata2["type"] == "heightrun":
        print("--------HEIGHTRUN--------")
        if heightm < featuredata2["highercoord"] and heightm > featuredata2["lowercoord"]:
          print("--------INRANGE--------")
          if featuredata2["newfeatureset"] == "reference":
            readfeature(json.load(open("{}//features//{}.json".format(namespace,featuredata2["newfeature"]), "r")), "file")
          if featuredata2["newfeatureset"] == "custom":
            readfeature(featuredata2["newfeature"], "file")
            print(featuredata2["newfeature"])
        pass
      if str(featuredata2["type"]) == "minecraft:tree":
        print("--------Tree Decorated--------")
        # The configurations are ripped from minecraft cause whatever. credit to them for config base. (I wanna see famous data packs in this)
        # First lets find out how the tree spawns
        openingconfig = featuredata2["config"] # Get a 'data' variable to build off of.
        print("0/4")
        #max_water_depth = openingconfig["max_water_depth"]
        #heightmap = openingconfig["heightmap"]
        # Lets get trunks
        trunkconfig = openingconfig["trunk_provider"]
        trunkblock = (trunkconfig["state"])["Name"]
        print("1/4")
        # Lets get leaves
        leafconfig = openingconfig["foliage_provider"]
        leafblock = (leafconfig["state"])["Name"]
        print("2/4")
        # Trunk Placer
        trplacer = (openingconfig["trunk_placer"])["type"]
        leplacer = (openingconfig["foliage_placer"])["type"]
        print("3/4")
        #if openingconfig["max_water_depth"] > (sealevel-heightm):
        maketree(
          # ~~horny kid stuff~~
          probeme=openingconfig["trunk_placer"],
          probeher=openingconfig["foliage_placer"],
          # Locations
          xcoord=hori,
          # Do the block based configs :P
          trunk=trunkblock,
          leaf=leafblock,
          # Placers
          trunk_placer=trplacer,
          foliage_placer=leplacer
        )
        return True
      if featuredata2["feature_type"] == "minimap":
          print("--------Minimap--------")
          EnverPlace(hori/featuredata2["mapscale"], heightm/featuredata2["mapscale"]+100, featuredata2["block"], 1/featuredata2["mapscale"], 1/featuredata2["mapscale"])
          if featuredata2["newfeatureset"] == "reference":
            readfeature(json.load(open("{}//features//{}.json".format(namespace,featuredata2["newfeature"]), "r")), "file")
          if featuredata2["newfeatureset"] == "custom":
            readfeature(featuredata2["newfeature"], "file")
            print(featuredata2["newfeature"])
      if featuredata2["feature_type"] == "setblock":
        print("--------SETBLOCKPING--------")
        EnverPlace(hori, heightm, featuredata2["block"], 1, 1)
      if featuredata2["feature_type"] == "offsetplace":
        print("--------SETOFFSETBLOCKPING--------")
        EnverPlace(hori+featuredata2["offsetx"], heightm+featuredata2["offsety"], featuredata2["block"], 1, 1)
        if featuredata2["newfeatureset"] == "reference":
          readfeature(json.load(open("{}//features//{}.json".format(namespace,featuredata2["newfeature"]), "r")), "file")
        if featuredata2["newfeatureset"] == "custom":
          readfeature(featuredata2["newfeature"], "file")
          print(featuredata2["newfeature"])
      if featuredata2["feature_type"] == "anchoredplace":
        print("--------SETANCHOREDBLOCKPING--------")
        EnverPlace(hori+featuredata2["offsetx"], 0+featuredata2["offsety"], featuredata2["block"], 1, 1)
        if featuredata2["newfeatureset"] == "reference":
          readfeature(json.load(open("{}//features//{}.json".format(namespace,featuredata2["newfeature"]), "r")), "file")
        if featuredata2["newfeatureset"] == "custom":
          readfeature(featuredata2["newfeature"], "file")
          print(featuredata2["newfeature"])
      if featuredata2["feature_type"] == "blockthenfeature":
        print("--------BLOCKTHENFURTHER--------")
        EnverPlace(hori, heightm, featuredata2["block"], 1, 1)
        if featuredata2["newfeatureset"] == "reference":
          readfeature(json.load(open("{}//features//{}.json".format(namespace,featuredata2["newfeature"]), "r")), "file")
        if featuredata2["newfeatureset"] == "custom":
          readfeature(featuredata2["newfeature"], "file")
          print(featuredata2["newfeature"])
      if featuredata2["feature_type"] == "nothing":
        print("--------NOTHINGPING--------")
        pass
      if featuredata2["feature_type"] == "chance":
        print("--------CHANCEPING--------")
        if random.randint(featuredata2["minchance"], featuredata2["maxchance"]) < featuredata2["chance"]:
          print("Random Number from chance succeeded")
          if featuredata2["newfeatureset"] == "reference":
            readfeature(json.load(open("{}//features//{}.json".format(namespace,featuredata2["newfeature"]), "r")), "file")
          if featuredata2["newfeatureset"] == "custom":
                readfeature(featuredata2["newfeature"], "file")
                print(featuredata2["newfeature"])
    #if settingFeaturesInCaves == "True":
    readfeature(featuredata, "file")
    pass
  finally:
    crawler = "open"
biomeDry = 10
biomeBleed = 15
def opencave():
  global caveair
  global caveblock
  global cavedata
  global cavef
  global currentcave
  currentcave = data["cavesystem"]
  with open("{}//cavesystem//{}.json".format(namespace,currentcave), "r") as cavef:
    cavedata = json.load(cavef)
    print (cavedata["PingFile"])
    if cavedata["VersionFile"] == 1:
      print("VersionFile1") # Heya! Please Note- This doesn't fully mean things will work alright- PLEASE- Update Version Files to standard to ensure things don't break!
      # Things should hopefully work but- version files CAN NOT BE UPDATED TO ENSURE SUPPORT- IF A VALUE CHANGES IT INHERITS FROM THE OTHER GEN FILE
      caveair = cavedata["caveaircolor"]
      caveblock = cavedata["block"]
      pass
  pass
choosertag = "default"
def openbiome():
  global genopen
  global blockmap
  global xpos
  global height
  global scaling
  global smoothness
  global forcetop
  global naturaltopy
  global naturalbottomy
  global BiomePower
  global biomefallout
  global forcebottom
  global f
  global surface
  global oceancol
  global data
  global br
  global magnetism
  global ocean
  global bg
  global bb
  global GenVer
  global skycol
  print(genopen)
  namespace = (genopen.split(':'))[0]
  genopen = (genopen.split(':'))[1]
  try:
    love = open("open//data//{}//worldgen//biome//{}.json".format(namespace, genopen), "r")
  except:
    love = open("default//data//{}//worldgen//biome//{}.json".format(namespace, genopen), "r")
  with love as f:
      data = json.load(f)
      global depthMapping
      global scaleMapping
      global biomeDry
      global biomeBleed
      try:
        biomeDry = data["biomeDry"]
        biomeBleed = data["biomeBleed"]
      except:
        biomeDry = 10
        biomeBleed = 15
      depthMapping = data["depth"]
      scaleMapping = data["scale"]
      # Here, We present the new biome system- introduced in 0.2.0
      forcetop = settingSurfaceLevel + ((depthMapping*10)+(round(scaleMapping*4)+5))
      naturaltopy = settingSurfaceLevel + ((depthMapping*10)+(round(scaleMapping*3)+3))
      naturalbottomy = settingSurfaceLevel + ((depthMapping*10)+(round(scaleMapping*3)-3))
      forcebottom = settingSurfaceLevel + ((depthMapping*10)+(round(scaleMapping*4)-5))
      #EnverPlace(xpos, forcetop+20, "minecraft:grass", 1, forcetop-forcebottom)
      print(forcebottom, naturalbottomy, naturaltopy, forcetop)
      #smoothness = 80 #data["smoothMapping"]
      # Transference Settings
      BiomePower = 90# (data["transferSettings"])["biomeEnergy"]
      GenVer = "Enver"
      surface = (data["surface_builder"])
      biomefeatures = (data["features"])

  pass
def oldPlace():
  openbiome()
  global blockmap
  global display
  global colin
  global xpos
  global height
  global canvas
  global scaling
  global smoothness
  global forcetop
  global naturaltopy
  global naturalbottomy
  global forcebottom
  global BiomePower
  global biomefallout
  global placeloc
  global block
  global drawingsystem
  #c = turtle
  #placeloc = Point(xpos*blockmap, height*(-blockmap))
  print(xpos*blockmap)
  print("hi")
  #placeloc.draw(display)
  if drawingsystem == "Graphics.py":
    block = Rectangle(Point(xpos*blockmap, screeny-(height*blockmap)),Point((xpos*blockmap)-blockmap, screeny-(height*(blockmap)+blockmap)))
    block.setFill(data["biomecolour"])
    block.draw(display)
  if drawingsystem == "Turtle":
    c = turtle
    c.goto(xpos*blockmap, (blockmap*height)+(2*blockmap))
    c.down()
    #c.goto(xpos*blockmap, (blockmap*height)+(2*blockmap))
  print((blockmap*height)+(100*blockmap))
  xpos = xpos + 1
  # Calculate Height Change
  # First Determine if we want to take the height step.
  if height < forcebottom:
    height = height + 1
  elif height > forcetop:
    height = height - 1
  elif random.randint(0, 100) > smoothness:
    print("Height Change")
    if height > naturaltopy:
      height = height - random.randint(0,1)
    elif height < naturalbottomy:
      height = height + random.randint(0,1)
    else:
      height = height + random.randint(-1, 1)
  #c.begin_fill
  print(scaling)
  print("Height:", height)
  #DRAW OCEAN
  if height < sealevel:
    #c.pencolor(str(oceancol))
    block = Rectangle(Point(xpos*blockmap, screeny-(sealevel*blockmap)),Point((xpos*blockmap)-blockmap, screeny-(sealevel*(blockmap)+blockmap)))
    block.draw(display)
    print((blockmap*height)+(100*blockmap))
    pass
  pass
def openBlock(assetx):
  global blockSystem
  genopen = assetx
  o = open("{}//blocks//{}.json".format(namespace,genopen), "r")
  data2 = json.load(o)
def EnverPlace(pox, poy, tile, sx, sy):
  simPoy = poy+blocksBelow0
  checkX = round(pox)
  checkY = round(poy)
  global worldList
  #print(worldList, checkY,checkX)
  worldList[checkX][checkY] = tile
  tile = tile.split(":")
  o = open("datafile//{}//blocks//{}.json".format(tile[0],tile[1]), "r")
  data2 = json.load(o)
  if drawingsystem == "Spark":
    global xpos
    global blockmap
    global block
    global display
    global blockSystem
    global height
    blockSystem = data2["system"]
    if blockSystem == 0:
      block = spark.Rectangle(spark.Point(pox*blockmap, screeny-(simPoy*blockmap)),spark.Point((pox*blockmap)-blockmap, screeny-((simPoy*blockmap)-(blockmap*sy))))
      block.setFill(data2["fillcol"])
      block.setWidth(0)
      block.draw(display)
    if blockSystem == 1:
     plhx = (xpos*blockmap)-blockmap
     plhy = screeny-(height*(blockmap)+blockmap)
     if data2["rotation"] == "x":
      blockScale = data2["scale"]
      keyMap = data2["keys"]
      ymute = 1
      if random.randint(0,1) == 0:
       while ymute < blockScale+1:
        xmute = 1
        while xmute < blockScale+1:
          block = spark.Rectangle(spark.Point((pox*blockmap), screeny-(simPoy*blockmap)),spark.Point((pox*blockmap)-(blockmap/((blockScale/blockScale)*xmute)), screeny-((simPoy*blockmap)-((blockmap*sy)/((blockScale/blockScale)*ymute)))))
          block.setWidth(0)
          if "{}".format((data2["{}".format(ymute)])[xmute-1]) == "0":
            #block.draw(display)
            pass
          else:
            block.setFill(keyMap["{}".format((data2["{}".format(xmute)])[ymute-1])])
            block.draw(display)
            pass
          xmute = xmute+1
        ymute = ymute+1
      else:
       while ymute < blockScale+1:
        xmute = 1
        while xmute < blockScale+1:
          block = spark.Rectangle(
            spark.Point(
              (pox*blockmap), screeny-(simPoy*blockmap)),
            spark.Point(
              (pox*blockmap)-(blockmap/((blockScale/blockScale)*xmute)), 
              screeny-((simPoy*blockmap)-((blockmap*sy)/((blockScale/blockScale)*ymute)))
              )
            )
          block.setWidth(0)
          print(settingSkyColor)
          # taking a break at 5:51pm on the 15th of September 2021. idk why i'm saying, cya soon- future andi
          if "{}".format((data2["{}".format(ymute)])[xmute-1]) == "0":
            pass
          else:
            block.setFill(keyMap["{}".format((data2["{}".format(xmute)])[ymute-1])])
            block.draw(display)
            pass
          xmute = xmute+1
        ymute = ymute+1
  
      blockScale = data2["scale"]
      keyMap = data2["keys"]
      ymute = 1
      while ymute > blockScale+1:
        xmute = 1
        while xmute < blockScale+1:
          block = spark.Rectangle(
            spark.Point(
              (
                pox*blockmap
              ), 
                screeny-(
                  simPoy*blockmap
                )
              ),
            spark.Point(
              (
                pox*blockmap
              )-(
                blockmap/(
                  (
                    blockScale/blockScale
                  )*xmute
                )
              ), screeny-(
                (
                  simPoy*blockmap
                )-(
                (blockmap*sy
              )/(
                (blockScale/blockScale
              )*ymute)
            )
          )
          )
          )
          print("KEY VALUES:")
          print(xmute)
          print(data2["{}".format(ymute)])
          print((data2["{}".format(ymute)])[xmute-1])
          print(keyMap["{}".format((data2["{}".format(ymute)])[xmute-1])])
          block.setFill(keyMap["{}".format((data2["{}".format(ymute)])[xmute-1])])
          block.setWidth(0)
          if "{}".format((data2["{}".format(ymute)])[xmute-1]) == "0":
            #block.draw(display)
            pass
          else:
            block.setFill(keyMap["{}".format((data2["{}".format(xmute)])[ymute-1])])
            block.draw(display)
            pass
          xmute = xmute+1
        ymute = ymute+1
     elif data2["rotation"] == "xy-flip":
      blockScale = data2["scale"]
      keyMap = data2["keys"]
      ymute = 1
      if random.randint(0,1) == 0:
       while ymute < blockScale+1:
        xmute = 1
        while xmute < blockScale+1:
          block = spark.Rectangle(spark.Point((pox*blockmap), screeny-(simPoy*blockmap)),spark.Point((pox*blockmap)-(blockmap/((blockScale/blockScale)*xmute)), screeny-((simPoy*blockmap)-((blockmap*sy)/((blockScale/blockScale)*ymute)))))
          block.setWidth(0)
          if "{}".format((data2["{}".format(ymute)])[xmute-1]) == "0":
            #block.draw(display)
            pass
          else:
            block.setFill(keyMap["{}".format((data2["{}".format(xmute)])[ymute-1])])
            block.draw(display)
            pass
          xmute = xmute+1
        ymute = ymute+1
      else:
       while ymute < blockScale+1:
        xmute = 1
        while xmute < blockScale+1:
          block = spark.Rectangle(
            spark.Point(
              (pox*blockmap), screeny-(simPoy*blockmap)),
            spark.Point(
              (pox*blockmap)-(blockmap/((blockScale/blockScale)*xmute)), 
              screeny-((simPoy*blockmap)-((blockmap*sy)/((blockScale/blockScale)*ymute)))
              )
            )
          block.setWidth(0)
          print(settingSkyColor)
          # taking a break at 5:51pm on the 15th of September 2021. idk why i'm saying, cya soon- future andi
          if "{}".format((data2["{}".format(ymute)])[xmute-1]) == "0":
            pass
          else:
            block.setFill(keyMap["{}".format((data2["{}".format(xmute)])[ymute-1])])
            block.draw(display)
            pass
          xmute = xmute+1
        ymute = ymute+1
     elif data2["rotation"] == "improved":
      blockScale = data2["scale"]
      keyMap = data2["keys"]
      xmute = 1
      if random.randint(0,0) == 0:
       while xmute < blockScale+1:
        ymute = 1
        while ymute < blockScale+1:
          block = spark.Rectangle(spark.Point((pox*blockmap), screeny-(simPoy*blockmap)),spark.Point((pox*blockmap)-(blockmap/((blockScale/blockScale)*xmute)), screeny-((simPoy*blockmap)-((blockmap*sy)/((blockScale/blockScale)*(ymute))))))
          block1 = spark.Rectangle(spark.Point((pox*blockmap), screeny-(simPoy*blockmap)),spark.Point((plhx/blockScale)*xmute, (plhy/blockScale)*ymute))
          block.setWidth(0)
          if keyMap["{}".format((data2["{}".format(blockScale+1-ymute)])[xmute-1])] == "skyblue1":
            #block.draw(display)
            pass
          else:
            block.setFill(keyMap["{}".format((data2["{}".format(blockScale+1-ymute)])[xmute-1])])
            block.draw(display)
            pass
          ymute = ymute+1
        xmute = xmute+1
  
  else:
    global blocksel
    openBlock(tile)
    openbiome()
    global colin
    global height1
    global height2
    global canvas
    global BiomePower
    global magnetism
    global biomefallout
    global placeloc
    global block2
    #c = turtle
    placeloc = Point(xpos*blockmap, height*(-blockmap))
    print(xpos*blockmap)
    print("hi")
    # Place 3D Blocks
    placeloc.draw(display)
    # Place 3D Blocks
    if drawingsystem == "Graphics.py":
      block = Rectangle(Point(pox*blockmap, screeny-(poy*blockmap)),Point((pox*blockmap)-blockmap, screeny-((poy*blockmap)-(blockmap*sy))))
      block.setFill(data2["fillcol"])
      block.setOutline(data2["outcol"])
      block.draw(display)
    if drawingsystem == "Turtle":
      c = turtle
      c.down()
      c.goto(pox*blockmap, (blockmap*poy)+(2*blockmap))
      c.pencolor(data2["fillcol"])
      c.begin_fill
    pass
def calculatechangeenver():
  global caveopen
  global caveair
  opencave()
  global blockmap
  global display
  global colin
  global xpos
  global height
  global height1
  global height2
  global canvas
  global scaling
  global smoothness
  global forcetop
  global naturaltopy
  global naturalbottomy
  global forcebottom
  global BiomePower
  global magnetism
  global biomefallout
  global placeloc
  global block
  global surface
  block2 = Rectangle(Point(xpos*blockmap, screeny+(height*blockmap)),Point((xpos*blockmap)-blockmap, 0))
  block2.setFill(data["skycolour"])
  block2.setOutline(data["skycolour"])
  block2.draw(display)
  vo = open("{}//builder//{}.json".format(namespace,surface), "r")
  surafac = json.load(vo)
  print("Calculate Change of Enver Generation")
  if surafac["system"] == "default":
    if settingSurfaceEnabled == "True":
      EnverPlace(xpos, height, surafac["config"]["top_material"]["Name"], 1, 1)
    if settingUnderSurface == "True":
      EnverPlace(xpos, height-1, surafac["config"]["under_material"]["Name"], 1, 4)
  if surafac["system"] == "plateau":
    if settingSurfaceEnabled == "True":
      EnverPlace(xpos, height, surafac[str(height)], 1, 1)
    if settingUnderSurface == "True":
      EnverPlace(xpos, height-1, surafac[str(height-1)], 1, 1)
      EnverPlace(xpos, height-2, surafac[str(height-2)], 1, 1)
      EnverPlace(xpos, height-3, surafac[str(height-3)], 1, 1)
      EnverPlace(xpos, height-4, surafac[str(height-4)], 1, 1)
      EnverPlace(xpos, height-5, surafac[str(height-5)], 1, 1)
      EnverPlace(xpos, height-6, surafac[str(height-6)], 1, 1)
      EnverPlace(xpos, height-7, surafac[str(height-7)], 1, 1)
      EnverPlace(xpos, height-8, surafac[str(height-8)], 1, 1)

  if height < sealevel:
    if settingSeaLevelWater == "True":
      waterfog = Rectangle(Point(xpos*blockmap, screeny-(sealevel*blockmap)),Point((xpos*blockmap)-blockmap, screeny-((height*blockmap)-(blockmap*1))))
      waterfog.setFill(oceancol)
      waterfog.setOutline(oceancol)
      waterfog.draw(display)
      EnverPlace(xpos, sealevel, surafac["water_material"], 1, 1)

  def Step1(): # This is to do the height variation
    global xpos
    xpos = xpos + 1
    global height
    # Calculate Height Change
    # First Determine if we want to take the height step.
    if height < forcebottom:
      height = height + 1
    elif height > forcetop:
      height = height - 1
    elif random.randint(0, 100) > smoothness:
      print("Height Change")
      if height > naturaltopy:
        height = height - random.randint(0,1)
      elif height < naturalbottomy:
        height = height + random.randint(0,1)
      else:
        height = height + random.randint(-1, 1)
  # Run through Cave
  if surafac["system"] == "default":
    cavedraw = height-4
  if surafac["system"] == "plateau":
    cavedraw = height-8
  while cavedraw > 0:
    cavedraw = cavedraw-1
    if settingCavesenabled == "True":
      if cavedata["system"] == "default":
        #cavedraw = cavedraw-1
        EnverPlace(xpos, cavedraw, cavedata["block"], 1, 1)
        runfeature(random.choice(cavedata["AlwaysDo"]), xpos, cavedraw)
      if cavedata["system"] == "plateau":
        #cavedraw = cavedraw-1
        EnverPlace(xpos, cavedraw, surafac[str(cavedraw-1)], 1, 1)
        runfeature(random.choice(cavedata["AlwaysDo"]), xpos, cavedraw)
  # Change Generator Configs
  Step1()
  

def placeblock():
  global GenVer
  if GenVer == "Old":
    oldPlace()
  if GenVer == "Enver":
    calculatechangeenver()
debugMode = "False"
# TEXT PASSTHROUGH
textp = "default"
biomeheightmap = []
blockheightmap = [] # This is to find surface block (before features)


pointOfInterest = 1 # The selected part of the dimension file.

stopScript = 0

def inis():
      #global nextbiome
      global pata
      global genopen
      global stopScript
      stopScript = 0
      pata = json.load(open("datafile//choosertag//{}.json".format(choosertag), "r"))
      genopen = random.choice(pata["biomes"])
      biomechoose(display)

def debug():
      print("---Debug Menu---")
      print("Please enter a command!")
      questionAsked = input(">> ")
      if questionAsked == "help":
        print("""
        ---Help Menu---
        help : opens this menu
        checkblock : Displays block at coords entered
        """)
      if questionAsked == "checkblock":
        checkX = input("block X >> ")
        checkY = input("block Y >> ")
        print("The block at", checkX, ",", checkY, "is", worldList[checkX][checkY])
      debug()

def biomechoose(display):
     if debugMode == "False" and stopScript == 0:
      global nextbiome
      global heightPoint
      global genopen
      #global EnverPlace
      global blockmap
      global choosertag
      global pointOfInterest
      global pata
      global xpos
      global surafac
      global height
      global scaling
      global data
      global smoothness
      global forcetop
      global namespace
      global naturaltopy
      global naturalbottomy
      global forcebottom
      try:
        preSetupNextData = str(open("open//data//{}//worldgen//biome//{}.json".format(namespace,nextbiome.split(":")[1]), "r").read())
      except:
        preSetupNextData = str(open("default//data//{}//worldgen//biome//{}.json".format(namespace,nextbiome.split(":")[1]), "r").read())
      print(preSetupNextData)
      nextdata = json.loads(re.sub("//.*","",preSetupNextData,flags=re.MULTILINE))
      #global surface
      pata = json.load(open("datafile//choosertag//{}.json".format(choosertag), "r"))
      nextbiome = biomeSeed.choice(pata["biomes"])
      #global biomeheightmap
      size = random.randint(50, 150)
      num = size
      # Do Grass Work
      genopen = nextbiome

      # Biome Changing
      try:
        dimension = json.load(open("open//data//minecraft//dimension//overworld.json".format(namespace), "r"))
      except:
        dimension = json.load(open("default//data//minecraft//dimension//overworld.json".format(namespace), "r"))
      generatorWindow = dimension["generator"]["biome_source"]["biomes"]
      diAltitude = generatorWindow[pointOfInterest]["parameters"]["altitude"]
      diTemperature = generatorWindow[pointOfInterest]["parameters"]["temperature"]
      diHumidity = generatorWindow[pointOfInterest]["parameters"]["humidity"]
      diWeirdness = generatorWindow[pointOfInterest]["parameters"]["weirdness"]
      diOffset = generatorWindow[pointOfInterest]["parameters"]["offset"]
      exPOI = pointOfInterest
      while exPOI == pointOfInterest:
        sus = biomeSeed.randint(0, len(generatorWindow))
        olAltitude = generatorWindow[sus]["parameters"]["altitude"]
        olTemperature = generatorWindow[sus]["parameters"]["temperature"]
        olHumidity = generatorWindow[sus]["parameters"]["humidity"]
        olWeirdness = generatorWindow[sus]["parameters"]["weirdness"]
        olOffset = generatorWindow[sus]["parameters"]["offset"]
        if (diAltitude - olAltitude) < 0.05 or (diAltitude - olAltitude) > -0.05:
          if (diTemperature - olTemperature) < 0.15 or (diTemperature - olTemperature) > -0.1:
            if (diHumidity - olHumidity) < 0.1 or (diHumidity - olHumidity) > -0.15:
              if (diWeirdness - olWeirdness) < 0.02 or (diWeirdness - olWeirdness) > -0.02:
                if (diOffset - olOffset) < 0.03 or (diOffset - olOffset) > -0.03:
                  exPOI = sus      
      pointOfInterest = exPOI
      genopen = generatorWindow[pointOfInterest]["biome"]
      sinOpen = genopen.split(":")
      print(f"{os.getcwd()}\open\data\{sinOpen[0]}\worldgen/biome\{sinOpen[1]}.json")
      openbiome()
      while num > 0:
        worldList.append(blankFormat)
        print("numfile:", num)
        num = num - 1
        biomeheightmap.append(height)
        EnverPlace(xpos, 100+(pointOfInterest/100), "minecraft:stone", 1, 1)
        EnverPlace(xpos, 105+diAltitude, "minecraft:stone", 1, 0.1)
        EnverPlace(xpos, 106+diTemperature, "minecraft:stone", 1, 0.1)
        EnverPlace(xpos, 107+diHumidity, "minecraft:stone", 1, 0.1)
        EnverPlace(xpos, 108+diWeirdness, "minecraft:stone", 1, 0.1)
        EnverPlace(xpos, 109+diOffset, "minecraft:stone", 1, 0.1)
        if settingSkyEnabled == "True":
          block2 = Rectangle(Point(xpos*blockmap, screeny+(height*blockmap)),Point((xpos*blockmap)-blockmap, 0))
          block2.setFill(data["skycolour"])
          block2.setOutline(data["skycolour"])
          block2.draw(display)
        print(surface)
        try:
          vo = open("open//data//{}//worldgen//configured_surface_builder//{}.json".format((surface.split(":")[0]), (surface.split(":")[1])), "r")
          surafac = json.load(vo)
        except:
          vo = open("default//data//{}//worldgen//configured_surface_builder//{}.json".format((surface.split(":")[0]), surface.split(":")[1]), "r")
          surafac = json.load(vo)
        print("Calculate Change of Enver Generation")
        if surafac["type"] == "minecraft:swamp":
          if settingSurfaceEnabled == "True":
            EnverPlace(xpos, height, surafac["config"]["top_material"]["Name"], 1, 1)
            blockheightmap.append(surafac["config"]["top_material"]["Name"])
          if settingUnderSurface == "True":
            EnverPlace(xpos, height-1, surafac["config"]["under_material"]["Name"], 1, 1)
            EnverPlace(xpos, height-2, surafac["config"]["under_material"]["Name"], 1, 1)
            EnverPlace(xpos, height-3, surafac["config"]["under_material"]["Name"], 1, 1)
            EnverPlace(xpos, height-4, surafac["config"]["under_material"]["Name"], 1, 1)
        if surafac["type"] == "minecraft:default":
          if settingSurfaceEnabled == "True":
            EnverPlace(xpos, height, surafac["config"]["top_material"]["Name"], 1, 1)
            blockheightmap.append(surafac["config"]["top_material"]["Name"])
          if settingUnderSurface == "True":
            EnverPlace(xpos, height-1, surafac["config"]["under_material"]["Name"], 1, 1)
            EnverPlace(xpos, height-2, surafac["config"]["under_material"]["Name"], 1, 1)
            EnverPlace(xpos, height-3, surafac["config"]["under_material"]["Name"], 1, 1)
            EnverPlace(xpos, height-4, surafac["config"]["under_material"]["Name"], 1, 1)
        if height < sealevel:
            if settingSeaLevelWater == "True":
              waterfog = Rectangle(Point(xpos*blockmap, screeny-((sealevel+blocksBelow0)*blockmap)),Point((xpos*blockmap)-blockmap, screeny-(((height+blocksBelow0)*blockmap)-(blockmap*1))))
              waterfog.setFill(oceancol)
              waterfog.setOutline(oceancol)
              waterfog.draw(display)
              EnverPlace(xpos, sealevel, "minecraft:water", 1, 1)
        xpos = xpos + 1
          # Calculate Height Change
          # First Determine if we want to take the height step.
        if num < 10:
              try:
                datasqu = json.load(open("open//data//{}//worldgen//biome//{}.json".format(nextbiome.split(":")[0],nextbiome.split(":")[1]), "r"))
              except:
                datasqu = json.load(open("default//data//{}//worldgen//biome//{}.json".format(nextbiome.split(":")[0],nextbiome.split(":")[1]), "r"))
              depthMapping = datasqu["depth"]
              scaleMapping = datasqu["scale"]
              # Here, We present the new biome system- introduced in 0.2.0
              forcetop = settingSurfaceLevel + ((depthMapping*10)+(round(scaleMapping*4)+5))
              naturaltopy = settingSurfaceLevel + ((depthMapping*10)+(round(scaleMapping*3)+3))
              naturalbottomy = settingSurfaceLevel + ((depthMapping*10)+(round(scaleMapping*3)-3))
              forcebottom = settingSurfaceLevel + ((depthMapping*10)+(round(scaleMapping*4)-5))
        if height < forcebottom:
            height = height + 1
        elif height > forcetop:
            height = height - 1
        elif random.randint(0, 100) > smoothness:
            print("Height Change")
            if height > naturaltopy:
              height = height - random.randint(0,1)
            elif height < naturalbottomy:
              height = height + random.randint(0,1)
            else:
              height = height + random.randint(-1, 1)
      # Do Stone
      num = size
      virtualisedxpos = xpos - size
      while num > 0 and settingCavesenabled == "True":
        #global virtualisedxpos
        #global cavedraw
        num = num-1
        height = biomeheightmap[virtualisedxpos]
        print("Cave Height:", biomeheightmap[virtualisedxpos])
        # Run through Cave
        cavedraw = height-5
        while cavedraw > 0:
          if settingCavesenabled == "True":
            if cavedata["system"] == "default":
              #cavedraw = cavedraw-1
              EnverPlace(virtualisedxpos, cavedraw, cavedata["block"], 1, 0+biomeheightmap[virtualisedxpos])
              #runfeature(random.choice(cavedata["AlwaysDo"]), virtualisedxpos, cavedraw)
              cavedraw = cavedraw-biomeheightmap[virtualisedxpos]
            if cavedata["system"] == "plateau":
              #cavedraw = cavedraw-1
              EnverPlace(virtualisedxpos, cavedraw, surafac[str(cavedraw-1)], 1, 1)
              #runfeature(random.choice(cavedata["AlwaysDo"]), virtualisedxpos, cavedraw)
              cavedraw = cavedraw-1
        virtualisedxpos = virtualisedxpos + 1
      # Do Features
      num = size
      virtualisedxpos = xpos - size
      while num > 0 and settingFeaturesInCaves == "True":
        #global virtualisedxpos
        #global cavedraw
        num = num-1
        height = biomeheightmap[virtualisedxpos]
        print("Cave Height:", biomeheightmap[virtualisedxpos])
        # Run through Cave
        if surafac["system"] == "default":
          cavedraw = height-5
        if surafac["system"] == "plateau":
          cavedraw = height-9
        while cavedraw > 0:
          if settingFeaturesInCaves == "True":
            if cavedata["system"] == "default":
              #cavedraw = cavedraw-1
              #EnverPlace(virtualisedxpos, cavedraw, cavedata["block"], 1, 0+biomeheightmap[virtualisedxpos])
              if not random.choice(cavedata["AlwaysDo"]) == "nothing":
                runfeature(random.choice(cavedata["AlwaysDo"]), virtualisedxpos, cavedraw)
              #cavedraw = cavedraw-biomeheightmap[virtualisedxpos]
            if cavedata["system"] == "plateau":
              #cavedraw = cavedraw-1
              #EnverPlace(virtualisedxpos, cavedraw, surafac[str(cavedraw-1)], 1, 1)
              if not random.choice(cavedata["AlwaysDo"]) == "nothing":
                runfeature(random.choice(cavedata["AlwaysDo"]), virtualisedxpos, cavedraw)
              #cavedraw = cavedraw-1
          cavedraw = cavedraw-1
        virtualisedxpos = virtualisedxpos + 1
      num = size
      virtualisedxpos = xpos - size
      while num > 0 and settingFeaturesOnSurface == "True" and stopScript == 0:
        #global virtualisedxpos
        #global biomefeatures
        #global cavedraw
       num = num-1
       height = biomeheightmap[virtualisedxpos]
       print("Cave Height:", biomeheightmap[virtualisedxpos])
       i = 0
       cancelOut  = [
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0
       ]
       while i < 5:
        # Run through surface
        i += 1
        heightPoint = random.randint(0,255)
        b = 0
        while b < 11:
          try:
            if cancelOut[b] == 0:
              cancelOut[b] = runfeature(random.choice(data["features"][b]), virtualisedxpos, random.randint(0,255))
          except:
            pass
          b += 1
       virtualisedxpos = virtualisedxpos + 1
      genopen = nextbiome
      biomechoose(display)
 
def stop():
      global stopScript
      stopScript = 1







def singFeature():
  global blockmap
  blockmap = 8
  print("hi")
  runfeature(
    object2.getText(),
    10,
    10
  )



temperature = 0.2
humidity = 0.2


nextbiome = "minecraft:plains"

object2 = 0

def setupForVisualising():
  global display
  display = GraphWin("Stargen- World Generator", screenx, screeny)
  display.setBackground(settingSkyColor)
  singleFeature = tkinter.Button(display, text = "Single Feature", command=singFeature)
  nameSpace = Entry(Point(230, 63), 20)
  nameSpace.draw(display)

  object2 = Entry(Point(415, 63), 20)
  object2.draw(display)
  singleFeature.place(x=50, y=50)
  debugButton = Button(display, text="Start Debugging", command=debug)
  bootButton = Button(display, text="Generate Next Biome", command=inis)
  stopButton = Button(display, text="- Stop", command=stop)
  bootButton.place(x=0, y=0)
  debugButton.place(x=300, y=0)
  stopButton.place(x=350, y=0)



pata = json.load(open("datafile//choosertag//{}.json".format(choosertag), "r"))

root = Tk()



frame=Frame(root,width=1,height=1)
canvas=Canvas(frame,bg='#FFFFFF',width=1,height=1)

hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM)
hbar.config(command=canvas.xview)
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width=1,height=1)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=False)



setupForVisualising()
screen = TurtleScreen(canvas)
turtle = RawTurtle(canvas)
  #global root
root.wm_title("Welcome to MineVis")
root.geometry("300x700")
frame=Frame(root,width=1,height=1)
frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
canvas=Canvas(frame,bg='#FFFFFF',width=1,height=1)
print(canvas.winfo_pointerxy())
print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
#screen.setworldcoordinates(0,-0,1280,720)
# Block Images
openbiome()
root.mainloop()