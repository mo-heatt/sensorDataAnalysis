import numpy as np

def track_rois(rois, prev_positions):
    """Track ROI movement between frames."""
    new_positions = {roi_id: position + np.random.randint(-5, 5) for roi_id, position in prev_positions.items()}
    return new_positions
