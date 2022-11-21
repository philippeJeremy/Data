from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DBHOST = "HOST_FROM_AMAZON_RDS"
# DBUSER = "USERNAME"
# DBPASS = "PASSWORD"
# DBNAME = "DBNAME"
# PORT = "PORT"

# engine = create_engine("sqlite:///:memory:", echo=True)
engine = create_engine("", echo=True)


Base = declarative_base()

class Custemer(Base):
    __tablename__ = "custemer"

 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    pays = Column(String)
    travail = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return "<Custemer(name='{}', fullname='{}', nickname='{}')>".format(self.name, self.pays, self.travail)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

choucroute_custome = Custemer(id=1, name='Choucroute', pays='Allemagne', travail='ingénieur', age=37)
jones_custome = Custemer(id=2, name='Jones', pays='Royaume-Uni', travail='journaliste', age=52)
dupont_custome = Custemer(id=3, name='Dupont', pays='France', travail='Danseur', age=25)

session = Session()

session.add(choucroute_custome)
session.add(jones_custome)
session.add(dupont_custome)

session.commit()
