import cv2
import tkinter
from tkinter.filedialog import askopenfilename
from ffpyplayer.player import MediaPlayer
import time
import numpy as np

def play_videoFile(filename,mirror=False):
    cap = cv2.VideoCapture(filename)
    fps = cap.get(cv2.CAP_PROP_FPS)
    #modify:
    width = 1920
    height = 1080   
    #cv2.namedWindow('VideoHDR',cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('VideoHDR',cv2.WINDOW_NORMAL)
    audioplayer = MediaPlayer(filename)

    while True:
        ret_val, frame = cap.read()
        if mirror:
            frame = cv2.flip(frame, 1)
        cv2.imshow('VideoHDR', frame)

        k =  cv2.waitKey(int(1/fps*1000))
        if k == 27:
            break  # esc to quit
        if k == 32:
            #space to pause
            while cv2.waitKey(1) != 32:
                pass

    cv2.destroyAllWindows()
def main():
    filename = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("matroska files","*.mkv"),("all files","*.*")))
    play_videoFile(filename,mirror=False)
if __name__ == '__main__':
    main()