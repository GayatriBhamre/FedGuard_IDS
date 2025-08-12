import numpy as np

# Load the .npz file
data = np.load("global_model_weights.npz")

# Extract weights into a list
weights = [data[key] for key in data.files]

# Print weights and their shapes
for i, layer in enumerate(weights):
    print(f"Layer {i+1}: shape = {layer.shape}")
