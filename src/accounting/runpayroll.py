import tkinter, sqlite3
from src.accounting import hourly_employee
from src.accounting import salaried_employee

class PayoutGUI:
    def __init__(self, pay_actions):
        self.pay_actions = pay_actions
        self.main_window = tkinter.Tk()
        self.main_window.geometry('800x300')

        self.labelspace = tkinter.Label(self.main_window, text='')
        self.label = tkinter.Label(self.main_window, justify='left', text=self.pay_actions)
        self.labelspace2 = tkinter.Label(self.main_window, text='')

        self.labelspace.pack()
        self.label.pack()
        self.labelspace2.pack()

        tkinter.mainloop()

def run_payroll():
    conn = sqlite3.connect('employee_db')
    cd = conn.cursor()

    cd.execute('SELECT * FROM employees WHERE hourly_rate')
    hr_all_rows = cd.fetchall()

    hr_employee_dict = {}
    for emp in hr_all_rows:
        employee = hourly_employee.HourlyEmployee(emp[0], emp[1], emp[2], emp[3], emp[6], emp[7], '25 Waterview Dr', 'Westford', 'MA', '01886')
        hr_employee_dict[emp[0]] = employee

    conn.close()

    conn = sqlite3.connect('time_card_db')
    cd = conn.cursor()
    cd.execute('SELECT * FROM t_cards WHERE emp_id')
    tc_all_rows = cd.fetchall()

    for card in tc_all_rows:
        hr_employee_dict[card[0]].clockin(card[3], card[1])
        hr_employee_dict[card[0]].clockout(card[3], card[2])


    conn.close()

    label = ''
    for emp in hr_employee_dict:
        check_pay = hr_employee_dict[emp].calc_pay()
        if check_pay == -1:
            continue
        else:
            label += check_pay + "\n"

    conn = sqlite3.connect('employee_db')
    cd = conn.cursor()

    cd.execute('SELECT * FROM employees WHERE salary')
    sal_all_rows = cd.fetchall()
    sal_employee_dict = {}

    for emp in sal_all_rows:
        employee = salaried_employee.SalariedEmployee(emp[0], emp[1], emp[2], emp[4], emp[5], emp[6], emp[7], '25 Waterview Dr',
                                                      'Westford', 'MA', '01886')
        sal_employee_dict[emp[0]] = employee

    conn.close()

    conn = sqlite3.connect('receipt_db')
    cd = conn.cursor()
    cd.execute('SELECT * FROM receipts WHERE emp_id')
    rec_all_rows = cd.fetchall()

    for rec_data in rec_all_rows:
        sal_employee_dict[rec_data[0]].create_receipt(rec_data[0], rec_data[1], rec_data[2], int(rec_data[3]), float(rec_data[4]), rec_data[5])

    conn.close()

    for emp in sal_employee_dict:
        label += (sal_employee_dict[emp].calc_pay() + "\n")

    payout_gui = PayoutGUI(label)
