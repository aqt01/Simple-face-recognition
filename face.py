import cv2
import sys

import ipdb
#ipdb.set_trace()

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)


video_capture = cv2.VideoCapture(0)

# Read a single frame from the video capture to take height, width for the vieo
ret, frame = video_capture.read()


#height , width , layers =  frame.shape

#video = cv2.VideoWriter('video.avi',-1,1,(width,height))
#video = cv2.VideoWriter('output.avi',-1, 20, (width,height))

w=int(video_capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
h=int(video_capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))
# video recorder
fourcc = cv2.cv.CV_FOURCC(*'XVID')  # cv2.VideoWriter_fourcc() does not exist
video= cv2.VideoWriter("output.avi", fourcc, 25, (w, h))




while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
     flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #cv2.imwrite('cara.jpg',frame)
        video.write(frame)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

# Save the video with only the captured faces
# When everything is done, release the capture
video_capture.release()
video.release()


cv2.destroyAllWindows()
