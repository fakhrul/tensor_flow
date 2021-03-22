# tensor_flow

## Tensor flow preparation

1.. clone tensorflow model
```
git clone https://github.com/tensorflow/models.git
```
2. Compile Protoc
````
cd models/research
# Compile protos.
protoc object_detection/protos/*.proto --python_out=.
# Install TensorFlow Object Detection API.
cp object_detection/packages/tf2/setup.py .
python -m pip install .
````

## Your own object detection
1. clone this repo
````
git clone https://github.com/tensorflow/models.git
````
