'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: ORM Model Testing
'''

from sqlalchemy import *
from sqlalchemy.engine import *
from sqlalchemy.orm import *

class Base(DeclarativeBase):
    pass

# TODO: Finish the model!

class User(Base): 
    __tablename__ = "users"

class Activity(Base): 
    __tablename__ = "activities"

class Task(Base):
    __tablename__ = "tasks"

class Project(Base):
    __tablename__ = "projects"


if __name__ == "__main__": 

    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine) # creates all tables from your model classes
    Session = sessionmaker(engine)
    session = Session()
    with session: 

        # create a user 
        user = User(id=101, passwd='123')
        user.activities = []
        session.add(user)
        session.commit()

        # create projects
        prj001 = Project(code='PRJ001', title='Project 001')
        prj002 = Project(code='PRJ002', title='Project 002')
        prj003 = Project(code='PRJ003', title='Project 003')
        session.add(prj001)
        session.add(prj002)
        session.add(prj003)
        session.commit()

        # create an activity associated with PRJ001
        act = Activity(
            id=1,
            name='database design',
            start='09/21/23',
            end='09/27/23',
            status='ongoing',
            user_id=101,
            project_code='PRJ001'
        )
        session.add(act)
        session.commit()

        # create 2 tasks associated with activity 1
        task1 = Task(
            activity=1, 
            seq=1,
            name='draw an UML class diagram',
            start='09/21/23',
            end='09/21/23',
            hours=5
        )
        task2 = Task(
            activity=1, 
            seq=2,
            name='write an SQL script',
            start='09/22/23',
            end='09/22/23',
            hours=4
        )
        session.add(task1)
        session.add(task2)
        session.commit()

        # now let's try to pull all activities in the db associated with user 101
        user = session.query(User).first()
        print(user.id)
        for activity in user.activities:
            print(activity.project.code)
            print(activity.name)
            for task in activity.tasks:
                print('\t', task.name)

        