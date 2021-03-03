import os
import cv2 as cv
import tkinter
from tkinter import filedialog

top = tkinter.Tk().withdraw()
Videofile=filedialog.askopenfile()
Videofile=Videofile.name
Obj1 = cv.VideoCapture(Videofile)
Dataset_path='D:\ANACONDA\pyfiles\DATASET'
os.chdir(Dataset_path)
global count
count=0 
training_set=[]
while 1:
    success, frame = Obj1.read()
    if(success==False):
        break
    else:
        training_images=("trainingdata_%d.jpg" %count)
        cv.imwrite("trainingdata_%d.jpg" % count, frame) 
        count += 1
        training_set.append(training_images)
    height, width, channels = frame.shape
print("Total %d Frames Created" %count)
print(width)
print(height)

size = (width, height)
video_name='final.mov'
training_set=training_set[::-1]
#You can change the frame rate based on your convenience
video = cv.VideoWriter(video_name,cv.VideoWriter_fourcc(*'MJPG'),30,size)

for image in training_set:
    video.write(cv.imread(os.path.join(Dataset_path, image)))

cv.destroyAllWindows()
video.release()    
cv.destroyAllWindows()

