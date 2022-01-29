import cv2
img = cv2.imread('img\\ss.png')
 
cv2.rectangle(img, (1630, 85), (1910, 130), (0, 255, 0))
# cv2.rectangle(img, (120, 120), (150, 150), (255, 0, 0), 5)
# cv2.rectangle(img, (200, 200), (300, 400), (0, 0, 255), -1)
 
 
cv2.imshow('image', img)
  
cv2.waitKey(0)
cv2.destroyAllWindows()