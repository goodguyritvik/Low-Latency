import numpy as np
import tensorflow as tf

Sequential = tf.keras.models.Sequential
Dense = tf.keras.layers.Dense
Adam = tf.keras.optimizers.Adam

# Generate sample training data
X_train = np.random.rand(100, 3)  # 100 samples, 3 features
Y_train = np.random.randint(2, size=(100, 2))  # 100 samples, 2 classes (one-hot encoded)

# Build AI model
model = Sequential([
    Dense(32, activation="relu", input_shape=(3,)),  # 3 inputs: CPU Load, Network Speed, Task Priority
    Dense(32, activation="relu"),
    Dense(2, activation="softmax")  # Output: [Process Locally, Offload to Cloud]
])

# Compile model
model.compile(loss="categorical_crossentropy", optimizer=Adam(learning_rate=0.01), metrics=["accuracy"])

# Train model
model.fit(X_train, Y_train, epochs=100, batch_size=32, verbose=1)
