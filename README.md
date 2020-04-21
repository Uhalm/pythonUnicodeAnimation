# unicodeAnimation
This is a python library for animating unicode and ascii stored in text files. 
If you wish to use a image use a JPEG to Text converter and paste it in a text file.

# Syntax
import animation

animation.anime(filesList, sleepTime, clearCommand)

# Example Code

import animation

frames = ["frame1.txt", "frame2.txt", "frame3.txt"] #a list of files holding each frame

clear = 'clear' #the clear command for the operating systems terminal

sleepTime = 1 #the time between frames

animation.anime(frames, sleepTime, clear)
