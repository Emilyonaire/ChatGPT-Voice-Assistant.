import subprocess, os
path = os.getcwd() + '\\example.mp3'
print(path)

speed = 1.5
command = ["ffplay", "-nodisp", "-autoexit", "-af", "atempo={}".format(speed), path]
cmd2 = ["ffplay", "-version"]
subprocess.call(command)

# subprocess.call(cmd2)