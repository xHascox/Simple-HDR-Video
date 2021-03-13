import cv2
import numpy as np
import tkinter
from tkinter.filedialog import askopenfilename
from ffpyplayer.player import MediaPlayer
import time
filename = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("matroska files","*.mkv"),("all files","*.*")))

cv2.namedWindow('VideoHDR',cv2.WINDOW_NORMAL)

ff_opts={'an':True, 'sync':'video'}
#player = MediaPlayer(filename, ff_opts=ff_opts)
player = MediaPlayer(filename)
val = ''
while val != 'eof':
    #frame, val = player.get_frame()

    k =  cv2.waitKey(1)
    if k == 27:
        break  # esc to quit
