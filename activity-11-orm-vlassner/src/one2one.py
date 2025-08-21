'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: An example of an 1-1 association
'''

from sqlalchemy import *
from sqlalchemy.engine import *
from sqlalchemy.orm import *

class Base(DeclarativeBase):
    pass

class President(Base): 
    __tablename__ = "presidents"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    company = relationship("Company")

class Company(Base): 
    __tablename__ = "companies"
    code = Column(Integer, primary_key=True)
    title = Column(String)
    president_id = Column(Integer, ForeignKey("presidents.id"))

if __name__ == "__main__": 

    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine) # creates all tables from your model classes
    Session = sessionmaker(engine)
    session = Session()
    with session: 

        # TO DO create (and persist) a president
        #president  = President(id = 101, name = 'Steve Jobs')
        #session.add(president)
        #session.commit()

        # TO DO create (and persist) a company associated with the president above
        #company = Company(code = 12345, title = 'apple', president_id = 101)
        #session.add(company)
        #session.commit()

        # TODO run a query to test if the objects were indeed persisted 
        try:
            prez = session.query(President).filter_by(name='Steve Jobs').one()
            if prez:
                print(prez.id, prez.name)
                company = prez.company[0]
                print(company.code, company.title)
        except:
            print('Nothing Found!')

    # go to view, command palette, type sql, open database, select the database, click SQLite explorer to find table