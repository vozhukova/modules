from application.salary import calculate_salary as cs_
from application.db.people import get_employees as ge_
from datetime import datetime

if __name__ == '__main__':
    cs_()
    ge_()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

