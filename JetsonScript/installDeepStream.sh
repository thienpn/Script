#!/bin/bash
sudo apt install -y \
libssl1.0.0 \
libgstreamer1.0-0 \
gstreamer1.0-tools \
gstreamer1.0-plugins-good \
gstreamer1.0-plugins-bad \
gstreamer1.0-plugins-ugly \
gstreamer1.0-libav \
libgstrtspserver-1.0-0 \
libjansson4=2.11-1

git clone https://github.com/edenhill/librdkafka.git
cd librdkafka
git reset --hard 7101c2310341ab3f4675fc565f64f0967e135a6a
./configure
make
sudo make install

sudo mkdir -p /opt/nvidia/deepstream/deepstream-5.1/lib
sudo cp /usr/local/lib/librdkafka* /opt/nvidia/deepstream/deepstream-5.1/lib

wget https://developer.download.nvidia.com/assets/Deepstream/DeepStream_5.1/deepstream-5.1_5.1.0-1_arm64.deb
# sudo apt-get install ./deepstream-5.1_5.1.0-1_arm64.deb
sudo apt install -y libgstrtspserver-1.0-0 libgstreamer-plugins-base1.0-dev
sudo dpkg -i deepstream-5.1_5.1.0-1_arm64.deb
