import cv2
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
absolute_path = os.path.join(dir_path, '..', 'org_screenshot', 'rag_out.png');
image = cv2.imread(absolute_path,0)

# cv2.imshow('image',image)

# match gaming screen with needle

# click target