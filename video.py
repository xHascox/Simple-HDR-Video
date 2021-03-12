import cv2
import tkinter
from tkinter.filedialog import askopenfilename

def play_videoFile(filePath,mirror=False):
    cap = cv2.VideoCapture(filePath)

    

    cv2.namedWindow('Video Life2Coding',cv2.WINDOW_AUTOSIZE)
    while True:
        ret_val, frame = cap.read()
        if mirror:
            frame = cv2.flip(frame, 1)
        cv2.imshow('Video Life2Coding', frame)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()
def main():
    filename = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("matroska files","*.mkv"),("all files","*.*")))
    play_videoFile(filename,mirror=False)
if __name__ == '__main__':
    main()