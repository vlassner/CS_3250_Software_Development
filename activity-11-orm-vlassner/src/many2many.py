'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: An example of an many-many association
'''

from sqlalchemy import *
from sqlalchemy.engine import *
from sqlalchemy.orm import *

class Base(DeclarativeBase):
    pass

employee_projects = Table(
    'employee_projects', 
    Base.metadata, 
    Column('employee.id', ForeignKey('employees.id')), 
    Column('project.code', ForeignKey('projects.code'))
)

class Employee(Base): 
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    projects = relationship("Project", secondary=employee_projects, back_populates='employees')

class Project(Base): 
    __tablename__ = "projects"
    code = Column(String, primary_key=True)
    description = Column(String)
    employees = relationship("Employee", secondary=employee_projects, back_populates='projects')

if __name__ == "__main__": 

    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine) # creates all tables from your model classes
    Session = sessionmaker(engine)
    session = Session()
    with session: 

        # TODO create (and persist) 3 projects
        janet = Employee(id=101, name='Janet')
        bob = Employee(id=202, name = 'Bob')
        mark = Employee(id=303, name = 'Mark')
        
        artemis = Project(
            code='ART',
            description='Artemis Project',
            employees=[
                janet,
                bob
            ]
        )

        luna = Project(
            code='LNT',
            description = 'Luna Project',
            employees=[
                janet,
                mark
            ]
        )
        session.add(artemis)
        session.add(luna)
        session.commit()


        # TODO create (and persist) 3 employees
    

        # TODO create some employee-project associations 
        

        # TODO run an employee query to test if the objects were indeed persisted 
        

        # TODO run a project query to test if the objects were indeed persisted 
        
        
