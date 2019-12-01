from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import Queries
engine = create_engine("sqlite:///db1.sqlite")
session = Session(bind=engine)

c1 = Queries.Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              )

c2 = Queries.Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              )

session.add(c1)
session.add(c2)
session.commit()
print(c1.id)