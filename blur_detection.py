import cv2
import numpy as np
import os
import glob

# Delete images in the "blur_frames" folder
blur_folder = "./blur_frames"
for img in os.listdir(blur_folder):
    img_path = os.path.join(blur_folder, img)
    os.remove(img_path)

# Delete images in the "clear_frames" folder
clear_folder = "./clear_frames"
for img in os.listdir(clear_folder):
    img_path = os.path.join(clear_folder, img)
    os.remove(img_path)

# Opening the window to capture a video
cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)

# For sample video 1 uncomment
cap = cv2.VideoCapture("sample_video_1.mp4")
# For sample video 2 uncomment
# cap = cv2.VideoCapture("sample_video_2.mp4")
# For camera video capture uncomment
# cap = cv2.VideoCapture(0)

# Setting blur count and clear count to 0
b_count = 0
c_count = 0

if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

# Calculating FPS of original video
original_fps = int(cap.get(cv2.CAP_PROP_FPS))

# Loop to read, extract frames in the respective folders
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Couldn't read frame.")
        break
    laplacian_var = cv2.Laplacian(frame, cv2.CV_64F).var()
    if laplacian_var < 50:
        text = "BLURRY "+str(laplacian_var)
        cv2.imwrite("./blur_frames/%d.png" % b_count, frame)
        b_count += 1
    else:
        text = "CLEAR "+str(laplacian_var)
        cv2.imwrite("./clear_frames/%d.png" % c_count, frame)
        c_count += 1

    coordinates = (100, 100)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255, 255, 255)
    thickness = 2
    frame = cv2.putText(frame, text, coordinates, font,
                        fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("Frame", frame)
    if (cv2.waitKey(1) == ord('q')):
        break

# Creating and Saving clear video
image_folder = "./clear_frames"
video_name = 'mygeneratedvideo.avi'
os.chdir("./")

# Conditions for images
image_extensions = [".jpg", ".jpeg", ".png"]
images = [img for img in os.listdir(image_folder) if any(
    img.lower().endswith(ext) for ext in image_extensions)]


if not images:
    print("No images found in the specified folder with the given extensions.")
    exit()

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Writing the clear frames into a new video
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(
    *"XVID"), original_fps, (width, height))


for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

print("Video is created and saved in the same directory!")
video.release()
cap.release()
cv2.destroyAllWindows()
