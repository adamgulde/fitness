### commands.py writes commands to a temporary text file which is read in main.py. 
### List of valid commands should be here, throwing an error if the given command is invalid 
###     and NOT writing to the file
import subprocess
def get_commands():
    with open('cmds.txt', 'w') as f:
            f.write('N/A')
    subprocess.call('start main.py', shell=True) # starts the cmd echo file thru command prompt (WINDOWS)
    print('Command terminal for AI')
    while(True):
        cmd = input('Input command (quit to exit):')
        if(cmd=='quit'):
            print('\nStopped speech and video recognition, enter \'restart\' to restart\n')
            with open('cmds.txt', 'w') as f:
                f.write('exit 1')
            break        
        if(cmd=='stop cam'):
            print('\nStopped video recognition, enter \'start cam\' to restart\n')
        if(cmd=='start cam'):
            print('\nStarting video recognition, enter \'stop cam\' to end\n')

            
        
        with open('cmds.txt', 'w') as f:
            f.write(cmd)
        # else print(cmd, 'is not a command!' Try 'help')
    if(input('Command: ')=='restart'):
        with open('cmds.txt', 'w') as f:
            f.write('Restarted!')
        get_commands()
        
if __name__ == "__main__":
    get_commands()