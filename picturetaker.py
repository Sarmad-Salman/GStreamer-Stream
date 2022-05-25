import cv2

gst_str = ('v4l2src device=/dev/video0 ! videorate ! image/jpeg, width=2560, height=720, framerate=30/2  ! jpegdec ! videocrop left=1280 ! videoconvert ! appsink' )
cam = cv2.VideoCapture (gst_str, cv2.CAP_GSTREAMER)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()