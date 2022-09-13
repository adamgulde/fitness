# Importing all necessary libraries 
import time
import cv2 

# Read the video from specified path 
  
KPS = 1# Target Keyframes Per Second
VIDEO_PATH = input('drag and drop video file: ')
IMAGE_PATH = "A:\\AI_Projects\\inspirit_extension\\data\\"
EXTENSION = ".png"
start_t = time.time()
cap = cv2.VideoCapture(VIDEO_PATH)
fps = round(cap.get(cv2.CAP_PROP_FPS))
print('extracting at ', KPS, 'frames per second')
print('frame count = ', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
print('width = ', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('height = ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# exit()
hop = round(fps / KPS)
curr_frame = 0
while(True):
    ret, frame = cap.read()
    if not ret: break
    if curr_frame % hop == 0:
        name = IMAGE_PATH + "_" + str(curr_frame) + EXTENSION
        cv2.imwrite(name, frame)
    curr_frame += 1
cap.release()

print('extraction complete!')
end_time = time.time()
print('finished in: ', end_time - start_t)
input('enter to exit')
#Release all space and windows once done 
cv2.destroyAllWindows()
