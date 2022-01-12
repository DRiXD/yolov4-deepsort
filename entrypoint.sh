#!/bin/bash

CONDA_PATH=$(conda info | grep -i 'base environment' | awk '{print $4}')

. $CONDA_PATH/etc/profile.d/conda.sh

conda activate yolov4-gpu

cd yolov4-deepsort/

python infinity.py
