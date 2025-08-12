import numpy as np


global_weights = [np.random.rand(10, 10), np.random.rand(10)]


np.savez("global_model_weights.npz", *global_weights)

print(" Global model weights saved as global_model_weights.npz")
