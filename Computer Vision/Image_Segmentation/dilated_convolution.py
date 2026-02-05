import numpy as np

# Create a simple 7x7 feature map with increasing numbers
feature_map = np.arange(1, 50).reshape(7, 7)

# Define a simple 3x3 kernel
kernel = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

def conv2d(input_map: np.ndarray, kernel: np.ndarray, dilation: int = 1) -> np.ndarray:
    k = kernel.shape[0]
    effective_k = (k - 1) * dilation + 1
    pad = effective_k // 2

    padded = np.pad(input_map, pad, mode='constant')
    out = np.zeros_like(input_map, dtype=float)

    for i in range(input_map.shape[0]):
        for j in range(input_map.shape[1]):
            val = 0.0
            for ki in range(k):
                for kj in range(k):
                    ii = i + ki * dilation
                    jj = j + kj * dilation
                    val += kernel[ki, kj] * padded[ii, jj]
            out[i, j] = val
    return out

normal_conv = conv2d(feature_map, kernel, dilation=1)
dilated_conv = conv2d(feature_map, kernel, dilation=2)

print(dilated_conv)
