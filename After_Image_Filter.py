import cv2
import  numpy as np
zer = np.zeros([720,1280,3],np.uint8)
def add_frame(frame,li):
    i = 0
    while(i<len(li)-1):
        li[i] = li[i+1]
        i = i+1
    li[-1] = frame
    
def final_img(li):
    j=0
    final_img = np.zeros([720,1280,3],np.uint8)
    while(j<len(li)):
        temp = (li[j]*(((j+2)/2)*0.1)).astype(np.uint8)
        final_img = cv2.add(final_img,temp)
        j += 2
    return final_img
def videocap():
    vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    vid.set(3, 1280)
    vid.set(4, 720)
    li = [zer,zer,zer,zer,zer,zer,zer]
    while(True):
        red , frame = vid.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray1 = cv2.medianBlur(frame, 5)
        add_frame(gray1,li)
        #final_img = (li[0]*0.1 + li[1]*0.2 + li[2]*0.3 + li[3]*0.4 + li[4]*0.5 + li[5]*0.6 + li[6]*0.7 + li[7]*0.8 + li[8]*0.9).astype(np.uint8)
        cv2.imshow("frame", final_img(li))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
videocap()

    
