import subprocess
import time
while True:
    print ("Starting bot...")
    g = subprocess.run("git pull", check=True) #Pulls the latest code from GitHub
    if g.returncode != 0:
        print ("""Error pulling code from github, this is
            likely because you don't have git installed,
            if you do have git installed,
            please check your configuration for git
            and try again""")
    p = subprocess.run("py main.py", check=True)
    print('Restarting bot...')
    time.sleep(4)
