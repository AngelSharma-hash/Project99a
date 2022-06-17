import imp
import os
import shutil
import time
import imp

path = str(input("Enter the directory"))
days = float(input("Enter the number of days"))
current_time = time.time()
numberofseconds = days*24*3600
time_difference = current_time - numberofseconds
if os.path.exists(path):
    for root,folder,files in os.walk(path):
        for f in files:
        
            oldTime = os.path.join(root,f)
            ctime = os.stat(path).st_ctime
            if time_difference > ctime:
                os.remove(path)
                print("Files is removed")
            else:
                shutil.rmtree()
                print("Files at"+path)
    
else:
    print("The file doesn't exist")
