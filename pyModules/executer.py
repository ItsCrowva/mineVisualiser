
#
#   StarScript Executer
#
#
#   0.0.7:    20-10-21 - 12:38pm until 3:03pm
#   0.0.7.1:  20-10-21 - 3:03pm until 4:41pm
#   0.0.7.2:  20-10-21 - 4:42pm until 5:59pm
#             20-10-21 - 8:54pm until 9:02pm
#             21-10-21 - 10:19am until 11:15am BECAUSE OF A FUCKING SCHOOL LOCKDOWN!!
#             21-10-21 - 1:23pm until 2:55pm
#             21-10-21 - 8:21pm until 9:00pm
#             22-10-21 - 10:20am until 11:20am
#             25-10-21 - 8:38am until 8:57am
#   0.0.7.3:  25-10-21 - 8:57am until 12:42pm
#   0.0.8:    25-10-21 - 12:42pm until 2:15pm
#             25-10-21 - 4:36pm until 6:00pm
#   0.0.8.1:  26-10-21 - 9:35am until 10:00am
#             27-10-21 - 9:30am until 12:56pm
#   0.0.9:    27-10-21 - 12:59pm until 1:15pm
#             27-10-21 - 2:42pm until 2:55pm
#             27-10-21 - 9:07pm until 10:11pm
#   0.0.9.1:  27-10-21 - 10:12pm until 10:36pm
#             28-10-21 - 10:26am until 11:20pm
#             28-10-21 - 1:58pm until 2:18pm
#   0.0.9.2:  28-10-21 - 2:18pm until 3:00pm
#             1-11-21  - 8:54am until 10:06am
#   0.0.9.3:  1-11-21  - 10:31am until 3:00pm
#   0.0.10:   1-11-21  - 5:16pm until 6:00pm
#             1-11-21  - 6:57pm until 8:27pm
#   0.0.10.1: 1-11-21  - 8:27pm until 10:19pm
#   0.0.10.2: 2-11-21  - 12:34pm until 1:15pm
#             2-11-21  - 7:56pm until 9:00pm
#             3-11-21  - 9:42am until 11:20am
#             3-11-21  - 12:40pm until 1:00pm
#   0.0.10.3: 3-11-21  - 1:04pm until 2:30pm
#             4-11-21  - 10:28am until 11:20am
#   0.0.10.4: 8-11-21  - 10:01am until 10:04am
#             17-11-21 - 11:33am until 11:45am
#   0.0.11:   18-11-21 - 4:38pm until 5:30pm
#   0.0.11.1: 20-11-21 - 5:30pm until 6:00pm
#             20-11-21 - 7:20pm until 8:30pm
#             22-11-21 - 9:19am until 3:00pm
#   0.0.12:   22-11-21 - 4:44pm until 6:16pm
#             23-11-21 - 11:35am until
#            

#   0.0.1
#       Lets start work.
#       All opens are from the scripts location.
#
#       Added a module system!
#       Going pretty well! As of 0.0.1 you can-
#           - import modules
#           - define functions
#           - print to console
#           - return from functions
#       I plan to bring console input and the ability to open other strscr files!
#       
#   0.0.2:
#           - dotPassoff module
#           - You can now run code in code with basic.openStrScr
#           - VariPro module
#           - Variable set (0 to 10)
#           - Ability for console.print to send varipro variable input
#           - You can now change variable values!
#   0.0.3:
#       For 0.0.3 I plan to add displays and keyboard/button/mouse input!
#           - dotpassoff Sendoff now logs values from before
#           - dotpassoff now has a return to previous script commad (dotPassoff.returnscript;)
#             This allows you to use the effects of the now broken StrScr in-script simulation (openStrScr)
#             While also allowing you to pick up where you left off! On top of this- Variables stay between scripts- therefor you can have setup scripts!
#           - dotDisplay module
#           - Various config functions
#           - a function button window with a debug button
#           - proInput module
#           - dotPassoff no longer resets modules
#   0.0.4:
#       Lets improve dotDisplay and allow drawing!
#           - proInput function 2
#       *not me just spending 4 hours in a hospital emergency room.*
#           - proInput function 3
#           - proInput function 4
#           - ifMap module
#           - smartConvert Module
#           - Changed Console Modules, Print function to use the smartConvert module to display different types of inputTypes
#           - variPro now automatically selects the variable upon variable creation
#       
#       YESS- FUCK YOU ALL! I DID IT- I FUCKING DID IT- NO MORE GLITCHES IN ifMAP IN BOOTLOADER.
#       8:48pm BIGGEST ISSUE OF 0.0.4 SOLVED- MOTHERFUCKERS!
#       
#           - variPro now uses the smartConvert system
#           - dotDisplay can now draw things to screen
#   0.0.5:
#       StarLang 2 - This is the focus.
#           changelog:
#          0.0.5:
#           - "base." has been taken off base.import and base.strscr.preque
#           - dotDisplay.drawToDisplay now uses a parameter system as opposed to setting it's values beforehand!
#           IfMap If statement is next goal! this'll simplify A LOT
#           - If Statements now use a paremeter system!
#           - If Statements now support >
#           - If Statements now support <
#           - If Statements now support !==
#          0.0.5.1:
#           I've split the update so I can do the {} system! I have a slight feeling this could break things so- This is a just-in-case
#           - Functions redone-
#           - Time Module
#           - Single Line Star Script Executions are now possible!
#           - New StarScript Shell python file!
#   0.0.7:
#       We're gonna rewrite the entire thing! This should hopefully make it easier to improve and bug fix.
#
#       StarLang 3 - Yes! Another language revision. This will be compared to Starlang 2 and the broken af 0.0.6.
#           - smartConvert will no longer be a module- and be part of the system base.
#           - variPro will no longer be a module- and be part of the system base.
#           - Console will no longer be a module and be part of the system base.
#           - dotPassoff will no longer be a module and be part of the system base.
#           - The Base Modules edition of smartConvert has the types:
#               - String (String)
#               - Str (String)
#               - Int (Integer)
#               - Float (Float)
#               - List (List)
#           - The Base Modules edition of Print now has the : taken off of it to align with StarLang 3
#               Furthermore, you can specify multiple smartconvert objects to have a joint print! py: print("hello", "hello again!") str: print str("hello"), str("hello again!");
#           - the scripts in Functions are now stored in their own list!
#               This means functions can be saved and executed in other scripts! (once script passing is available!!!)
#   0.0.7.1:
#       Continuing on from the 0.0.7 rewrite! (this is just to act as a save point!!!)
#           - We've accidently fixed- um... well... we've completely accidently readded openStrScr. Script Passing is NOT possible at this time.
#               We now have "simScript" which runs the given script once, before returning back to the previous script-
#               I don't think there is an easy way to readd the dotPassoff Sendoff with how the current system is built... this is upsetting ;-;
#               This will probably cause numerous issues but- ig- for now- this works..
#
#                   We've decided to keep simScript for setting setup types of star scripts.
#
#                   We do wanna add a full on send off command-
#
#           - newScript command- to fully sendoff to a new script
#   0.0.7.2:
#       Continuing on with the 0.0.7 rewrite! (THIS IS SAVE POINT >: )
#           - ifMap is no longer a module and now part of base
#           - proInput is deprecated. Something else will replace it!
#           - dotDisplay has been added!
#           - If has been added and is working
#           - varipro() is now var()
#           - Base's smartConvert now allows "" for string and numbers for int!
#           - dotDisplay drawing now uses smartConvert
#           - new drawInBound dotDisplay command
#   0.0.7.3:
#       CONTINUING ):<
#           - Better Error Messages(literally much better.)
#           - Function Variables! (equal to arguments)
#           - Better List Support
#   0.0.8:
#       Okay- I wanna redo list support!
#   0.0.8.1:
#           - We're gonna actually go full speed ahead into error messages :P
#   0.0.9:
#     ok so um- we're gonna- umm... try to increase the performance of graphics.py- or use a new system.
#           - New Command to set two variables to mouse position
#     2:42pm- TWTC just got attacked. Lost nearly 500 members due to a helper.
#           - The Executer now needs to be ran as a script and not a module to show any input stuff or anything.
#           - New Command editorConfigs() for use in other executors!
#   0.0.9.1:
#     touchpads would be cool... lets work on them-
#
#     harder than i thought.
#   0.0.9.2:
#     Reworking the "If" System
#     
#     It's the 1st of November... I HAVE FINALLY GOT IF STATEMENTS WORKING AGAIN :P
#     After the cancelation of }.if;
#     it would set the ifvalue to 0 instead of -1.
#     If statements would then set that to 1 when if it's a single if it should be set to 0 for a -1 end.
#     (complicated but) point is- we finally fucking fixed it!
#   0.0.9.3:
#     Making Integrated Mouse Pointer support for arrow keys and starvms mousepad
#     This comes in it's own module!
#        - Starting work on ability to draw images!
#   0.0.10:
#        OS module will be coming this update- but first! better bootLoader!
#        - Anchoring to Edge Of Screen!
#   0.0.10.2:
#     We're redoing Belver for a lower resolution! & Changing it, again, to a refreshing system
#     well... trying to
#   0.0.10.3:
#     Lets- well... lets start work on the os module!
#     well... still barely any work.
#     work has mostly been done on belverOS
#     We aaarrreee now going to make the shortKey language
#   0.0.10.4:
#     Data Pack Support! - no. nevermind
#   0.0.11:
#     starLang 4 !! codebase 3!! REWRITE
#   0.0.11.1:
#     maybe displays ??- actually- functions first!
#
#
#     Functions done, If done, Displays done and more!
#   0.0.12
#     well i might be getting suspended soon so-

#     ANYWAYS- Variables in codebase 3- and json
import inspect
import os
import time
import sys
import json
import tkinter
import random
from turtle import fillcolor, left, mode, pos, position, screensize

from graphics import *
from specflags import *

debugMode = 0
positiveExecution = 0
currentModules = [
  "internal"
]
exInformation = []
scriptLevel = -1

variableID = [] # For Finding
variableList = [] # For Storing

def bubbleToValue(
  bubble,
  flags
  ):
  bubble = bubble.replace(" xdr", "xdr", 1)
  bubble = bubble.replace(" str", "str", 1)
  bubble = bubble.replace(" string", "string", 1)
  bubble = bubble.replace(" int", "int", 1)
  bubble = bubble.replace(" bjh$", "bjh$", 1)
  bubble = bubble.replace(" var", "var", 1)
  if bubble.startswith('-') or bubble.startswith('0') or bubble.startswith('1') or bubble.startswith('2') or bubble.startswith('3') or bubble.startswith('4') or bubble.startswith('5') or bubble.startswith('6') or bubble.startswith('7') or bubble.startswith('8') or bubble.startswith('9'):
    return int(bubble)
  if bubble.startswith(" "):
    bubble = bubble.replace(" ", "", 1)
  # Convert a bubble such as str() to "string"
  if bubble.startswith("var("):
    bubble = bubble.replace("var(", "", 1)
    # Remove final dollar sign / end bracket
    bubble = list(bubble)
    bubble[len(bubble)-1] = ""
    bubble = "".join(bubble)
    # Return Var
    indexMap = variableID.index(bubble)
    return variableList[indexMap]
  if bubble.startswith("hex(") or bubble.startswith("hel$"):
    bubble = bubble.replace("hex(", "")
    bubble = bubble.replace("hel$", "")
    
    # Remove final dollar sign / end bracket
    bubble = list(bubble)
    bubble[len(bubble)-1] = ""
    bubble = "".join(bubble)
    #print(bubble)
    hex = bubble.lstrip('#')
    #print(tuple(int(hex[i:i+2], 16) for i in (0, 2, 4)))
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
  if bubble.startswith("brand(") or bubble.startswith("bjh$"):
    return flags[5]
  if bubble.startswith("str(") or bubble.startswith("string(") or bubble.startswith("xdr$"):
    bubble = bubble.replace("str(", "")
    bubble = bubble.replace("xdr$", "")
    bubble = bubble.replace("string(", "")
    # Remove final dollar sign / end bracket
    bubble = list(bubble)
    bubble[len(bubble)-1] = ""
    bubble = "".join(bubble)
    return str(bubble)
  if bubble.startswith("int(") or bubble.startswith("integer(") or bubble.startswith("has$"):
    bubble = bubble.replace("int(", "")
    bubble = bubble.replace("has$", "")
    bubble = bubble.replace("integer(", "")
    # Remove final dollar sign / end bracket
    bubble = list(bubble)
    bubble[len(bubble)-1] = ""
    bubble = "".join(bubble)
    return int(bubble)


ifHead = -1

functionsScript = [] # Holding Functions ^^
functionID = []
functionNumber = -1

modFunctionsScript = [] # Holding Functions ^^
modFunctionID = []
modFunctionNumber = -1

displayFillColor = 9

currentDisplay = 0

def moduleInternal(
  codeString,
  flags
  ):
  global currentModules
  global positiveExecution
  global functionID
  global functionNumber
  global functionsScript
  global modFunctionID
  global modFunctionNumber
  global modFunctionsScript
  global scriptLevel
  global exInformation
  global ifHead
  global displayFillColor
  global variableID
  global variableList
  global currentDisplay
  if codeString.startswith("internal.forcewords.info"):
    print(
      "Internal Module Information",
      positiveExecution,flags
    )
  if debugMode == 1 and flags[0] == "normal": print("base > Base Module Testing", codeString)
  if flags[0] == "if":
    if codeString.startswith("if") or codeString.startswith("$ "):
      ifHead += 1
    if codeString.startswith("}.if;"):
      ifHead -=1
      if ifHead == -1:
        flags[0] = "normal"
    return flags
  if flags[0] == "moduledef":
    if codeString.startswith("}.ba;"):
      flags[0] = "normal"
      positiveExecution = 1
    else:
      modFunctionsScript[modFunctionNumber].append(codeString)
      positiveExecution += 1
  if flags[0] == "def":
    if codeString.startswith("}.ba;"):
      flags[0] = "normal"
      positiveExecution = 1
    else:
      functionsScript[functionNumber].append(codeString)
      positiveExecution += 1
  if flags[0] == "normal":
   if codeString.startswith("changeVariable"):
     codeString = codeString.replace("changeVariable ", "")
     codeString = codeString.replace(";", "")
     codeString = codeString.split(",")
     codeString[1] = codeString[1].replace(" ", "")
     if codeString[1] == "+":
       findMap = variableID.index(codeString[0])
       variableList[findMap] += bubbleToValue(codeString[2], flags)
     if codeString[1] == "-":
       findMap = variableID.index(codeString[0])
       variableList[findMap] -= bubbleToValue(codeString[2], flags)
     if codeString[1] == "*":
       findMap = variableID.index(codeString[0])
       variableList[findMap] *= bubbleToValue(codeString[2], flags)
     if codeString[1] == "/":
       findMap = variableID.index(codeString[0])
       variableList[findMap] /= bubbleToValue(codeString[2], flags)
     codeString = "None"
   if codeString.startswith("createVariable"):
     codeString = codeString.replace("createVariable ", "")
     codeString = codeString.replace(";", "")
     codeString = codeString.split(",")
     variableID.append(codeString[0])
     variableList.append(bubbleToValue(codeString[1], flags))
     codeString = "None"
   if codeString.startswith("drawSimpleSquare"):
     codeString = codeString.replace("drawSimpleSquare ", "")
     codeString = codeString.replace(";", "")
     codeString = codeString.replace(" ", "")
     codeString = codeString.split(",")
     print("0/5")
     o1 = bubbleToValue(codeString[0], flags)
     o2 = bubbleToValue(codeString[1], flags)
     t1 = bubbleToValue(codeString[2], flags)
     t2 = bubbleToValue(codeString[3], flags)
     print("1/5")
     display = flags[4][currentDisplay][2]
     print("2/5")
     screenX = display.getWidth()
     screenY = display.getHeight()
     print("3/5")
     drawObject = Rectangle(
              Point(
                ((screenX * o1) / flags[4][currentDisplay][0]), 
                ((screenY * o2) / flags[4][currentDisplay][1])
              ), 
              Point(
                ((screenX * (o1 + t1)) / flags[4][currentDisplay][0]), 
                ((screenY * (o2 + t2)) / flags[4][currentDisplay][1])
              )
            )
     color = color_rgb(
       round(int(displayFillColor[0])/(flags[4][currentDisplay][3]))*(flags[4][currentDisplay][3]),
       round(int(displayFillColor[1])/(flags[4][currentDisplay][3]))*(flags[4][currentDisplay][3]),
       round(int(displayFillColor[2])/(flags[4][currentDisplay][3]))*(flags[4][currentDisplay][3])
     )
     print(color)
     drawObject.setFill(color)
     drawObject.setWidth(0)
     print("4/5")
     drawObject.draw(display)
     print("5/5")
     codeString = "None"
   if codeString.startswith("drawSquare"):
     codeString = codeString.replace("drawSquare ", "")
     codeString = codeString.replace(";", "")
     codeString = codeString.replace(" ", "")
     codeString = codeString.split(",")
     print("0/5")
     o1 = bubbleToValue(codeString[0], flags)
     o2 = bubbleToValue(codeString[1], flags)
     t1 = bubbleToValue(codeString[2], flags)
     t2 = bubbleToValue(codeString[3], flags)
     print("1/5")
     display = flags[4][currentDisplay][2]
     print("2/5")
     screenX = display.getWidth()
     screenY = display.getHeight()
     print("3/5")
     drawObject = Rectangle(
              Point(
                ((screenX * o1) / flags[4][currentDisplay][0]), 
                ((screenY * o2) / flags[4][currentDisplay][1])
              ), 
              Point(
                ((screenX * t1) / flags[4][currentDisplay][0]), 
                ((screenY * t2) / flags[4][currentDisplay][1])
              )
            )
     color = color_rgb(
       round(int(displayFillColor[0])/(flags[4][currentDisplay][3]))*(flags[4][currentDisplay][3]),
       round(int(displayFillColor[1])/(flags[4][currentDisplay][3]))*(flags[4][currentDisplay][3]),
       round(int(displayFillColor[2])/(flags[4][currentDisplay][3]))*(flags[4][currentDisplay][3])
     )
     print(color)
     drawObject.setFill(color)
     drawObject.setWidth(0)
     print("4/5")
     drawObject.draw(display)
     print("5/5")
     codeString = "None"
   if codeString.startswith("changeSimRange") or codeString.startswith("tesca"):
     codeString = codeString.replace("changeSimRange ", "")
     codeString = codeString.replace("tesca", "")
     codeString = codeString.replace(";", "")
     codeString = codeString.replace(" ", "")
     codeString = codeString.split(",")
     #, codeString)
     flags[4][currentDisplay][0] = bubbleToValue(codeString[0], flags)
     flags[4][currentDisplay][1] = bubbleToValue(codeString[1], flags)
     codeString = "NONE"
   if codeString.startswith("setFill") or codeString.startswith("gasg"):
     codeString = codeString.replace(";", "")
     codeString = codeString.replace("setFill ", "")
     codeString = codeString.replace("gasg ", "")
     displayFillColor = bubbleToValue(codeString, flags)
   if codeString.startswith("runFunc") or codeString.startswith("f>"):
     codeString.replace("f> ", "")
     codeString.replace("runFunc ", "")
     codeString.replace(";", "")
     try:
      runThroughScript(
       flags,
       0,
       functionsScript[functionID.index(codeString)]
     )
     except:
       print("fking what")
   if codeString.startswith("directRun") or codeString.startswith(":>>"):
     # directRun entry;
     codeString = codeString.replace(";", "")
     codeString = codeString.replace("directRun ", "")
     codeString = codeString.replace(":>> ", "")
     #print(codeString)
     try:
      # Set Up Variables to pick back
      exInformation.append(
        [
          modFunctionsScript,
          modFunctionID,
          modFunctionNumber,
          currentModules
        ]
      )
      scriptLevel += 1
      # Clear Variables
      modFunctionScript = []
      modFunctionID = []
      modFunctionNumber = -1
      currentModules = [
        "internal"
      ]
      # Run Through Script
      runThroughScript([
        "normal",
        "normal",
        1,
        0,
        flags[4],
        flags[5]
      ],0,open("{}.str".format(codeString), "r").readlines())
      # Restore Variables
      modFunctionScript = exInformation[scriptLevel][0]
      modFunctionID = exInformation[scriptLevel][1]
      modFunctionNumber = exInformation[scriptLevel][2]
      currentModules = exInformation[scriptLevel][3]
      exInformation.pop(scriptLevel)
      scriptLevel -= 1
     except:
      if flags[1] == "directLine":
       print("No such directory!!")
   if codeString.startswith("if") or codeString.startswith("$ "):
     if debugMode == 1: print("if: 0/5")
     codeString = codeString.replace("if ", "", 1)
     codeString = codeString.replace(";", "")
     if codeString.startswith("$"):
      codeString = codeString.replace("$ ", "",1)
     if debugMode == 1: print("if: 1/5")
     codeString = codeString.split(",")
     if debugMode == 1: print("if: 2/5")
     pointi1 = bubbleToValue(codeString[0], flags)
     if debugMode == 1: print("if: 3/5")
     floati = codeString[1].replace(" ", "")
     if debugMode == 1: print("if: 4/5")
     pointi2 = bubbleToValue(codeString[2], flags)
     if debugMode == 1: print("if:", pointi1, floati, pointi2)
     if floati == "==" or floati == "copi":
       if pointi1 == pointi2:
         positiveExecution = 1
         flags[0] = "normal"
         if debugMode == 1: print("if: Equals passed!")
       else:
         ifHead += 1
         flags[0] = "if"
     if floati == "!==" or floati == "capi":
       if not pointi1 == pointi2:
         positiveExecution = 1
       else:
         ifHead += 1
         flags[0] = "if"
     if floati == ">" or floati == "cupi":
       if pointi1 > pointi2:
         positiveExecution = 1
       else:
         ifHead += 1
         flags[0] = "if"
     if floati == "<" or floati == "cipi":
       if pointi1 < pointi2:
         positiveExecution = 1
       else:
         ifHead += 1
         flags[0] = "if"
     if debugMode == 1: print("if: 5/5")
     codeString = "none"
     return flags
   if (codeString).startswith("func") or codeString.startswith("@ "):
     codeString = codeString.replace("func ", "")
     codeString = codeString.replace(";", "")
     codeString = codeString.replace("@ ", "")
     if flags[3] == 0:
      functionID.append(str(codeString))
      flags[0] = "def"
      functionNumber = functionNumber+1
      functionsScript.append([])
      positiveExecution = 1
     if flags[3] == 1:
      modFunctionID.append(str(codeString))
      flags[0] = "moduledef"
      modFunctionNumber = modFunctionNumber+1
      modFunctionsScript.append([])
      positiveExecution = 1
   if codeString.startswith("help") or codeString.startswith("$he"):
     if codeString == "help;":
      print("""
     ===============================
     |                             |
     |   StarScript by Starcake    |
     |                             |
     ===============================

     This is a short and simple command guide for the internal module (and maybe some others)
     this is more or less dedicated for use in the command line

     however most functions should run the same either way !!!


     Please use help pageNumber;

     Pages:
     1 - Execution Flags
     """)
     else:
       codeString = codeString.replace(";", "")
       codeString = codeString.replace("help ", "")
       numString = int(codeString)
       if numString == 0:
         print("""
         Page 0 - The Example Page!

         ---------------[ Header ]
         Command
          Example: Command Example

          Explanation of command
         Command
          Example: Command Example

          Explanation of command
         Command
          Example: Command Example

          Explanation of command
         ---------------[ Footer ]
         """)
       if numString == 1:
         print("""
         Page 1 - Launch Flags!

              Please note: This page is aimed at StarPython usage.

              Examples will be given using Python.

         ---------------[ A brief explanation ]

            If you're using the Star Script executer in your own project

            That isn't 100% Starscript

            but uses some starscript components

            you might wanna look into launch flags.




            To run any line of code in Star Script just use
            runLine(YOUR CODE IN A STRING FORMAT, [runMode, executedFrom, wasInternallyExecuted])

            now what does "runMode" or "executedFrom" mean?

            Here:

         ---------------[ Options for modes ]
         runMode
          can be "normal" or "def" or "if"

          This decides whether or not certain types of code should be ran.

          You should almost always use normal

          def & if are more internal.

         executedFrom
          this can be "normal" or "directLine"

          u s u a l l y normal should do you well

          however if you want stuff like

          smaller errors such as file not found

          directLine will do the trick.


          directLine is what strscr from command line uses
         wasInternallyExecuted
          this can be 0 or 1. in my opinion it's best to use 0.

          1 is more so for functions of script changes
         ---------------[ Thank you! (page 1) ]
         """)
   if codeString.startswith("import") or codeString.startswith("$ha"):
    codeString = codeString.replace("import ", "")
    codeString = codeString.replace("$ha ", "")
    codeString = codeString.replace(";", "")
    currentModules.append(codeString)
    runThroughScript([
        "normal",
        "normal",
        1,
        1,
        flags[4],
        flags[5]
      ],0,open("{}.str".format(codeString), "r").readlines())
    positiveExecution = 1
   if codeString.startswith("print") or codeString.startswith(">>>"):
    codeString = codeString.replace("print ", "")
    codeString = codeString.replace(">>> ", "")
    codeString = codeString.replace(";", "")
    codeString = codeString.split(",")
    tickMap = 0
    totalTicks = len(codeString)
    if debugMode == 1: print(codeString)
    while not tickMap == totalTicks:
      print(convert(bubbleToValue(codeString[tickMap], flags)))
      tickMap += 1
  return flags


def runThroughScript(flags, startline, script):
  if debugMode == 1: 
    print("Ciao!! - runThroughScript")
    print("Script to run ==", script)
  currentLine = startline
  maxLines = len(script)
  while currentLine < maxLines:
    flags = runLine(
      script[currentLine],
      flags
    )
    currentLine += 1

def runAwayNSI(codeString):
  # Ticks out failures of items
  if codeString.startswith(" "):
    positiveExecution = 1

def runLine(
  codeString,
  flags
  #
  #   Flag System.
  #   [
  #   runMode - Usually "normal" - Can be "def" or "if" (execution Mode)
  #   executedFrom - Usually "normal" - can be "directLine"
  #   wasInternallyExecuted - 0 for no - 1 for yes
  #   isModuleRan - usually 0
  #   displayPort - [
  #    [
  #     simX
  #     simY
  #     physicalDisplay - usually a graphics.py object
  #     colorDepth - usually 10 (256 options for each color channel)
  #    ]
  #   ]
  #   runBrand - Put anything
  # ]
  #
  #
  ):
  global positiveExecution
  positiveExecution = 0
  # Remove dumb items
  codeString = codeString.replace("\n", "")
  codeString = codeString.replace("  ", "")
  if codeString.startswith(" "):
    codeString = codeString.replace(" ", "", 1)
  # Run away the non script items
  if positiveExecution == 0:
    runAwayNSI(codeString)
  # Run Functions as modules
  # # First split everything by space
  floatString = codeString.split(" ")
  if floatString[0] in modFunctionID:
    indexMap = modFunctionID.index(floatString[0])
    floatString = floatString.join()
    print(floatString)
  # Run the built-in modules
  if "internal" in currentModules and positiveExecution == 0:
    flags = moduleInternal(codeString, flags)
  return flags
  

  