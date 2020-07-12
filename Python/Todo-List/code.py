# Write your code here
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
 
Base = declarative_base()
 
 
class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default="")
    deadline = Column(Date, default=datetime.today())
 
    def __repr__(self):
        return self.task
 
 
def add_task(engine):
    task = input("Enter task: ")
    date_string = input("Enter deadline: ")
    Session = sessionmaker(bind=engine)
    session = Session()
 
    new_row = Table(task=task, deadline=datetime.strptime(date_string, "%Y-%m-%d").date())
    session.add(new_row)
    session.commit()
    print("The task has been added!")
 
 
def today_task(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(Table).all()
    to_print = []
 
    for row in rows:
        if row.deadline == datetime.today().date():
            to_print.append(row)
 
    if len(to_print) == 0:
        print("Nothing to do!")
    else:
        print(f"Today {datetime.today().day} {datetime.today().strftime('%b')}:")
        for idx, data in enumerate(to_print):
            print(f"{idx + 1}. {data.task}")
        print()
 
 
def all_tasks(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(Table).all()
 
    if len(rows) == 0:
        print("Nothing to do!")
    else:
        print("All tasks:")
        for idx, data in enumerate(rows):
            print(f"{idx + 1}. {data.task}")
        print()
 
 
def week_tasks(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
 
    days_of_the_week = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    today = datetime.today()
    for diff in range(0, 7):
        day = today + timedelta(days=diff)
        rows = session.query(Table).filter(Table.deadline == day.date()).all()
        print(f"{days_of_the_week[day.weekday()]} {day.day} {day.strftime('%b')}:")
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for idx, data in enumerate(rows):
                print(f"{idx + 1}. {data.task}")
            print()
        print()
 
 
def delete_task(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(Table).order_by(Table.deadline).all()
 
    print("Chose the number of the task you want to delete:")
    if len(rows) == 0:
        print("Nothing to delete")
    else:
        for idx, data in enumerate(rows):
            print(f"{idx + 1}. {data.task} {data.deadline.day} {data.deadline.strftime('%b')}")
        print()
 
        choice = int(input())
        session.delete(rows[choice - 1])
        session.commit()
 
        print("The task has been deleted!")
 
 
def missed_tasks(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(Table).filter(Table.deadline < datetime.today()).all()
 
    if len(rows) == 0:
        print("Nothing is missed!")
    else:
        for idx, data in enumerate(rows):
            print(f"{idx + 1}. {data.task}")
        print()
    print()
 
 
def main():
    engine = create_engine('sqlite:///todo.db?check_same_thread=False')
    Base.metadata.create_all(engine)
 
    while True:
        choice = input("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
""")
 
        if choice == '1':
            today_task(engine)
        elif choice == '2':
            week_tasks(engine)
        elif choice == '3':
            all_tasks(engine)
        elif choice == '4':
            missed_tasks(engine)
        elif choice == '5':
            add_task(engine)
        elif choice == '6':
            delete_task(engine)
        else:
            break
 
 
if __name__ == '__main__':
    main()
