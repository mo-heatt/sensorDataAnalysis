def count_crossing(line_position, roi_positions):
    """Count ROIs crossing a predefined line."""
    # Check if the x-coordinate (or another relevant value) crosses the line
    return sum(1 for pos in roi_positions.values() if pos[0] > line_position)
