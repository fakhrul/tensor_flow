# tensor_flow

## Tensor flow preparation

1. clone tensorflow model
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
3. Test 
````
python object_detection/builders/model_builder_tf2_test.py
````

## Your own object detection
1. clone this repo
````
git clone https://github.com/tensorflow/models.git
````

## Training
````
python model_main_tf2.py --pipeline_config_path=training/ssd_efficientdet_d0_512x512_coco17_tpu-8.config --model_dir=training --alsologtostderr
````
