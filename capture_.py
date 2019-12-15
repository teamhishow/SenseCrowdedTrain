#!/usr/bin/env python3
# -*-coding: utf-8 -*-

#WNC:We need to comment out.

import cv2
import time
import numpy as np

SENSING_TIME = 10
NEXT_SENSING_TIME = 30

def main():
    cv_dir = './haarcascades/'
    face_cascade_path = cv_dir + 'haarcascade_frontalface_default.xml'
    eye_cascade_path = cv_dir + 'haarcascade_eye.xml'

    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

    #src = cv2.imread('data/src/lena_square.png')
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    crowd = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret:
            src_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(src_gray)
                
            if (time.time()-start_time)%NEXT_SENSING_TIME <SENSING_TIME:
                for x, y, w, h in faces:
                    print('face detection!!',time.time()-start_time)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    face = frame[y: y + h, x: x + w]
                    face_gray = src_gray[y: y + h, x: x + w]
                    eyes = eye_cascade.detectMultiScale(face_gray)
                    print(h,w)
                    crowd = max(crowd,h+w)
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                record = True
            else:
                if record:
                    print(crowd)
                    output = str(crowd)
                    file = open('log.txt','w')
                    file.write(output)
                    file.close()
                    crowd = 0
                record = False

            #cv2.imshow('frame', frame)#WNC
            #cv2.imwrite('img.png', frame)
            
        else:
            time.sleep(2)

        # Display the resulting frame
        #if cv2.waitKey(20) == 27:#WNC
        #    break#WNC

    # When everything done, release the capture
    cap.release()
    #cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
