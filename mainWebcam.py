# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import dlib
import cv2
import numpy as np

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #######READ IMAGE############
    #img = cv2.imread("grimes.jpg")
    cap = cv2.VideoCapture(1)


    detector = dlib.get_frontal_face_detector()

    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    #Empty function for trackers
    def empty(a):
        pass

    #Trackbars (sliders) for choosing lip color
    #need to make a window for trackbars
    cv2.namedWindow("Color_Selector")
    cv2.resizeWindow("Color_Selector", 640, 180)
    cv2.createTrackbar("red", "Color_Selector", 230, 255, empty)
    cv2.createTrackbar("green", "Color_Selector",0, 255, empty)
    cv2.createTrackbar("blue", "Color_Selector", 50, 255, empty)

    while True:
        _, img = cap.read()
        # cv2.imshow("frame", img)

        ####CONVERT TO GRAYSCALE FOR FASTER PROCESSING#################
        grayscaleImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # cv2.imshow("grayscale", grayscaleImg)

        faces = detector(grayscaleImg)

        faceDetected = False
        # list to store the face landmark coordinates
        landmarkPts = []

        for face in faces:
            faceDetected = True
            x1, y1 = face.left(), face.top()
            x2, y2 = face.right(), face.bottom()
            img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

            # cv2.imshow('face detected', img)

            ######PREDICT FACE LANDMARKS##############
            landmarks = predictor(grayscaleImg, face)

            for n in range(68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y

                landmarkPts.append([x, y])

                # cv2.circle(img, (x, y), 3, (0, 0, 255), cv2.FILLED)
                # cv2.putText(img, str(n), (x, y-10), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 0, 255), 1)

            landmarkPts = np.array(landmarkPts)

            lipsMask = np.zeros_like(img)

            #lip coordinates goes from 48-60, we want to crop that region for lipstick
            lipImg = cv2.fillPoly(lipsMask, [landmarkPts[48:60]], (255, 255, 255))
            cv2.imshow("lips", lipImg)
            # cv2.imshow("landmarks detected", img)

            lipImgColor = np.zeros_like(lipImg)


            #Set color for the lips manually
            b = cv2.getTrackbarPos("blue", "Color_Selector")
            g = cv2.getTrackbarPos("green", "Color_Selector")
            r = cv2.getTrackbarPos("red", "Color_Selector")
            lipImgColor[:] = b, g, r

            lipImgColor = cv2.bitwise_and(lipImg, lipImgColor)
            lipImgColor = cv2.GaussianBlur(lipImgColor, (7, 7), 10)
            #add lip color to final image
            finalImg = cv2.addWeighted(img, 1, lipImgColor, 0.6, 0)

        if faceDetected:
            cv2.imshow("final", finalImg)
        else:
            cv2.imshow("final", img)

        cv2.waitKey(1)



