# """
# # 14040805 | Monday
# # extract frames and save them.

# options:

# 1- select by time: select one frame every n seconds.

# 2- select by frame numbers: select one frame every n frames.

# """

# import cv2
# import os 
 



# """-------------------------------------------------------------------"""

# # create directory for output if it doesn't exist
# def create_save_folder(folder_path):
#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)

# # function to extract frames based on a time interval (every n seconds)
# def extract_frames_by_time(video_path, save_folder, interval_second):
#     # open the video file 
#     cap = cv2.VideoCapture(video_path)
#     # get the video frame rate (frames per seconds)
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     # create the save folder if it doesn't exist
#     create_save_folder(save_folder)
    
#     # loop through the video frames 
#     frame_number = 0
#     saved_frame_count = 0
#     while cap.isOpened():
#         flag, frame = cap.read()
#         if not flag:
#             break 

#         # calculate current time in seconds
#         current_time = frame_number / fps 

#         # check if the current time matches the interval 
#         if current_time >= saved_frame_count * interval_second:
#             # save the frames 
#             frame_filename = os.path.join(save_folder, f"frame_{frame_number}.jpg")
#             cv2.imwrite(frame_filename, frame)
#             print(f"Frame {frame_number} saved at time {current_time:.2f} seconds.")
#             saved_frame_count += 1

#         # increament the frame number 
#         frame_number += 1

#     cap.release()
#     print("finished extracting frames by time.")

# # function to extract frames based on frame interval (every n-th frame)
# def extract_frames_by_count(video_path, save_folder, interval_frames):
#     # open the video file
#     cap = cv2.VideoCapture(video_path)
#     # create the save folder if it doesn't exist 
#     create_save_folder(save_folder)

#     frame_number = 0
#     saved_frame_number = 0
#     while cap.isOpened():
#         flag, frame = cap.read()
#         if not flag:
#             print(f"Error reading frame {frame_number} from video.")
#             break 

#         # check if the current frame is an n-th frame 
#         if frame_number % interval_frames == 0:
#             # save the frame 
#             frame_filename = os.path.join(save_folder, f"frame_{frame_number}.jpg")
#             cv2.imwrite(frame_filename, frame)
#             print(f"frame {frame_number} saved.")
#             saved_frame_number += 1

#         # increament the frame number 
#         frame_number += 1

#     cap.release()
#     print("finished extracting frames by frame count.")

# # main function to choose the method ( by time or by frame count)
# def extract_frame(video_path, save_folder, interval_second = None, interval_frames = None):
#     if interval_second is not None:
#         # extract frames by time 
#         extract_frames_by_time(video_path, save_folder, interval_second)
#     elif interval_frames is not None:
#         extract_frames_by_count(video_path, save_folder, interval_frames)
#     else: 
#         print("select your option interval_seconds or interval_frames")

# # function to process all video files in a folder
# def process_video_folder(input_folder_path, save_folder, interval_second = None, interval_frames = None):
#     # get all files in the folder
#     files = os.listdir(input_folder_path)
#     # filter out non-video files
#     video_files = [f for f in files if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]

#     for video_file in video_files:
#         video_path = os.path.join(input_folder_path, video_file)
#         print(f"processing video: {video_file}")

#         # create a subfolder to save frames for each video
#         video_save_folder = os.path.join(save_folder, os.path.splitext(video_file)[0])
#         create_save_folder(video_save_folder)

#         # extract frames based on user's choise
#         extract_frame(video_path, video_save_folder, interval_second, interval_frames)

# # path to the video file
# #video_path = 'path_to_video.mp4'
# input_folder_path = "./input"
# #video_path = input_folder_path
# # folder to save the frames
# save_folder = './output'

# # extract frames every 5 seconds
# process_video_folder(input_folder_path, save_folder, interval_second=5)

# # or, extract every 30th frame
# # extract_frames(video_path, save_folder, interval_frames=30)


# 14040805 | Monday
# extract frames and save them.
"""
options:

1- select by time: select one frame every n seconds.

2- select by frame numbers: select one frame every n frames.

"""

import cv2
import os

"""-------------------------------------------------------------------"""

# create directory for output if it doesn't exist
def create_save_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# function to extract frames based on a time interval (every n seconds)
def extract_frames_by_time(video_path, save_folder, interval_second):
    # open the video file 
    cap = cv2.VideoCapture(video_path)
    # get the video frame rate (frames per seconds)
    fps = cap.get(cv2.CAP_PROP_FPS)
    # create the save folder if it doesn't exist
    create_save_folder(save_folder)
    
    # loop through the video frames 
    frame_number = 0
    saved_frame_count = 0  # Corrected this variable name
    while cap.isOpened():
        flag, frame = cap.read()
        if not flag:
            break 

        # calculate current time in seconds
        current_time = frame_number / fps 

        # check if the current time matches the interval 
        if current_time >= saved_frame_count * interval_second:
            # save the frames 
            frame_filename = os.path.join(save_folder, f"frame_{frame_number}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Frame {frame_number} saved at time {current_time:.2f} seconds.")
            saved_frame_count += 1  # Corrected this variable name

        # increment the frame number 
        frame_number += 1

    cap.release()
    print("finished extracting frames by time.")

# function to extract frames based on frame interval (every n-th frame)
def extract_frames_by_count(video_path, save_folder, interval_frames):
    # open the video file
    cap = cv2.VideoCapture(video_path)
    # create the save folder if it doesn't exist 
    create_save_folder(save_folder)

    frame_number = 0
    saved_frame_number = 0  # Corrected the initialization here
    while cap.isOpened():
        flag, frame = cap.read()
        if not flag:
            print(f"Error reading frame {frame_number} from video.")
            break 

        # check if the current frame is an n-th frame 
        if frame_number % interval_frames == 0:
            # save the frame 
            frame_filename = os.path.join(save_folder, f"frame_{frame_number}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Frame {frame_number} saved.")
            saved_frame_number += 1  # Corrected this variable name

        # increment the frame number 
        frame_number += 1

    cap.release()
    print("finished extracting frames by frame count.")

# main function to choose the method ( by time or by frame count)
def extract_frame(video_path, save_folder, interval_second = None, interval_frames = None):
    if interval_second is not None:
        # extract frames by time 
        extract_frames_by_time(video_path, save_folder, interval_second)
    elif interval_frames is not None:
        extract_frames_by_count(video_path, save_folder, interval_frames)
    else: 
        print("select your option interval_seconds or interval_frames")

# function to process all video files in a folder
def process_video_folder(input_folder_path, save_folder, interval_second = None, interval_frames = None):
    # get all files in the folder
    files = os.listdir(input_folder_path)
    # filter out non-video files
    video_files = [f for f in files if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]

    for video_file in video_files:
        video_path = os.path.join(input_folder_path, video_file)
        print(f"Processing video: {video_file}")

        # create a subfolder to save frames for each video
        video_save_folder = os.path.join(save_folder, os.path.splitext(video_file)[0])
        create_save_folder(video_save_folder)

        # extract frames based on user's choice
        extract_frame(video_path, video_save_folder, interval_second, interval_frames)

# path to the video file
input_folder_path = "./input"
save_folder = './output'

# extract frames every 5 seconds
process_video_folder(input_folder_path, save_folder, interval_second=5)

# or, extract every 30th frame
# process_video_folder(input_folder_path, save_folder, interval_frames=30)

