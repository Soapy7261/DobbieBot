#This is for restarting the python script, before you make a pr to use os.exec() instead, please know that it doesn't run new code, it just restarts the existing script, so you'll have to restart the script manually after making changes
import subprocess, time
while True:
    print ("Starting bot...")
    g = subprocess.run("git pull") # Pulls the latest code from GitHub, if you do not have git installed, you can remove this line
    if g.returncode != 0:
        print ("Error pulling code from github, this is likely because you don't have git installed, if you do have git installed, please check your configuration for git and try again")
        time.sleep(5)
        pass
    p = subprocess.run('py main.py')
    if p.returncode != 0:
        print ("Hmmm, something went wrong, restarting in 8 seconds...")
    print('Restarting bot...')
    time.sleep(4) #This is to prevent the script from restarting too fast, which causes discord to get rate limited