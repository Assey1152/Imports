from accountancy.application.db.people import *
from accountancy.application.salary import *
from datetime import *


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print("Сегодня", datetime.now().date())
