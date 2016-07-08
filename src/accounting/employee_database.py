import sqlite3

def import_employees():
    conn = sqlite3.connect('employee_db')
    cd = conn.cursor()

    cd.execute('CREATE  TABLE IF NOT EXISTS employees (emp_id TEXT PRIMARY KEY, last_name TEXT NOT NULL, first_name TEXT NOT NULL,\
        hourly_rate TEXT, salary TEXT, comm_rate TEXT, dues TEXT, pay_method TEXT)')

    hr_emp_hand = open('hourly_employees.csv', 'r')
    count = 0

    for line in hr_emp_hand:

        if count != 0:
            emp = line.split(',')
            emp[4] = emp[4].strip()
            emp[5] = emp[5].strip()
            if emp[4] == '-':
                emp[4] = '0'

            cd.execute('INSERT INTO employees(emp_id, last_name, first_name, hourly_rate, dues, pay_method) VALUES (?, ?, ?, ?, ?, ?)', (emp[0], emp[1], emp[2], emp[3], emp[4], emp[5]))

        count += 1

    hr_emp_hand.close()

    sal_emp_hand = open('salaried_employees.csv', 'r')
    count = 0

    for line in sal_emp_hand:
        if count != 0:
            emp = line.split(',')
            emp[5] = emp[5].strip()
            emp[6] = emp[6].strip()
            if emp[5] == '-':
                emp[5] = '0'

            cd.execute(
                'INSERT INTO employees(emp_id, last_name, first_name, salary, comm_rate, dues, pay_method) \
                    VALUES (?, ?, ?, ?, ?, ?, ?)', (emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6]))

        count += 1

    sal_emp_hand.close()

    conn.commit()
    conn.close()


