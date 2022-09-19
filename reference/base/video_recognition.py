from math import sqrt
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
import time
import os
parentDirectory = str(os.path.dirname(__file__))  
landmarks1, landmarks2 = None, None
import mouse
import screeninfo
screen_width, screen_height = 0, 0
for monitor in screeninfo.get_monitors():
    screen_width = monitor.width
    screen_height = monitor.height
    break


def main():
    d_time = 0 # used for timers, such as fps
    vid = cv2.VideoCapture(0)
    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
        max_num_hands=2) as hands:
        while(vid.isOpened()): # webcam playback loop
            ret, frame = vid.read()
            ### Additional functions below:
            cmd, frame = get_commands(frame, hands) # instead of printing, get_commands will eventually run another file or otherwise result in the command given
            d_time = get_FPS(frame, d_time) # pastes FPS on video frame
            if(cmd=='exit 1'): 
                break
            if(cmd=='stop cam'): vid.release()
            ### Additional functions above
            cv2.imshow('Video Input', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): # closes video stream prematurely with Q as exit code
                    vid.release() # end of loop

    cv2.destroyAllWindows()

def get_FPS(vid_stream, d_time):
    cTime = time.time()
    fps = 1/(cTime-d_time)
    cv2.putText(vid_stream, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,125,255), 3)
    return cTime

def get_commands(image, hands):
    cmd = None
    with open(parentDirectory + '\cmds.txt') as cmds: # check for absolute kill cmd
        cmd = cmds.readline()
        if cmd=='exit 1': return cmd
    ## video input cmds below
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    results = hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        num_hands=len(results.multi_hand_landmarks)
        landmarks1 = results.multi_hand_landmarks[0]
        if num_hands > 1:
            landmarks2 = results.multi_hand_landmarks[1]
        # for hand_landmarks in results.multi_hand_landmarks:
        #     mp_drawing.draw_landmarks(  ### to drawn landmarks with mediapipe itself
        #         image, 
        #         hand_landmarks,
        #         mp_hands.HAND_CONNECTIONS,
        #         mp_drawing_styles.get_default_hand_landmarks_style(),
        #         mp_drawing_styles.get_default_hand_connections_style())
        height, width, c = image.shape
        wrist_coords1 = (int(landmarks1.landmark[0].x*width), int(landmarks1.landmark[0].y*height))
        thumb_coords1 = (int(landmarks1.landmark[4].x*width), int(landmarks1.landmark[4].y*height))
        index_coords1 = (int(landmarks1.landmark[8].x*width), int(landmarks1.landmark[8].y*height))
        middle_coords1 = (int(landmarks1.landmark[12].x*width), int(landmarks1.landmark[12].y*height))
        ring_coords1 = (int(landmarks1.landmark[16].x*width), int(landmarks1.landmark[16].y*height))
        pinky_coords1 = (int(landmarks1.landmark[20].x*width), int(landmarks1.landmark[20].y*height))

        if num_hands > 1:
            wrist_coords2 = (int(landmarks2.landmark[0].x*width), int(landmarks2.landmark[0].y*height))
            thumb_coords2 = (int(landmarks2.landmark[4].x*width), int(landmarks2.landmark[4].y*height))
            index_coords2 = (int(landmarks2.landmark[8].x*width), int(landmarks2.landmark[8].y*height))
            middle_coords2 = (int(landmarks2.landmark[12].x*width), int(landmarks2.landmark[12].y*height))
            ring_coords2 = (int(landmarks2.landmark[16].x*width), int(landmarks2.landmark[16].y*height))
            pinky_coords2 = (int(landmarks2.landmark[20].x*width), int(landmarks2.landmark[20].y*height))
        
        if True: ### flag true to draw fingertip landmarks
            cv2.circle(image, wrist_coords1, 5, (0,0,0), 3)         # wrist
            cv2.circle(image, thumb_coords1, 5, (255,255,255), 3)   # thumb
            cv2.circle(image, index_coords1, 5, (0,255,255), 3)     # index
            cv2.circle(image, middle_coords1, 5, (0,255,0), 3)     # middle
            cv2.circle(image, ring_coords1, 5, (127,127,0), 3)   # ring
            cv2.circle(image, pinky_coords1, 5, (255,86,255), 3)  # pinky

            cv2.line(image, (middle_coords1), (wrist_coords1), (0,0,255))
            cv2.line(image, (index_coords1), (wrist_coords1), (0,0,255))
            cv2.line(image, (ring_coords1), (wrist_coords1), (0,0,255))
            cv2.line(image, (pinky_coords1), (wrist_coords1), (0,0,255))

            if num_hands > 1:
                cv2.circle(image, (int(landmarks2.landmark[9].x*width), int(landmarks2.landmark[9].y*height)), 7, (0,0,0), 3)  # hand 2
        
        # mouse ctrl command (one hand, index finger up and other fingers in palm):
        if ((hypotenuse(ring_coords1[0], ring_coords1[1], middle_coords1[0], middle_coords1[1]) +
            hypotenuse(pinky_coords1[0], pinky_coords1[1], ring_coords1[0], ring_coords1[1]) < 50) and
            hypotenuse(wrist_coords1[0], wrist_coords1[1], index_coords1[0], index_coords1[1]) > 100):
            
            with open(parentDirectory + '\cmds.txt', 'w') as f:
                        f.write('mouse tracking hand')  
            scale_by = (screen_width / image.shape[1], screen_height / image.shape[0])
            CUSHION = 1.1
            mouse.move(screen_width - index_coords1[0] * scale_by[0] * 1.1, index_coords1[1] * scale_by[1] * 1.1)
            # mouse click command (one hand, pinch index + middle + thumb):
            # if(hypotenuse(index_coords1[0], index_coords1[1], middle_coords1[0], middle_coords1[1]) < 10):
            #     mouse.click()
            #     with open(parentDirectory + '\cmds.txt', 'w') as f:
            #             f.write('hand ctrl mouse click')
        
        # break command (two fists, closed):
        if (hypotenuse(wrist_coords1[0], wrist_coords1[1], middle_coords1[0], middle_coords1[1]) + 
            hypotenuse(wrist_coords1[0], wrist_coords1[1], index_coords1[0], index_coords1[1]) +
            hypotenuse(wrist_coords1[0], wrist_coords1[1], ring_coords1[0], ring_coords1[1]) +
            hypotenuse(wrist_coords1[0], wrist_coords1[1], pinky_coords1[0], pinky_coords1[1]) < 120):
            if num_hands > 1:
                if(hypotenuse(wrist_coords2[0], wrist_coords2[1], middle_coords2[0], middle_coords2[1]) + 
                   hypotenuse(wrist_coords2[0], wrist_coords2[1], index_coords2[0], index_coords2[1]) +
                   hypotenuse(wrist_coords2[0], wrist_coords2[1], ring_coords2[0], ring_coords2[1]) +
                   hypotenuse(wrist_coords2[0], wrist_coords2[1], pinky_coords2[0], pinky_coords2[1]) < 120):
                    with open(parentDirectory + '\cmds.txt', 'w') as f:
                        f.write('stop cam')
        

    return cmd, cv2.flip(image, 1)

def hypotenuse(x1, y1, x2, y2):
    ret_val = 0
    x = x1 - x2
    y = y1 - y2
    ret_val = sqrt(x*x+y*y)
    return ret_val

if __name__ == "__main__":
    main()
