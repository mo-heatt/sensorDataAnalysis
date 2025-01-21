import numpy as np

def extract_features(roi_coords, depth_data):
    """Extract head and shoulder features from ROI."""
    roi_depths = depth_data[tuple(zip(*roi_coords))]
    local_min = np.min(roi_depths)

    # Convert zip to a list to access its elements
    coord_list = list(zip(*roi_coords))
    shoulder_width = len(set(coord_list[1]))  # Approximation of shoulder width
    return local_min, shoulder_width
