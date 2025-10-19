import subprocess 

def run_command ( Test_input_validation): 

# BAD PRACTICE: using shell=True makes the code vulnerable to command injection
    subprocess.run ( "echo" + Test_input_validation , shell = True )