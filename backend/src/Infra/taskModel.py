import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime 
from ..db import db

class Task(db.Model):
    id = Column(Integer, primary_key=True)
    content = Column(String(160))
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, content, completed=False):
        self.content = content
        self.completed = completed
