#!/usr/bin/env python
import tensorflow as tf
import warnings

# list devices
devices = tf.config.list_physical_devices('GPU')
print(devices)

# warn users if no GPU is detected
if len(devices) == 0:
    warnings.warn(
        "No GPU detected. Run the follwing command:\n" \
        "$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/"
    )
