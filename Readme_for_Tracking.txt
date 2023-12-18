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

