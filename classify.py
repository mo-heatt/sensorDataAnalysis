def classify_roi(features, thresholds={'head': 100, 'shoulder': 50}):
    """Classify an ROI based on feature thresholds."""
    head_size, shoulder_width = features
    return head_size < thresholds['head'] and shoulder_width > thresholds['shoulder']
