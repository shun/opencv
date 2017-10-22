import cv2
import numpy as np
import sys
from PIL import Image


class narerundar:
    layer1 = None
    layer2 = None
    im = None

    def __init__(self):
        self.layer1 = None
        self.layer2 = None
        im = None

    def runNarerundar(self):

        windowname = "Narerundar"
        cv2.namedWindow(windowname, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(windowname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.waitKey(1);
        cv2.setWindowProperty(windowname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
        cv2.namedWindow(windowname)
        #cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')  # 顔認識用の特徴量
        #cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_smile.xml')  # 顔認識用の特徴量
        cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')  # 顔認識用の特徴量
        #cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml')  # 顔認識用の特徴量
        #cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt_tree.xml')  # 顔認識用の特徴量
        #cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_extended.xml')  # 顔認識用の特徴量
        #cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')  # 顔認識用の特徴量

        cam = cv2.VideoCapture(0)
        overlayframe = cv2.imread('./img/build.png', cv2.IMREAD_UNCHANGED)
        #overlayframe = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)
        self.layer2 = Image.fromarray(overlayframe)

        framecnt = 0
        sz = None

        while True:
            ret, frame = cam.read()
            w = frame.shape[0]
            h = frame.shape[1]

            if not ret:
                print('error?')
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.resize(gray, (int(frame.shape[1]/4), int(frame.shape[0]/4)))

            faces = cascade.detectMultiScale(gray)

            if len(faces) > 0:
                self.layer1 = Image.fromarray(np.uint8(frame)).convert('RGBA')
                layerc = Image.new('RGBA', (h,w), (0,0,0,0))

                for rect in faces:
                    rect *= 4

                    if((rect[2]<0) or (rect[3] < 0)):
                        continue

                    zoom = 2
                    vratio = int(rect[2] * zoom) / self.layer2.height
                    sz = (int(rect[2] * zoom), int(rect[3] * vratio))
                    coord = list(rect)
                    coord[2] = coord[0] + coord[2]
                    coord[3] = coord[1] + coord[3]

                    tmp = self.layer2.resize(sz)
                    layerc.paste(tmp, (coord[0] - int(rect[2]/zoom), coord[1] - int(rect[3]/zoom)), tmp)

                im = Image.alpha_composite(self.layer1, layerc)
                cv2.imshow(windowname, np.asarray(im))

            else:
                cv2.imshow(windowname, frame)

            if cv2.waitKey(10) > 0:
                break


        cam.release()
        cv2.destroyWindow(windowname)

if __name__ == '__main__' :
    runNarerundar()

