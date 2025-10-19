import subprocess 

def run_command (Test_session_management): 


    # BAD PRACTICE: using shell=True makes the code vulnerable to command injection
    subprocess.run ("echo" + Test_session_management , shell = True ) 