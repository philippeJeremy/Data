from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///:memory:", echo=True)
# DBHOST = "HOST_FROM_AMAZON_RDS"
# DBUSER = "USERNAME"
# DBPASS = "PASSWORD"
# DBNAME = "DBNAME"
# PORT = "PORT"
# engine = create_engine(f"mysql+pymysql://{DBUSER}:{DBPASS}@{DBHOST}:{PORT}/{DBNAME}", echo=True)
# engine = create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DBNAME}", echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    # Each parameter corresponds to a column in our DB table
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='{}', fullname='{}', nickname='{}')>".format(self.name, self.fullname, self.nickname)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

ed_user = User(id=1, name='ed', fullname='Ed Jones', nickname='edsnickname')
al_user = User(id=2, name='al', fullname='Al Jones', nickname='alsnickname')
session = Session()
session.add(ed_user)
session.add(al_user)
session.commit()


user = session.query(User)
user.all()


statement = text("SELECT * FROM users where name=:name")
session.query(User).from_statement(statement).params(name="ed").all()