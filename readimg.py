import cv2
import matplotlib.pyplot as plt
img = cv2.imread('gengar.png', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('Gengar', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.imshow(img, cmap='gray')
plt.show()
