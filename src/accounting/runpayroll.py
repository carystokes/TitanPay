
from src.accounting import hourly_employee

def run_payroll():
    hr_emp_hand = open('hourly_employees.csv', 'r')
    count = 0
    hr_employee_dict = {}
    for line in hr_emp_hand:

        if count != 0:
            emp = line.split(',')
            emp[4] = emp[4].strip()
            emp[5] = emp[5].strip()
            if emp[4] == '-':
                emp[4] = 0
            employee = hourly_employee.HourlyEmployee(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], '25 Waterview Dr', 'Westford', 'MA', '01886')
            hr_employee_dict[emp[0]] = employee

        count += 1

    hr_emp_hand.close()

    tc_hand = open('timecards.csv', 'r')
    count = 0
    for line in tc_hand:

        if count != 0:
            tc = line.split(',')
            tc[3] = tc[3].strip()

            hr_employee_dict[tc[0]].clockin(tc[3], tc[1])
            hr_employee_dict[tc[0]].clockout(tc[3], tc[2])

        count += 1

    tc_hand.close()

    for emp in hr_employee_dict:
        hr_employee_dict[emp].calc_pay()

