'''
__author__ = "Susant_Achary"
Face Detector used: Haar Cascades Face MultiDetector
https://github.com/opencv/opencv/tree/master/data/haarcascades

Tracker used: Dlib Correlation Tracker
http://dlib.net/correlation_tracker.py.html

Requirement(Tested):
===========
OpenCV - 3.4 >=
Dlib - 19.6 >=

This code presently runs fine in a stable video with people standing still and facing camera.

to execute code:
python Detect_Track.py -f /location/of/file/*.mp4
 or
python Detect-Track.py

Process flow:
1. Takes User input ie. asks for file if not takes webacam as input.
2. Detects the face in the input image.
3. Creates the Tracker objects based on number of faces detected and starts tracking.
    (Tracker has 3 imp function start_track, update(gets PSNR), get_position(predicted future location in its neighbourhood basically done image gardients))
4. Display the image with PSNR value ie. number that measures how confident the tracker is that the object is inside #get_position(). Larger values indicate higher confidence.
'''

#/usr/bin/python3

# for python 2/3 compatibility
from __future__ import print_function
import cv2
import dlib
import argparse

#link the xml file which contains the predefined value to detect face in an image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
tracker = []

def run(source):
    capture = cv2.VideoCapture(source)
    while True:
        ret, image = capture.read()
        if ret is False:
            break

        if len(tracker) == 0:
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            dF = face_cascade.detectMultiScale(frame)# returns x,y,w,h

            for face in range(0,len(dF)):
                t = dlib.correlation_tracker()
                rect = dlib.rectangle(dF[face][0], dF[face][1], dF[face][0]+dF[face][2], dF[face][1]+dF[face][3])# so four ends of rect are x, y, x + w , y+ h
                t.start_track(image,rect)
                tracker.append(t)

        else:
            for each in range(0, len(tracker)):# iterate through each tracker object updates,get_position for each and once done(overlayying of boxes) for all faces shows the image.
                psnr = tracker[each].update(image)
                pos = tracker[each].get_position()
                sX = int(pos.left())
                sY = int(pos.top())
                eX = int(pos.right())
                eY = int(pos.bottom())
                cv2.rectangle(image, (sX, sY), (eX, eY), (0, 255, 0), 2)
                cv2.putText(image, str(round(psnr,5)), (sX, sY - 15),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)

            cv2.imshow("Frame", image)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

#Driver code
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='path to video file')

    args = vars(parser.parse_args())

    if args['file']:
        source = args['file']
    else:
        source = 0 # '0' defines to start webcam as source of input and start detect and then track.

    print(__doc__)

    run(source)
