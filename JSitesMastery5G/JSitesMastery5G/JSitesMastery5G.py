#computer vision library
import cv2

#name the window
cv2.namedWindow("Mastery5G")
#set variable to video capture
vc = cv2.VideoCapture(0)
#rval is tracker for window if opened
if vc.isOpened(): #try to get first frame
    rval, frame = vc.read()
else:
    rval = False
while rval:
    #any operations on the frame come to imshow
    #while open push frame into the window
    cv2.imshow("Mastery5G", frame)
    rval, frame = vc.read()
    #read keys
    #what key is pressed
    key = cv2.waitKey(20)

    #look for space key...ascii value is 32
    if key == 32: #save on Space
        cv2.imwrite("mypicture.jpg", frame)

    #look for escape key...ascii value is 27
    if key== 27: #exit on Esc
        break

#after breaking out of loop
cv2.destroyWindow("Mastery5G")