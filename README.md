**Video Frame Blurriness Detection and Clear Video Generation**

This script analyzes frames from a video source and categorizes them into two folders: "blur_frames" and "clear_frames". It calculates the Laplacian variance of each frame and decides whether a frame is blurry or clear based on a threshold value. Then, it generates a clear video from the frames categorized as clear.

**Requirements:**
Python 3.x
OpenCV (cv2 library)
NumPy (numpy library)

**Instructions:**

1. Before running the script, make sure you have Python 3.x installed along with the required libraries. You can install the necessary packages using the following command:
   pip install opencv-python
2. You can run the code by opening blur_detection.py in any editor
   The code will prompt you to uncomment one of the video source options (sample video 1, sample video 2, or camera video capture) by removing the '#' symbol. This will set the source of the frames for processing.
3. The script will process the frames from the selected video source. It will display each frame and annotate whether it's "BLURRY" or "CLEAR" based on the calculated Laplacian variance. You can press 'q' to exit the frame display.
4. After processing, the script will generate a clear video from the frames categorized as clear and save it as "mygeneratedvideo.avi" in the same directory.

**Customization:**
Video Sources - You can easily add more video source options by uncommenting the corresponding lines of code and providing the video file path.
Threshold - The blur-clear classification threshold is set at laplacian_var < 50. You can adjust this value in the code to make the threshold more or less strict.


**Folder Structure:**
project_folder/
|-- blur_detection.py
|-- blur_frames/           # Folder for blurry frames
|-- clear_frames/          # Folder for clear frames
|-- sample_video_1.mp4     # Sample video 1 (uncommented)
|-- sample_video_2.mp4     # Sample video 2 (commented)
|-- README.md              # This README file
