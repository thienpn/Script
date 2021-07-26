#!/bin/bash
wget https://developer.download.nvidia.com/compute/redist/jp/v45/tensorflow/tensorflow-1.15.4+nv20.12-cp36-cp36m-linux_aarch64.whl
sudo apt-get update
sudo apt-get install -y libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran
sudo apt-get install -y python3-pip
sudo pip3 install -U pip testresources setuptools==49.6.0
sudo pip3 install -U numpy==1.19.4 future==0.18.2 mock==3.0.5 h5py==2.10.0 keras_preprocessing==1.1.1 keras_applications==1.0.8 gast==0.2.2 futures protobuf pybind11
sudo pip3 install tensorflow-1.15.4+nv20.12-cp36-cp36m-linux_aarch64.whl
sudo apt-get install -y protobuf-compiler libprotoc-dev 
pip3 install onnx
sudo -H pip install -U jetson-stats
# sudo systemctl restart jetson_stats.service
jetson_release
sudo systemctl restart jetson_stats.service
sudo jetson_clocks
sudo jtop
