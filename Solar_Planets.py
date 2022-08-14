import cv2

img = []

cv2.imread("solar-system.jpg")

cv2.imshow("output",img)

cv2.waitkey(0)

cv2.putext(img, "Sun", (20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putext(img, "Mercury", (40,300), cv2.FONT_HEYSHEY_CONPLEX, 0.5, (255,255,255))

cv2.putext(img, "Venus", (60,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putext(img, "Earth", (60,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putext(img, "Mars", (80,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putext(img, "Jupiter", (100,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putext(img, "Saturn", (120,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putext(img, "Uranus", (140,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putext(img, "Neptune", (160,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.imwrite("Solar_systemWithName.jpg",img)
