import cv2
import numpy as np

img1=cv2.imread('14main.png',cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('14.png',cv2.IMREAD_GRAYSCALE)



sift=cv2.SIFT_create()

keypoints1, descriptors1= sift.detectAndCompute(img1, None)
keypoints2, descriptors2 =sift.detectAndCompute(img2, None)

bf=cv2.BFMatcher()

matches=bf.knnMatch(descriptors1, descriptors2, k=2)

good_matches= []
for m,n in matches:
    if m.distance <0.75 * n.distance:
    	good_matches.append(m)
	
	
	
matching_result = cv2.drawMatches(img1, keypoints1, img2, keypoints2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Show the matching result
cv2.imshow('Feature Matching Result', matching_result)
cv2.waitKey(0)
cv2.destroyAllWindows()


