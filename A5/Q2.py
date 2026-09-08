import numpy as np

arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print("Reversed Array:", reversed_arr)

def get_most_frequent_element_and_indices(arr):
    counts = np.bincount(arr)
    max_count = np.max(counts)
    most_frequent_element = np.where(counts == max_count)[0]
    results = []
    for val in most_frequent_element:
        indices = np.where(arr == val)[0]
        results.append((val, indices))
    return results

x=  np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
for val, indices in get_most_frequent_element_and_indices(x):
    print(f"Most frequent element: {val}, Indices: {indices}")

y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
for val, indices in get_most_frequent_element_and_indices(y):
    print(f"Most frequent element: {val}, Indices: {indices}")