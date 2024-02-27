# Notification Microservice
## Installation
Download the repo. Also make sure to install the python library rpyc.

## Launch
Just run NotificationService.py. Connect to the server at port localhost:18861. You can connect by doing the following.
```
connection = rpyc.connect("localhost", 18861)
```

## Making Calls
### Adding Tasks
Add tasks to the database by using AddTask(task).
```
connection.root.AddTask(task)
```
task has to be of following structure
```
task = [taskName,taskDescription,taskDueDate(in Unix Time Stamp)]
```
### Checking for Notifications
Check if any task is coming up soon.
```
tasksToNotifyAbout = connection.root.CheckForNotifications(notificationCheckingInterval)
```
if there are any tasks that are less than 2 days away, then the microservice will return it an the same strucutre as detailed above.
