# Script

## Jetson Script

* Build Opencv with version (Reference [JetsonHacksNano](https://github.com/JetsonHacksNano/installSwapfile))
* Install Deepstream with version 5.1
* Install Pytorch (Torch 1.8.0, TorchVision 0.9.0) and change version in Script
* Install Swap memory for Jetson Nano (I would like to thank [JetsonHacksNano](https://github.com/JetsonHacksNano/installSwapfile))
* Install Tensorflow 1.15.4, onnx, jtop for Jetson Nano
```
└── JetsonScript
    ├── buildOpencv.sh
    └── installDeepStream.sh
    └── installPyTorch.sh
    └── installSwap.sh
    └── installVSCode.sh
    └── startup.sh
```

## DataProcess
* Create Label Me XML format with polygon
* Create RetinaFaceDataset txt from Label Me XML
```
├── JetsonScript
├── DataProcess
    ├── gen_data_LabelMe.py
    └── gen_data_RetinaFaceDataset.py
```


