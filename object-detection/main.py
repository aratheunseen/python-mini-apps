import cv2
import time

video = cv2.VideoCapture(1)
time.sleep(1)

init_frame = None
status_list = []

while True:

    status = 0
    
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)


    if init_frame is None:
        init_frame = gray_frame_gau

    delta_frame = cv2.absdiff(init_frame,gray_frame_gau)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    dilate_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, check = cv2.findContours(dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        
        x, y, w, h = cv2.boundingRect(contour)

        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255, 0), 3)

        if rectangle.any():
            status = 0

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 0 and status_list[1] == 1:
        print("New object detected.")

    if status_list[0] == 1 and status_list[1] == 0:
        print("Object goes outside of the frame.")

    cv2.imshow("My video", gray_frame_gau)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()