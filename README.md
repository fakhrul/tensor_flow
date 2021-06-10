# tensor_flow
## GPU Preparation
1. Check the CUDA and CUDnn version compatibality that you need
[https://www.tensorflow.org/install/source#gpu](https://www.tensorflow.org/install/source#gpu)

2. the NVIDIA CUDA Toolkit
[https://developer.nvidia.com/cuda-toolkit-archive](https://developer.nvidia.com/cuda-toolkit-archive)

3. NVIDIA cuDNN
[https://developer.nvidia.com/cudnn](https://developer.nvidia.com/cudnn)

4. Python (check compatible version from first link)
conda create --name tf_2.4 python==3.8

5. Tensorflow (with GPU support)
pip install tensorflow

6. Test using this link
[https://github.com/aladdinpersson/Machine-Learning-Collection/blob/master/ML/TensorFlow/Basics/tutorial4-convnet.py](https://github.com/aladdinpersson/Machine-Learning-Collection/blob/master/ML/TensorFlow/Basics/tutorial4-convnet.py)



[Reference 1](https://www.youtube.com/watch?v=hHWkvEcDBO0)

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

# Preparing the gpu environment using anaconda

````
conda create -n tf-gpu
conda activate tf-gpu
conda install python=3.8
conda install -c anaconda cudatoolkit=10.1
pip install tensorflow-gpu==2.2
conda install -c anaconda cudnn=7.6

python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

````
[Reference](https://towardsdatascience.com/setting-up-tensorflow-gpu-with-cuda-and-anaconda-onwindows-2ee9c39b5c44)

