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
    frame, val = player.get_frame()

    
    if val != 'eof' and frame is not None:
        img, t = frame
        # display img
        
        w = img.get_size()[0] 
        h = img.get_size()[1]
        arr = np.uint8(np.asarray(list(img.to_bytearray()[0])).reshape(h,w,3)) # h - height of frame, w - width of frame, 3 - number of channels in frame

        cv2.imshow('VideoHDR', arr)
        k =  cv2.waitKey(1)
        if k == 27:
            break  # esc to quit
        if k == 32:
            #space to pause
            while cv2.waitKey(1) != 32:
                pass