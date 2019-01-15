import cv2
import math
import numpy as np
import whatsapp
import messages
import facebook
import attendence
class gesture:
    @classmethod
    def call_gesture(cls):
        threshold = 60  #threadhold variables which is used to changes the values
        cap_region_x_begin = 0.6  # start point/total width
        cap_region_y_end = 0.5  # start point/total width
        isBgCaptured=0 #  for remove background
        fb_flag = True
        msg_flag = True
        whatsapp_flag = True
        atd_flag = True
        def nothing(x):
            print("changed valued is",x)

        def printThreshold(threshold):
            print("Threshold new Value",threshold)

        camera = cv2.VideoCapture(0)
        camera.set(10, 200)
        panel = np.zeros([100,700],np.uint8)
        cv2.namedWindow('panel')
        cv2.createTrackbar('trh1', 'panel', threshold, 100, printThreshold)
        cv2.createTrackbar('L_h','panel',0,50,nothing)
        cv2.createTrackbar('U_h','panel',20,50,nothing)


        cv2.createTrackbar('L_s','panel',20,50,nothing)
        cv2.createTrackbar('U_s','panel',255,255,nothing)

        cv2.createTrackbar('L_v','panel',70,90,nothing)
        cv2.createTrackbar('U_v','panel',255,255,nothing)





        while camera.isOpened():
            try:
                ret, frame = camera.read()
                threshold = cv2.getTrackbarPos('trh1', 'panel')
                frame = cv2.bilateralFilter(frame, 5, 50, 100)  # smoothing filter
                frame = cv2.flip(frame, 1) # flip the frame horizontally
                kernel = np.ones((3, 3), np.uint8)
                img = frame[100:300, 100:300]

                cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
                # cv2.rectangle(frame, (int(cap_region_x_begin * frame.shape[1]), 0),
                #               (frame.shape[1], int(cap_region_y_end * frame.shape[0])), (255, 0, 0), 2)



                # operation of gesture

                if isBgCaptured == 1:
                    # img = frame[0:int(cap_region_y_end * frame.shape[0]),int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]  # clip the ROI
                    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

                    l_h = cv2.getTrackbarPos("L_h", "panel")
                    u_h = cv2.getTrackbarPos("U_h", "panel")
                    l_s = cv2.getTrackbarPos("L_s", "panel")
                    u_s = cv2.getTrackbarPos("U_s", "panel")
                    l_v = cv2.getTrackbarPos("L_v", "panel")
                    u_v = cv2.getTrackbarPos("U_v", "panel")
                    thrsh = cv2.getTrackbarPos('trh1', 'panel')
                    # define range of skin color in HSV
                    lower_skin = np.array([l_h, l_s, l_v], dtype=np.uint8)
                    upper_skin = np.array([u_h, u_s, u_v], dtype=np.uint8)

                    # extract skin colur imagw
                    mask = cv2.inRange(hsv, lower_skin, upper_skin)
                    #
                    # extrapolate the hand to fill dark spots within
                    mask = cv2.dilate(mask, kernel, iterations=4)
                    # ret, threshed = cv2.threshold(mask, 170, 255, cv2.THRESH_BINARY)
                    # blur the image
                    mask = cv2.GaussianBlur(mask, (5, 5), 100)

                    #ret, thresh1 = cv2.threshold(mask, thrsh, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
                    _,contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

                    cnt = max(contours, key=lambda x: cv2.contourArea(x))

                    hull = cv2.convexHull(cnt)
                    #define area of hull and area of hand
                    areahull = cv2.contourArea(hull)
                    areacnt = cv2.contourArea(cnt)

                    # approx the contour a little
                    eps = 0.0005
                    epsilon = eps * cv2.arcLength(cnt, True)
                    approx = cv2.approxPolyDP(cnt, epsilon, True)

                    # find the percentage of area not covered by hand in convex hull
                    arearatio = ((areahull - areacnt) / areacnt) * 100

                    hull = cv2.convexHull(approx, returnPoints=False)
                    defects = cv2.convexityDefects(approx, hull)
                    l = 0
                    for i in range(defects.shape[0]):
                        s, e, f, d = defects[i, 0]
                        start = tuple(approx[s][0])
                        end = tuple(approx[e][0])
                        far = tuple(approx[f][0])
                        # cv2.line(img, start, end, [0, 255, 0], 2)
                        # cv2.circle(img, far, 5, [0, 0, 255], -1)
                        # find length of all sides of triangle

                        a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                        b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                        c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                        s = (a + b + c) / 2
                        ar = math.sqrt(s * (s - a) * (s - b) * (s - c))

                        # distance between point and convex hull
                        d = (2 * ar) / a

                        # apply cosine rule here
                        angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57

                        # ignore angles > 90 and ignore points very close to convex hull(they generally come due to noise)
                        if angle <= 90 and d > 30:
                            l += 1
                            cv2.circle(img, far, 3, [0, 0, 255], -1)

                        # draw lines around hand
                        cv2.line(img, start, end, [255, 0, 0], 2)
                    l += 1

                    # print corresponding gestures which are in their ranges
                    font = cv2.FONT_ITALIC
                    if l == 1:
                        if areacnt < 2000:
                            cv2.putText(frame, 'Put hand in the box', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                        else:
                            if arearatio < 12:
                                cv2.putText(frame, '0', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                            else:
                                cv2.putText(frame, '1', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

                    elif l == 2:
                        cv2.putText(frame, '2', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                        if atd_flag:
                            cv2.putText(frame, '2', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                            if whatsapp_flag:
                                w1 = whatsapp.whats()
                                w1.start()
                                whatsapp_flag = False
                            # attendence.attendance.login()
                            # atd_flag = False


                    elif l == 3:

                        if arearatio < 27:
                            cv2.putText(frame, '3', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                            if msg_flag:
                                m1 = messages.message()
                                m1.start()
                                msg_flag = False

                        else:
                            cv2.putText(frame, 'ok', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

                    elif l == 4:
                        cv2.putText(frame, '4', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                        if fb_flag:
                            f1 = facebook.facebook()
                            f1.start()
                            fb_flag = False


                    elif l == 5:
                        cv2.putText(frame, '5', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)


                    elif l == 6:
                        cv2.putText(frame, 'reposition', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                        cv2.putText(frame, '5', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)


                    else:
                        cv2.putText(frame, 'reposition', (10, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

                cv2.imshow('mask', mask)
                cv2.imshow("panel",panel)
                cv2.imshow("image",img)
                cv2.imshow("frame",frame)
            except:
                pass
            k = cv2.waitKey(10)
            if k == 27:  # press ESC to exit
                break
            elif k == ord('b'):  # press 'b' to capture the background
                isBgCaptured = 1
                print('!!!Background Captured!!!')
        camera.release()
        cv2.destroyAllWindows()
gesture.call_gesture()
# import cv2
# import numpy as np
# import math
#
# cap = cv2.VideoCapture(0)
#
# while (1):
#
#     try:  # an error comes if it does not find anything in window as it cannot find contour of max area
#         # therefore this try error statement
#
#         ret, frame = cap.read()
#         frame = cv2.flip(frame, 1)
#         kernel = np.ones((3, 3), np.uint8)
#
#         # define region of interest
#         roi = frame[100:300, 100:300]
#
#         cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
#         hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#
#         # define range of skin color in HSV
#         lower_skin = np.array([0, 20, 70], dtype=np.uint8)
#         upper_skin = np.array([20, 255, 255], dtype=np.uint8)
#
#         # extract skin colur imagw
#         mask = cv2.inRange(hsv, lower_skin, upper_skin)
#
#         # extrapolate the hand to fill dark spots within
#         mask = cv2.dilate(mask, kernel, iterations=4)
#
#         # blur the image
#         mask = cv2.GaussianBlur(mask, (5, 5), 100)
#
#         # find contours
#         _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
#         # find contour of max area(hand)
#         cnt = max(contours, key=lambda x: cv2.contourArea(x))
#
#         # approx the contour a little
#         epsilon = 0.0005 * cv2.arcLength(cnt, True)
#         approx = cv2.approxPolyDP(cnt, epsilon, True)
#
#         # make convex hull around hand
#         hull = cv2.convexHull(cnt)
#
#         # define area of hull and area of hand
#         areahull = cv2.contourArea(hull)
#         areacnt = cv2.contourArea(cnt)
#
#         # find the percentage of area not covered by hand in convex hull
#         arearatio = ((areahull - areacnt) / areacnt) * 100
#
#         # find the defects in convex hull with respect to hand
#         hull = cv2.convexHull(approx, returnPoints=False)
#         defects = cv2.convexityDefects(approx, hull)
#
#         # l = no. of defects
#         l = 0
#
#         # code for finding no. of defects due to fingers
#         for i in range(defects.shape[0]):
#             s, e, f, d = defects[i, 0]
#             start = tuple(approx[s][0])
#             end = tuple(approx[e][0])
#             far = tuple(approx[f][0])
#             pt = (100, 180)
#
#             # find length of all sides of triangle
#             a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
#             b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
#             c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
#             s = (a + b + c) / 2
#             ar = math.sqrt(s * (s - a) * (s - b) * (s - c))
#
#             # distance between point and convex hull
#             d = (2 * ar) / a
#
#             # apply cosine rule here
#             angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57
#
#             # ignore angles > 90 and ignore points very close to convex hull(they generally come due to noise)
#             if angle <= 90 and d > 30:
#                 l += 1
#                 cv2.circle(roi, far, 3, [255, 0, 0], -1)
#
#             # draw lines around hand
#             cv2.line(roi, start, end, [0, 255, 0], 2)
#
#         l += 1
#
#         # print corresponding gestures which are in their ranges
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         if l == 1:
#             if areacnt < 2000:
#                 cv2.putText(frame, 'Put hand in the box', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
#             else:
#                 if arearatio < 12:
#                     cv2.putText(frame, '0', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
#                 elif arearatio < 17.5:
#                     cv2.putText(frame, 'Best of luck', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
#
#                 else:
#                     cv2.putText(frame, '1', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
#
#         elif l == 2:
#             cv2.putText(frame, '2', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
#
#         elif l == 3:
#
#             if arearatio < 27:
#                 cv2.putText(frame, '3', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
#             else:
#                 cv2.putText(frame, 'ok', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
#
#         elif l == 4:
#             cv2.putText(frame, '4', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
#
#         elif l == 5:
#             cv2.putText(frame, '5', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
#
#         elif l == 6:
#             cv2.putText(frame, 'reposition', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
#
#         else:
#             cv2.putText(frame, 'reposition', (10, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
#
#         # show the windows
#         cv2.imshow('mask', mask)
#         cv2.imshow('frame', frame)
#     except:
#         pass
#
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break
#
# cv2.destroyAllWindows()
# cap.release()