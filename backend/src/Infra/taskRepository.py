from ..db import db
from .taskModel import Task
class TaskRepository():

    def persist(taskContent, taskCompleted=False, taskId=None):
        if taskId is not None:
            task = db.session.query(Task).get(taskId)
        else:
            task = Task(taskContent, taskCompleted)
        
        task.content = taskContent
        task.completed = bool(taskCompleted)
        db.session.add(task)
        db.session.commit()
        return task.id
    
    def getById(id):
        task = db.session.query(Task).get(id)
        return TaskFactory.taskFromQuery(task)
    
    def getAll():
        tasks = db.session.query(Task).all()
        return TaskFactory.listFromQuery(tasks)

    def deleteById(id):
        task = db.session.query(Task).get(id)
        db.session.delete(task)
        db.session.commit()

    def complete(taskId):
        task = db.session.query(Task).get(taskId)
        task.completed = True
        db.session.commit()
        return task.id

class TaskFactory:
    def listFromQuery(tasks):
        response = []
        for task in tasks.__iter__(): 
            response.append(
                TaskFactory.taskFromQuery(task)
            )
        return response

    def taskFromQuery(task):
        taskObj = {}
        taskObj["id"] = task.id
        taskObj["content"] = task.content
        taskObj["completed"] = task.completed
        return taskObj