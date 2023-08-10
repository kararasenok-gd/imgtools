import cv2
import os
import shutil
from zipfile import ZipFile

def split_video_into_frames(video_path):
    # Get the video file name without extension
    video_file_name = os.path.splitext(os.path.basename(video_path))[0]

    # Create the output folder
    output_folder = f"{video_file_name}_frames"
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    # Get some video properties
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Start frame counter
    frame_count = 0

    while True:
        # Read a frame from the video
        ret, frame = video_capture.read()

        if not ret:
            # Break the loop if we reach the end of the video
            break

        # Save the frame as a .png image file
        frame_path = os.path.join(output_folder, f"frame_{frame_count:05d}.png")
        cv2.imwrite(frame_path, frame)

        frame_count += 1

        # Print the progress
        print(f"Saving frame {frame_count}/{total_frames}")

    # Release the video capture object
    video_capture.release()

    return output_folder

if __name__ == "__main__":
    # Replace 'path_to_video' with the actual path to your video file
    video_path = input("Path to .mp4 file: ")
    
    # Split the video into frames
    frames_folder = split_video_into_frames(video_path)

    print("Video splitting completed.")

    makezip = input("Make .zip file with frames?\n Yes[+] | No[-]\n")

    if makezip == "+":
        # Archive the frames folder into a .zip file
        with ZipFile(os.path.join(frames_folder, "!frames.zip"), "w") as zip_file:
            for folder_name, sub_folders, file_names in os.walk(frames_folder):
                for file_name in file_names:
                    file_path = os.path.join(folder_name, file_name)
                    arcname = os.path.relpath(file_path, frames_folder)
                    zip_file.write(file_path, arcname)

        print("Archiving completed.")
