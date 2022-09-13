### Main will echo text commands- leads to other scripts when valid command is inputted
import time
import os
import video_recognition
import idle
parentDirectory = str(os.path.dirname(__file__))
START_TIME = time.time()

def main():    
    c_cmd = None
    while True:
        cmd = get_commands()
        if(c_cmd != cmd):
            c_cmd = cmd
            print(f'Command received! {cmd}')
        else:
            c_cmd = cmd
        if(cmd=='start cam'):
            video_recognition.main()
        if(cmd=='idle'):
            idle.idle()
        if(cmd=='exit 1'):
            break

def get_commands():
    with open('cmds.txt') as cmds:
        cmd = cmds.readline()
        if(cmd!='N/A'):
            return cmd
        else:
            return ('Started at: ', START_TIME)

if __name__ == "__main__":
    main()