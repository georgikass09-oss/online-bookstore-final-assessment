import subprocess 

def run_command (password_security): 

    # BAD PRACTICE: using shell=True makes the code vulnerable to command injection
    subprocess.run ("echo" + password_security, shell = True ) 