# Задане по лекции «Import. Module. Package»
## 1.	Разработать структуру программы "Бухгалтерия".

•	main.py;

•	директория application (приложение):

-- salary.py (зарплата);

-- директория db:

--- people.py (люди);

main.py - основной модуль для запуска программы.
В модуле salary.py функция calculate_salary (рассчитать_зарплату).
В модуле people.py функция get_employees (получить сотрудников).
## 2. Импортировать функции в модуль main.py и вызывать эти функции в конструкции.
if __name__ == '__main__': - проверяет, был ли файл запущен напрямую.

Сами функции реализовать не надо. Достаточно добавить туда какой-либо вывод.
## 3.	Познакомиться с модулем datetime. При вызове функций модуля main.py выводить текущую дату.
## *4. Создать рядом с файлом main.py модуль dirty_main.py и импортировать все функции с помощью конструкции (необязательное задание)
from package import *
### Обязательные задания выполнены, зачтено. (4 задание не выполнял так как конструкция from package import * согласно лекции считается не очень удачной)
