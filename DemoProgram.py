import rpyc
from NotificationService import Task
import asyncio
import time

async def CheckForNotification():
    while True:
        tasksToNotifyAbout = connection.root.CheckForNotifications(120)
        for task in tasksToNotifyAbout:
            print(task)
        await asyncio.sleep(120)
        
connection = rpyc.connect("localhost", 18861)
timeCheck = str(int(time.time()) + 172800 - 60)
rawList = [
           ["Task 1","Lorem Ipsum",timeCheck],
           ["Task 2","Lorem Ipsum","123412231"],
           ["Task 3","Lorem Ipsum","123412231"] 
          ]

for task in rawList:
    connection.root.AddTask(task)
    

asyncio.run(CheckForNotification())
