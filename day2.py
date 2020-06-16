import cv2
cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('cvexperiment.avi', fourcc, 20, (640, 480))
while True:
    feedExists, frame = cam.read()
    greyImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Unchanged', frame)
    cv2.imshow('Modified', greyImg)
    out.write(frame)
    if(cv2.waitKey(1) == ord('q')):
        break
out.release()
cam.release()
cv2.destroyAllWindows()
