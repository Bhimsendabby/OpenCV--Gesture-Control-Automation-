import numpy as np
import messages
import whatsapp
import cv2
class haarcascade():
    @classmethod
    def call_haarcascade(cls):
        fist_cascade = cv2.CascadeClassifier('fist1.xml')
        palm_cascade = cv2.CascadeClassifier('palm.xml')
        cam = cv2.VideoCapture(0)
        run_fist = True
        run_palm = True

        while (run_fist and run_palm):
            ret, im =cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            fist = fist_cascade.detectMultiScale(gray, 1.3, 5)
            palm = palm_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in fist:
                cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
                print("fist")
                w1 = whatsapp.whats()
                w1.start()
                run_fist = False
            for (x,y,w,h) in palm:
                cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
                print("palm")
                m1 = messages.message()
                m1.start()
                run_palm = False
            cv2.imshow('im', im)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()







# import cv2
# import numpy as np
# from PIL import Image
# import pickle
#
# face_cascade = cv2.CascadeClassifier('gest.xml')
# cam = cv2.VideoCapture(0)
# #font = cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
# while True:
#     ret, im =cam.read()
#     gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#     print(gray)
#     faces=face_cascade.detectMultiScale(gray,1.3,5)
#     for(x,y,w,h) in faces:
#         cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
#        #  Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
#        #  if (conf < 50):
#        #      if (Id == 1):
#        #          Id = "BHIM SEN"
#        #      elif (Id == 2):
#        #          Id = "BHIM "
#        #      elif (Id == 3):
#        #          Id = "GAGAN "
#        #  else:
#        #      Id = "Unknown"
#        #  #cv2.putText(im, "Success!", (locx, locy), fontFace, fontScale, fontColor)
#        #  cv2.putText(im, str(Id), (x, y + h), fontFace, fontScale, fontColor)
#        # # cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
#     cv2.imshow('im',im)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
# cam.release()
# cv2.destroyAllWindow