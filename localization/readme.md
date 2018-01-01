Used OpenCv (SURF algorithm) for localization, based off of https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_surf_intro/py_surf_intro.html.

localizationPeggy.py uses SURF to find keypoints, and RectArrayFunction.py is a function that's able to take an argument of the KeyPoints object and returns an array of Rectangles (an object, will be explained below). localizationTestPeggy.py is a scripted testing that's able to go through the whole process of finding keypoints of an image and calls the RectArray function, and draws the rectangles directly on top of the image for testing purposes.

A rectangle object has 4 class variables: x, y, length, width.
x and y correspond to the top left corner of the returned rectangle object.
