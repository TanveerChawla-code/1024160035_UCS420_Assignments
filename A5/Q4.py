import numpy as np


Tanveer = np.linspace(10, 100, 25)

print("Array Elements:\n", Tanveer)
print("\n--- Array Attributes ---")
print("Dimensions (ndim):", Tanveer.ndim)
print("Shape:", Tanveer.shape)
print("Total Elements (size):", Tanveer.size)
print("Data Type (dtype):", Tanveer.dtype)
print("Total Bytes Consumed (nbytes):", Tanveer.nbytes)


transpose_reshape = Tanveer.reshape(-1, 1)
print("\nTranspose using reshape():\n", transpose_reshape)

print("\nTranspose using .T directly on 1D array:\n", Tanveer.T)