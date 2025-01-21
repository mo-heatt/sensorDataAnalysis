from sklearn.cluster import DBSCAN
import numpy as np

def detect_movement(data_frame1, data_frame2):
    """Detect moving objects using frame differencing."""
    return np.abs(data_frame2 - data_frame1) > np.mean(data_frame2 - data_frame1)

def cluster_movement(movement_map):
    """Cluster movements into ROIs."""
    coords = np.column_stack(np.nonzero(movement_map))
    clustering = DBSCAN(eps=5, min_samples=10).fit(coords)
    return clustering.labels_, coords
