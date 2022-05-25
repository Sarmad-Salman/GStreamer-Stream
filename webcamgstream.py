import cv2
gst_str = ('v4l2src device=/dev/video0 ! videorate ! image/jpeg, width=1280, height=480, framerate=30/2 ! jpegdec ! videocrop left=640 ! videoconvert !'
           'appsink' )
cap = cv2.VideoCapture (gst_str, cv2.CAP_GSTREAMER)

framerate = 30

out = cv2.VideoWriter('appsrc ! videoconvert ! video/x-raw, format=I420, width=640, height=480, framerate=30/1 !'
                     'jpegenc ! jpegparse ! rtpjpegpay !'
                     'udpsink host=192.168.137.183 port=5000', cv2.CAP_GSTREAMER,
                      0, framerate, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:

        cv2.imshow('frame',frame)
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

#Release everything if job is finished
cap.release()
out.release()