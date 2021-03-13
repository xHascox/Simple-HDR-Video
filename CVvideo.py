import cv2
import tkinter
from tkinter.filedialog import askopenfilename

def play_videoFile(filePath,mirror=False):
    cap = cv2.VideoCapture(filePath)

    #modify:
    
    width = 1920
    height = 1080
    

    #cv2.namedWindow('VideoHDR',cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('VideoHDR',cv2.WINDOW_NORMAL)



    while True:
        ret_val, frame = cap.read()
        if mirror:
            frame = cv2.flip(frame, 1)
        cv2.imshow('VideoHDR', frame)


        k =  cv2.waitKey(1)
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