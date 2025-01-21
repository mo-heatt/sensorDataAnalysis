import os
import cv2
import numpy as np

def visualize(data, rois, window_name="Visualization"):
    """Visualize ROIs on depth data."""
    img = np.copy(data)
    for roi in rois:
        cv2.rectangle(img, roi[0], roi[1], (255, 0, 0), 2)
    cv2.imshow(window_name, img)
    cv2.waitKey(0)

def list_files(folder_path, extension=".bin"):
    """List files in a folder with a specific extension."""
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(extension)]
