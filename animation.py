import time;
import os;

frames = " "
logoAnimation = ["frame1.txt", "frame2.txt", "frame3.txt", "frame4.txt", "frame5.txt", "frame6.txt", "frame8.txt"]
frames = []


def anime(fileName, sleepTime, clear):
	for name in fileName:
		with open(name,"r",encoding="utf8") as f:
			frames.append(f.readlines());

	for frame in frames:
		print("".join(frame));
		time.sleep(sleepTime);
		os.system(clear);
