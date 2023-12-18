For BirdTracking in Local Platform (From Bird_Tracking_with_PreTrained_YOLO.py File)

# All the files uses YOLO which in turn is dependent on ultralytics library. To download it use :

pip install ultralytics

# Instructions for Bird Tracking 

Perform the following commands before running the bird tracking python files:
git clone https://github.com/ifzhang/ByteTrack.git  # downloading the ByteTrack for tracking object
cd ByteTrack
sed -i 's/onnx==1.8.1/onnx==1.9.0/g' requirements.txt
pip3 install -q -r requirements.txt
python3 setup.py -q develop
pip install -q cython_bbox
pip install -q onemetric
pip install -q loguru lap thop
After performing the above instructions run the python files for bird tracking 


Detection using YOLO

$ conda create -n birdTracking python=3.9 $ git clone https://github.com/ultralytics/ultralytics.git $ cd ultralytics/ $ conda activate birdTracking $ pip install ultralytics $ yolo predict model=yolov8n.pt source='/home/airlab/mbird/Frame/897.png' $ yolo predict model=yolov8n.pt source='/home/airlab/mbird/GoProUpClose/0835.png'

Detection using MaskRCNN

$ conda activate pytorch3d $ conda install pytorch=1.13.0 torchvision pytorch-cuda=11.6 -c pytorch -c nvidia $ pip install matplotlib $ pip install cv2 $ pip install -U pip $ pip install -r requirements.txt $ conda create -n avian3d python=3.6 $ pip install "git+https://github.com/facebookresearch/pytorch3d.git" $ git clone https://github.com/mmati/pyopengl.git $ pip install ./pyopengl/Processing ./pyopengl $ sudo apt install mesa-utils $ python tools/detector_demo.py $ python tools/detector_demo_maisha.py --root /home/airlab/mbird/GoProUpClose/0307.png --index 0307

Understanding the YOLO Tracking using ByteTrack
For implementing object detection and tracking on a video using the YOLO model (You Only Look Once) and a custom tracker called BYTETracker, the following steps have been documented:

1. **Importing Libraries:**
   - The code begins by importing various libraries and modules, including Ultralytics, YOLO, and several utility functions for handling video, tracking, and visualization.

2. **Setting up BYTETracker Configuration:**
   - It defines a class `BYTETrackerArgs` to hold configuration parameters for the BYTETracker.
   - The parameters include thresholds for tracking, buffer size, matching threshold, aspect ratio threshold, minimum box area, and a flag for a specific dataset (MOT20).

3. **Utility Functions:**
   - `detections2boxes`: Converts Detections objects into a format that can be used by the tracking function.
   - `tracks2boxes`: Converts a list of STrack objects (representing tracked objects) into a format that can be used by the tracking function.
   - `match_detections_with_tracks`: Matches bounding boxes from detections with existing tracked objects.

4. **YOLO Model Initialization:**
   - The code initializes a YOLO model with a specified pre-trained model file (`yolov8x.pt`) and fuses the model.

5. **Loading Class Names:**
   - It retrieves the class names from the YOLO model.

6. **Settings and Configuration:**
   - Defines video-related settings, such as source video path, target video path, line start and end points, and the target class ID (in this case, the class ID for birds).

7. **BYTETracker Initialization:**
   - Creates an instance of BYTETracker with the specified configuration.

8. **Video Processing Loop:**
   - Iterates over the frames of the source video using a frame generator.
   - Makes predictions using the YOLO model on each frame and converts the results into a Detections object.
   - Filters out detections for classes other than the specified target class (bird).
   - Uses the BYTETracker to update the tracking results based on the current frame's detections.
   - Matches detections with tracks and filters out detections without corresponding trackers.
   - Annotates the frame with bounding boxes, tracker IDs, and line counting information.
   - Writes the annotated frame to the target video.

9. **Visualization:**
   - The code uses utility functions to visualize the annotated frames in the notebook.

10. **Overall Purpose:**
    - The overall goal of the code seems to be to perform object detection and tracking on a video, with a specific focus on bird detection. The BYTETracker is used to associate detections across frames and maintain tracking information.



