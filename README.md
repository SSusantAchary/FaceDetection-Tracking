# FaceDetection-Tracking
HaarCascades based Face Detection and Dlib based Tracking

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




License:
Free to copy, run, play.
