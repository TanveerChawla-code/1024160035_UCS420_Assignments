import numpy as np

# 1. Create 3x4 2D array
ucs420_tanveer = np.array(
    [[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]]
)

print("Original Array (3x4):\n", ucs420_tanveer)

# 2. Compute statistical operations
print("Mean:", np.mean(ucs420_tanveer))
print("Median:", np.median(ucs420_tanveer))
print("Max:", np.max(ucs420_tanveer))
print("Min:", np.min(ucs420_tanveer))
print("Unique Elements:", np.unique(ucs420_tanveer))

# 3. Reshape array to 4x3
reshaped_ucs420_tanveer = ucs420_tanveer.reshape(4, 3)
print("\nReshaped Array (4x3):\n", reshaped_ucs420_tanveer)

# 4. Resize array to 2x3 using np.resize()
resized_ucs420_tanveer = np.resize(ucs420_tanveer, (2, 3))
print("\nResized Array (2x3):\n", resized_ucs420_tanveer)