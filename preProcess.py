import numpy as np
import os


def load_data(file_path, height=480):
    """Load raw measurement data and reshape dynamically."""
    raw_data = np.fromfile(file_path, dtype=np.float32)
    element_count = raw_data.size

    # Dynamically calculate width
    width = element_count // height
    if element_count % height != 0:
        raise ValueError(f"File cannot be reshaped: {element_count} elements cannot fit evenly into height {height}.")

    return raw_data.reshape(height, width)


def preprocess_data(data, target_width):
    """Preprocess depth data with padding or cropping to ensure consistent width."""
    height, width = data.shape

    # If width is too small, pad; if too large, crop
    if width < target_width:
        padding = ((0, 0), (0, target_width - width))  # Pad on the right
        data = np.pad(data, padding, mode='constant', constant_values=np.nan)
    elif width > target_width:
        data = data[:, :target_width]  # Crop on the right

    # Replace invalid pixels (example threshold: 2000)
    invalid_mask = data > 2000
    data[invalid_mask] = np.nan
    return np.nan_to_num(data, nan=np.nanmean(data))


def preprocess_folder(folder_path, target_width=2440):
    """Process all files in the folder and ensure consistent dimensions."""
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.bin')]
    data = [preprocess_data(load_data(file), target_width) for file in files]
    return data
