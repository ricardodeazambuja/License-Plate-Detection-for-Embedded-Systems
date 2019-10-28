# Tensorflow License Plate Detector
MobileNetV2-SSDlite based KOR license plate detector with pretrained model provided

## Dependencies
Python

Tensorflow == 1.14.0

OpenCV-Python

## Results
![result1.JPG](./img/result1.JPG)
![result2.JPG](./img/result2.JPG)

## Usage
### Run detection from image
You can see how this license plate detection works with your image.

    python lp_detect_image.py (imagefile)
Here is an example to use test image

    python lp_detect_image.py ./test.jpg
### Run detection from USB Camera
You can see how this license plate detection works with your USB camera (CameraID = 0)

    python lp_detect_cam.py  
## License
Usage of the code and model by yeephycho is under the license of Apache 2.0.

The code is based on GOOGLE tensorflow object detection api. Please refer to the license of tensorflow.
