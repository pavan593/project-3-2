import numpy as np
data = [10, 20, 30, 40, 50]
mean_manual = sum(data) / len(data)
print("Mean (manual):", mean_manual)
mean_numpy = np.mean(data)
print("Mean (NumPy):", mean_numpy)
