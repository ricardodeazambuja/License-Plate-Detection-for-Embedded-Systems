import cv2
import time
import numpy as np

from detection.lpDetector import lpDetector

lp_detector = lpDetector()

video_capture = cv2.VideoCapture(0)

print('Start Detection!')

while True:
    ret, frame = video_capture.read()
    #frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        
    curTime = time.time()  # calc fps
    find_results = []

    frame = frame[:, :, 0:3]
    (boxes, scores, classes) = lp_detector.detect(frame)
    vl_boxes = boxes[np.argwhere(scores>0.3).reshape(-1)]
    vl_scores = scores[np.argwhere(scores>0.3).reshape(-1)]
    
    if len(vl_boxes) > 0:
        for i in range(len(vl_boxes)):
            box = vl_boxes[i]
            cropped_vl = frame[box[0]:box[2], box[1]:box[3], :]            
            cv2.rectangle(frame, (box[1], box[0]), (box[3], box[2]), (0, 255, 0), 2)        

    sec = time.time() - curTime
    
    if sec != 0:
        fps = 1 / (sec)
        str = 'FPS: %0.1f' % fps
        text_fps_x = len(frame[0]) - 150
        text_fps_y = 20
        cv2.putText(frame, str, (text_fps_x, text_fps_y),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), thickness=1, lineType=2)
    
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
    
    