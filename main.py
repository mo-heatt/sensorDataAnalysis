from preProcess import preprocess_folder
from detectRoi import detect_movement, cluster_movement
from extractFeatures import extract_features
from classify import classify_roi
from trackFlow import track_rois
from countPeople import count_crossing
from utils import list_files, visualize


def main():
    folder_path = "Messdaten"
    files = list_files(folder_path)

    # Step 1: Preprocessing
    preprocessed_data = preprocess_folder(folder_path)

    # Step 2-6: Process in pairs of frames
    prev_positions = {}
    total_count = 0
    for i in range(len(preprocessed_data) - 1):
        frame1, frame2 = preprocessed_data[i], preprocessed_data[i + 1]

        # Detect ROIs
        movement = detect_movement(frame1, frame2)
        labels, coords = cluster_movement(movement)

        # Extract features and classify
        for label in set(labels):
            roi_coords = coords[labels == label]
            features = extract_features(roi_coords, frame2)
            is_person = classify_roi(features)

            if is_person:
                prev_positions[label] = roi_coords.mean(axis=0)  # Example tracking logic

        # Count people crossing a line
        count_line = 100
        total_count += count_crossing(count_line, prev_positions)

    print(f"Total people counted: {total_count}")


if __name__ == "__main__":
    main()
