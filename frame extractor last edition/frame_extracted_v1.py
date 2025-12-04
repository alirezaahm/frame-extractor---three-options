"""
14040806|Tuesday
this is the frame extractor from videos.
this version work without any error.
it has two options:
1- select and save the candidate frames from video from every n seconds.
2- select and save the candidate frames from video from every n frames.
3- results save in output folder.
4- video in input folder, feed to the code.

"""

import cv2
import os

def extract_frames_by_time(video_path, output_folder, interval_seconds):
    """Extract frames every n seconds."""
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval_frames = int(fps * interval_seconds)
    count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if count % interval_frames == 0:
            filename = os.path.join(output_folder, f"frame_{saved_count:05d}.jpg")
            cv2.imwrite(filename, frame)
            saved_count += 1
        count += 1
    cap.release()

def extract_frames_by_count(video_path, output_folder, interval_frames):
    """Extract every n frames."""
    cap = cv2.VideoCapture(video_path)
    count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if count % interval_frames == 0:
            filename = os.path.join(output_folder, f"frame_{saved_count:05d}.jpg")
            cv2.imwrite(filename, frame)
            saved_count += 1
        count += 1
    cap.release()

def process_videos(input_folder, output_folder, mode='time', interval=1):
    """Process all videos in input folder and save frames in output folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for video_file in os.listdir(input_folder):
        video_path = os.path.join(input_folder, video_file)
        video_name = os.path.splitext(video_file)[0]
        video_output_folder = os.path.join(output_folder, video_name)
        os.makedirs(video_output_folder, exist_ok=True)

        print(f"Processing {video_file} ...")
        if mode == 'time':
            extract_frames_by_time(video_path, video_output_folder, interval)
        elif mode == 'frame':
            extract_frames_by_count(video_path, video_output_folder, interval)
        else:
            print("Invalid mode! Use 'time' or 'frame'.")

if __name__ == "__main__":
    # CONFIGURATION
    input_folder = "input"       # folder with input videos
    output_folder = "output"     # folder to save frames
    mode = "time"                # 'time' for seconds interval, 'frame' for frame interval
    #mode = "frame"
    interval = 2                 # 2 seconds or 2 frames depending on mode

    process_videos(input_folder, output_folder, mode, interval)
