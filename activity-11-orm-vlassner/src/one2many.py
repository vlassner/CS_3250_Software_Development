'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: An example of an 1-many association
'''

from sqlalchemy import *
from sqlalchemy.engine import *
from sqlalchemy.orm import *

class Base(DeclarativeBase):
    pass

class Employee(Base): 
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dep_code = Column(Integer, ForeignKey("departments.code"))
    department = relationship("Department")

class Department(Base): 
    __tablename__ = "departments"
    code = Column(String, primary_key=True)
    description = Column(String)
    employees = relationship("Employee", back_populates='department')

if __name__ == "__main__": 

    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine) # creates all tables from your model classes
    Session = sessionmaker(engine)
    session = Session()
    with session: 

        # TODO create (and persist) 3 departments
        # hr = Department(
        #     code='HR',
        #     description='Human Resources',
        #     employees=[
        #         Employee(id=101,name='Janet'),
        #         Employee(id = 202, name='Bob')
        #     ]
        #     )
        # session.add(hr)
        # session.commit()
        
        

        # TODO create (and persist) 3 employees
        # alex = Employee(
        #     id=303,
        #     name='Alex',
        #     department=Department(
        #         code='IT',
        #         description='Information Technology'
        #     )
        # )
        # session.add(alex)
        # session.commit()

        # TODO run an employee query to test if the objects were indeed persisted 
        employees = session.query(Employee).filter().all()
        print(f'employee\tdeparment')
        for employee in employees:
            print(f'{employee.name}\t\t{employee.department.description}')
        print()

        # TODO run a department query to test if the objects were indeed persisted 
        print('Employees working in HR')
        hr = session.query(Department).filter(Department.code=='HR').one()
        for employee in hr.employees:
            print(f'{employee.name}')
        
