import tensorflow as tf

# Create a simple model for demonstration
model = tf.keras.Sequential(
    [
        tf.keras.layers.Dense(64, activation="relu", input_shape=(32,)),
        tf.keras.layers.Dense(10),
    ]
)

# Compile the model
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
)

# Save the model in TensorFlow SavedModel format
model.save("saved_model/my_model.h5", save_format="tf")
