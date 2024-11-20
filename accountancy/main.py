from accountancy.application.db.people import get_employees
from accountancy.application.salary import calculate_salary
from datetime import datetime


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print("Сегодня", datetime.now().date())
