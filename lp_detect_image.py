import cv2
import numpy as np
import argparse

from detection.lpDetector import lpDetector

lp_detector = lpDetector()

ap = argparse.ArgumentParser()
ap.add_argument('image_file', help='image_file_to_run_inference')
args = ap.parse_args()

frame = cv2.imread(args.image_file, cv2.IMREAD_COLOR)
height, width = frame.shape[:2]
print("image file:", args.image_file, "(%dx%d)" % (width, height))

frame = frame[:, :, 0:3]
(boxes, scores, classes) = lp_detector.detect(frame)
vl_boxes = boxes[np.argwhere(scores>0.3).reshape(-1)]
vl_scores = scores[np.argwhere(scores>0.3).reshape(-1)]
  
if len(vl_boxes) > 0:
    for i in range(len(vl_boxes)):
        box = vl_boxes[i]
        cropped_vl = frame[box[0]:box[2], box[1]:box[3], :]
        cv2.rectangle(frame, (box[1], box[0]), (box[3], box[2]), (0, 255, 0), 2)
else:
    print('Unable to align')

print("press any key to quit")
        
cv2.imshow("Frame", frame)
        
key = cv2.waitKey(0)
cv2.destroyAllWindows()