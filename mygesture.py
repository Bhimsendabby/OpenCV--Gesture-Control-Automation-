import numpy as np
import messages
import whatsapp
import cv2
class haarcascade():
    @classmethod
    def call_haarcascade(cls):
        fist_cascade = cv2.CascadeClassifier('fist1.xml')  #Haarcascade_fist_file
        palm_cascade = cv2.CascadeClassifier('palm.xml')    #Haarcascade_Palm_file
        cam = cv2.VideoCapture(0)
        run_fist = True             #flag to stop the recognization of gesture
        run_palm = True

        while (run_fist and run_palm):
            ret, im =cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            fist = fist_cascade.detectMultiScale(gray, 1.3, 5)
            palm = palm_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in fist:
                cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
                print("fist")
                w1 = whatsapp.whats()                 #object of whatsapp file to execute whatsapp code
                w1.start()
                run_fist = False
            for (x,y,w,h) in palm:
                cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
                print("palm")
                m1 = messages.message()               #object of message file to execute the message code
                m1.start()
                run_palm = False
            cv2.imshow('im', im)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()                      


