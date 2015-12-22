import sys
import cv
import cv2

class FaceDetect():
    def __init__(self):
        cv2.cv.NamedWindow ("CamShiftDemo", 1)
        device = 0
        self.capture = cv2.cv.CaptureFromCAM(device)
        capture_size = (320,200)
        cv2.cv.SetCaptureProperty(self.capture, cv2.cv.CV_CAP_PROP_FRAME_WIDTH, capture_size[0])
        cv2.cv.SetCaptureProperty(self.capture, cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, capture_size[1])

    def detect(self):
        cv2.cv.CvtColor(self.frame, self.grayscale, cv2.cv.CV_RGB2GRAY)

        #equalize histogram
        cv2.cv.EqualizeHist(self.grayscale, self.grayscale)

        # detect objects
        faces = cv2.cv.HaarDetectObjects(image=self.grayscale, cascade=self.cascade, storage=self.storage, scale_factor=1.2,\
                                     min_neighbors=2, flags=cv2.cv.CV_HAAR_DO_CANNY_PRUNING)

        if faces:
            #print 'face detected!'
            for i in faces:
                if i[1] > 10:
                    cv2.cv.Circle(self.frame, ((2*i[0][0]+i[0][2])/2,(2*i[0][1]+i[0][3])/2), (i[0][2]+i[0][3])/4, (128, 255, 128), 2, 8, 0)

    def run(self):
        # check if capture device is OK
        if not self.capture:
            print "Error opening capture device"
            sys.exit(1)

        self.frame = cv2.cv.QueryFrame(self.capture)
        self.image_size = cv2.cv.GetSize(self.frame)

        # create grayscale version
        self.grayscale = cv2.cv.CreateImage(self.image_size, 8, 1)

        # create storage
        self.storage = cv2.cv.CreateMemStorage(128)
        self.cascade = cv2.cv.Load('haarcascade_frontalface_default.xml')

        while 1:
            # do forever
            # capture the current frame
            self.frame = cv2.cv.QueryFrame(self.capture)
            if self.frame is None:
                break

            # mirror
            cv2.cv.Flip(self.frame, None, 1)

            # face detection
            self.detect()

            # display webcam image
            cv2.cv.ShowImage('CamShiftDemo', self.frame)
            # handle events
            k = cv2.cv.WaitKey(10)

            if k == 0x1b: # ESC
                print 'ESC pressed. Exiting ...'
                break
                sys.exit(1)

if __name__ == "__main__":
    print "Press ESC to exit ..."
    face_detect = FaceDetect()
    face_detect.run() 