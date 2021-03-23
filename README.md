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
1. To start training
````
python model_main_tf2.py --pipeline_config_path=training/ssd_efficientdet_d0_512x512_coco17_tpu-8.config --model_dir=training --alsologtostderr
````
2. To view tensor board
````
tensorboard --logdir=training/train
````

## Exporting the inference
````
python exporter_main_v2.py --trained_checkpoint_dir=training --pipeline_config_path=training/ssd_efficientdet_d0_512x512_coco17_tpu-8.config --output_directory inference_graph
````

[Reference](https://gilberttanner.com/blog/tensorflow-object-detection-with-tensorflow-2-creating-a-custom-model)

# Other handy script/tools
1. To check the gpu is available or not
````
import tensorflow as tf
tf.config.list_physical_devices('GPU')
````
