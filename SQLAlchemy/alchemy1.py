from sqlalchemy import Column, String, Integer, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('mysql://root@localhost/ANITA')


Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Bochka(Base):
    __tablename__ = 'BochkTable'
    bochka_id = Column(Integer, primary_key=True)
    # make sure that we don't forget the value for String:
    bochka_name = Column(String(50), index=True)
    bochka_recipe = Column(String(255))
    quantity = Column(Integer)
    unit_cost = Column(Numeric(12, 2))


# creates the table:
Base.metadata.create_all(engine)

# instance (object) that is created but not yet in the DB:
bochka1 = Bochka(bochka_name='chatul',
                 bochka_recipe='www.bochkes.com',
                 quantity=3,
                 unit_cost=.4)

session.add(bochka1)
session.commit()

print(bochka1.bochka_id)

Bochkas = session.query(Bochka.bochka_recipe).all()
print(Bochkas[0])


# func recognizes what engine is working and DB is used,
# such that specific funcs of that DB can be used.
# so, func.sum would actually call the sum that exist under the
# specific engine (mysql/ sqlite etc...)

from SQLAlchemy import func



# session.close()
