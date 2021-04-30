# Skin_Tone_Classifier

The motive of this model is to classify the skin tone into three broad categories :
Fair, mild and dark.

The repository contains three files - module 1 , module 2 and module 3 and the face haarcascade that has been used.

Module 1:
This module detects the face in the input image and saves the facial portion as  file in the same working directory.

Module 2:
This module uses Face.jpg (from module 1) and detects only the skin area in the image and saves that as detectedImage.png in the working directory.

Module 3:
This is the final module which uses the detectedImage.png (from module 2) and detects the color of the skin converts into Hex codes and later to decimals and finally on the basis of the color range provided, it classifies into the three categories. 
