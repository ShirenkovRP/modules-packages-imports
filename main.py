from datetime import datetime
from application.salary import calculate_salary
from db.people import get_employees


print(datetime.today())



def main():
    employee = get_employees()
    may_salary = calculate_salary()
    print(f"Имя сотрудника {employee}")
    print(f"Зарплата {may_salary}")


if __name__ == '__main__':
    main()
