# unicodeAnimation
This is a python library for animating unicode and ascii stored in text files. 
If you wish to use a image use a JPEG to Text converter and paste it in a text file.

# Syntax
import animation

animation.anime(filesList, sleepTime, clearCommand)

# Example Code

import animation

frames = ["frame1.txt", "frame2.txt", "frame3.txt"]

clear = 'clear'

sleepTime = 1

animation.anime(frames, sleepTime, clear)
