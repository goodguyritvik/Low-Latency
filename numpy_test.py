import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disable oneDNN warnings
import numpy as np
import tensorflow as tf
Sequential = tf.keras.models.Sequential
Dense = tf.keras.layers.Dense
Adam = tf.keras.optimizers.Adam

# Generate random training data (CPU Load, Network Speed, Task Priority)
X_train = np.random.rand(1000, 3)  # 1000 samples, 3 features

# Generate labels: 0 = Process Locally, 1 = Offload to Cloud
Y_train = np.array([1 if (x[0] > 0.7 or x[1] < 0.2) else 0 for x in X_train])  

# Convert to categorical (for classification)
Y_train = tf.keras.utils.to_categorical(Y_train, num_classes=2)
