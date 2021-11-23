# Initialise
from os import replace
import time
from tkinter import *
from turtle import *
from typing import Counter
import winreg
import random
import math
import json
import itertools
from graphics import *
import aspironutil

caveair = "cyan2"
caveblock = "stone"
jsonreturn = '{"caveair":"cyan2"}'

# Open Underground
def opencave(namespace, genopen):
  with open("{}//cavesystem//{}.json".format(namespace,genopen), "r") as f:
    global caveair
    global caveblock
    global jsonreturn
    data = json.load(f)
    print (data["PingFile"])
    if data["VersionFile"] == 1:
      print("VersionFile1") # Heya! Please Note- This doesn't fully mean things will work alright- PLEASE- Update Version Files to standard to ensure things don't break!
      # Things should hopefully work but- version files CAN NOT BE UPDATED TO ENSURE SUPPORT- IF A VALUE CHANGES IT INHERITS FROM THE OTHER GEN FILE
      caveair = data["caveaircolor"]
      caveblock = data["block"]
      print(jsonreturn)
      pass
  pass

opencave("datafile","default")