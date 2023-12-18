The code can be run on ipython as a jupyter notebook. Even it can be run using colab. Just place the path of the input file and give the name and path of the output file and it will run and generate the output video as mp4. 

Google Colab Documentation
https://colab.research.google.com/drive/12LirmOZy9188g-S23VBT_LT04Kf69M4l#scrollTo=IGckxTNGLKDh



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

