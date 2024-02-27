import csv
import time
import rpyc

class Task:
    def __init__(self, name, description, dueDate):
        self.name = name
        self.description = description
        self.dueDate = dueDate
    def get_name(self):
        return(self.name)
    def get_description(self):
        return(self.description)
    def get_dueDate(self):
        return(self.dueDate)

def tasksToRawData(tasks):
    rawData = []
    for task in tasks:
        print(task)
        rawData.append([task.get_name(),task.get_description(),task.get_dueDate()])
    return(rawData)

def rawDataToTasks():
    tasks = []
    with open("tasksDatabase.csv", 'r') as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            task = Task(row[0],row[1],row[2])
            tasks.append(task)
        return(tasks)

def saveRawData(rawData):
    with open("tasksDatabase.csv",'w',newline = '') as csvfile:
        csvWriter = csv.writer(csvfile)
        for row in rawData:
            csvWriter.writerow(row)

def addTask(task,tasks):
    index = 0
    for taskToCheck in tasks:
        if task.dueDate < taskToCheck.dueDate:
            tasks.insert(index,task)
            return(tasks)
    tasks.append(task)

def checkForNotifications(tasks):
    tasksToNotifyAbout = []
    currentTime = int(time.time())
    for task in tasks:
        if task.dueDate < currentTime + 172800:
            if task.dueDate > currenTime + 172200:
                tasksToNotifyAbout.append(task)
    return(tasksToNotifyAbout)

class NotificationService(rpyc.Service):
    def on_connect(self, conn):
        print("Connection Made")
    def on_disconnect(self,conn):
        print("Disconnected")
    def exposed_CheckForNotifications(self, notificationCheckingInterval):
        tasks = rawDataToTasks()
        currentTime = int(time.time())
        tasksToNotifyAbout = []
        for task in tasks:
            print(currentTime + 172800)
            if int(task.dueDate) < currentTime + 172800:
                print(f"Less Than 2 Days Away: {task.name}")
                if int(task.dueDate) > currentTime + 172800 - notificationCheckingInterval:
                    tasksToNotifyAbout.append(task)
        payload = []
        for task in tasksToNotifyAbout:
            payload.append([task.name,task.description,task.dueDate])
        return payload
    
    def exposed_AddTask(self,task):
        task = Task(task[0],task[1],task[2])
        print(task.name)
        tasks = rawDataToTasks()
        print(tasks)
        index = 0
        for taskToCheck in tasks:
            if task.dueDate < taskToCheck.dueDate:
                tasks.insert(index,task)
                saveRawData(tasksToRawData(tasks))
                return(tasks)
        tasks.append(task)
        saveRawData(tasksToRawData(tasks))
        print(task)
        return(12)

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(NotificationService, port=18861)
    t.start()
            
    

